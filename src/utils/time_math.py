import time


class TimeMath:
    def __init__(self):
        self.start_time = time.time()

    def convert_seconds_into_time(self, time):
        seconds = 0 
        minutes = 0
        hours = 0
        while time > 3600:
            hours += 1
            time -= 3600
        while time > 60:
            minutes += 1
            time -= 60
        seconds = int(time)
        return hours, minutes, seconds

    def start_running_time(self):
        self.start_time = time.time()

    def show_running_time(self, reset=False):
        # Print running time
        end_time = time.time() - self.start_time
        h, m, s = self.convert_seconds_into_time(end_time)
        print("--- Time of running: {}h {}min {}sec".format(h, m, s))

        if reset:
            self.start_running_time()
