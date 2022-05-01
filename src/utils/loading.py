import time 


class Loading:
    def __init__(self):
        self.do_reset = True

    def reset(self, max_value):
        self.max_value = max_value
        self.pourcentage = 0
        self.pourcentage_showed = []
        self.last_showing_msg = time.time()
        self.period = 3
        self.do_reset = False

    def show_loading_msg(self, current_value, max_value, custom_msg=""):
        if self.do_reset:
            self.reset(max_value)

        if current_value >= max_value:
            self.do_reset = True

        # make value go into a 0-100 scale
        pourcentage_value = (current_value * 100) / self.max_value
        while pourcentage_value > self.pourcentage:
            self.pourcentage += 1

        if self.pourcentage == 100:
            if self.pourcentage not in self.pourcentage_showed:
                print(custom_msg, "Loading 100%")
                self.pourcentage_showed.append(self.pourcentage)
            else:
                return

        # every self.period time, display new loading state if it has changed
        # thus when loading is fast, prgm is not slowed due to multiple print
        elif time.time() - self.last_showing_msg > self.period:
            if self.pourcentage not in self.pourcentage_showed:
                self.last_showing_msg = time.time()
                self.pourcentage_showed.append(self.pourcentage)
                print(custom_msg, "Loading {}%".format(self.pourcentage))
