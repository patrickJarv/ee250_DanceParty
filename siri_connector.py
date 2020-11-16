import time
import imaplib
import email
import json
import os
import pkgutil
import paho.mqtt.client as mqtt

##########################################

username = "ee250projecttemp"
password = "EE250temp"

##########################################


class ControlException(Exception):
    pass


class Control():
    x = None
    cut = False
    def __init__(self, username, password, client):
        try:
            self.clientRP = client
            self.last_checked = -1
            self.mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
            self.mail.login(username, password)
            self.mail.list()
            self.mail.select("Notes")

            # Gets last Note id to stop last command from executing
            result, uidlist = self.mail.search(None, "ALL")
            try:
                self.last_checked = uidlist[0].split()[-1]
            except IndexError:
                pass

            self.load()
            self.handle()
        except imaplib.IMAP4.error:
            print("Your username and password is incorrect")
            print("Or IMAP is not enabled.")

    def load(self):
        """Try to load all modules found in the modules folder"""
        print("\nWelcome to the Dance Party! Time to start playing song.\n")
        self.modules = []
        path = os.path.join(os.path.dirname(__file__), "modules")
        directory = pkgutil.iter_modules(path=[path])
        for finder, name, ispkg in directory:
            try:
                loader = finder.find_module(name)
                module = loader.load_module(name)
                if hasattr(module, "commandWords") \
                        and hasattr(module, "moduleName") \
                        and hasattr(module, "execute"):
                    self.modules.append(module)
                else:
                    print("[ERROR] The module '{0}' is not in the "
                          "correct format.".format(name))
            except:
                print("[ERROR] The module '" + name + "' has some errors.")
        print("\n")

    def fetch_command(self):
        """Retrieve the last Note created if new id found"""
        self.mail.list()
        self.mail.select("Notes")

        result, uidlist = self.mail.search(None, "ALL")
        try:
            latest_email_id = uidlist[0].split()[-1]
        except IndexError:
            return

        if latest_email_id == self.last_checked:
            return

        self.last_checked = latest_email_id
        result, data = self.mail.fetch(latest_email_id, "(RFC822)")
        voice_command = email.message_from_string(data[0][1].decode('utf-8'))
        return str(voice_command.get_payload()).lower().strip()

    def handle(self):
        """Handle new commands

        Poll continuously every second and check for new commands.
        """
        while True:
            try:
                command = self.fetch_command()
                if not command:
                    raise ControlException("No command found.")

                for module in self.modules:
                    foundWords = []
                    for word in module.commandWords:
                        if str(word) in command:
                            foundWords.append(str(word))
                    if len(foundWords) == len(module.commandWords):
                        # try:
                        response = module.execute(command)
                        if response == "ERROR":
                            print("Invalid command. Try again.")
                        if response == "Setup":
                            print("Setup complete.")
                        else:
                            index = response.find('#$#');
                            beats = json.loads(response[index+3:])
                            index2 = response.find('#%#')
                            artist = response[0:index2]
                            song = response[index2+3:index]
                            print("Playing " + song.upper() + " by " + artist.upper())
                                # print(response[index+3:])
                                # print(response[0:index])
                            self.clientRP.publish("raspberrypi/lcd", response[0:index])
                            self.clientRP.publish("raspberrypi/led", response[index+3:])
                        # except:
                        #     print("[ERROR] There has been an error "
                        #           "when running the {0} module".format(
                        #               module.moduleName))
            except (TypeError, ControlException):
                pass
            except Exception as exc:
                print("The request is not included in the API. Try Again.")
            time.sleep(1)



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here

#Default message callback. Never used
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #subprocess.run(["export"], ["SPOTIPY_CLIENT_ID=1b237c5da7d04e7f91638b02b735bdc0"])
    os.environ["SPOTIPY_CLIENT_ID"] = "1b237c5da7d04e7f91638b02b735bdc0"
    os.environ["SPOTIPY_CLIENT_SECRET"]= "93ceac2198fe4ee6af0bb614847e0a0d"
    os.environ["SPOTIPY_REDIRECT_URI"]= "https://google.com"
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    control = Control(username, password, client)

    while True:
        time.sleep(1)
