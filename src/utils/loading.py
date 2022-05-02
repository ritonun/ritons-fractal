import time 


class Loading:
    """Handle loading bar with text msg to user 
    
    Attributes:
        do_reset (bool): Reset loading bar to 0%
        last_showing_msg (float): last time in seconds a loading msg was showed to user
        max_value (int): max_value possible for number of iteration
        period (int): Period of time between two msg to user
        pourcentage (int): Total advancement of the task
        pourcentage_showed (list): List that keep all value showed to user
    """
    def __init__(self):
        self.do_reset = True

    def reset(self, max_value):
        """Reset the loading to zero 
        
        Args:
            max_value (int): max_value possible for number of iteration
        """
        self.max_value = max_value
        self.pourcentage = 0
        self.pourcentage_showed = []
        self.last_showing_msg = time.time()
        self.period = 3
        self.do_reset = False

    def show_loading_msg(self, current_value, max_value, custom_msg=""):
        """
        Show progress of task to user in %.
        current_value is the current_value of iteration in the loop.
        max_value is the maximum number of iteration it will go through.
        
        Args:
            current_value (int): current value of loop iteration
            max_value (int): max_value possible for number of iteration
            custom_msg (str, optional): Start the loading msg with a custom msg
        """
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
