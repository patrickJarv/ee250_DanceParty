import time
def strobe(data):
    beats = data
    timing = []
    for beat in beats:
        timer = (beat['start']) - (beat['start'] % 0.01)
        timing.append(round(timer, 2))

    sec = 0
    idx = 0
    while True:
        if(idx == len(timing)):
            break
        else:
            if(round(sec, 2) == timing[idx]):
                print("test")
                idx = idx + 1
            sec = sec + 0.01
            time.sleep(0.01)


