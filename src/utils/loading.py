import time 


class Loading:
    def __init__(self, max_value):
        self.max_value = max_value
        self.pourcentage = 0
        self.pourcentage_showed = []
        self.last_showing_msg = time.time()
        self.period = 3

    def show_loading_msg(self, current_value):
        pourcentage_value = (current_value * 100) / self.max_value
        while pourcentage_value > self.pourcentage:
            self.pourcentage += 1
        if self.pourcentage == 100:
            print("-- Loading Done! ---")
            self.reset()
        if time.time() - self.last_showing_msg > self.period:
            if self.pourcentage not in self.pourcentage_showed:
                self.last_showing_msg = time.time()
                self.pourcentage_showed.append(self.pourcentage)
                print("--- Loading {}% ---".format(self.pourcentage))
