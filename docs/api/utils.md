Utils package
==========

# class Loading
## Loading.show_loading_msg(current_value, max_value)
*int* current_value: current value of the iteration  
*int* max_value: value reach at the end of iteration  
Take a value and transform in into a pourcentage. Every 3 seconds, if pourcentage has advanced, it display a msg to the user until the task is done.  

# class TimeMath
## TimeMath.start_running_time()
Reeset internal timer.  
## TimeMath.show_running_time(reset=False)
*bool* reset: force timer to reset  
Print to user running time between reset and call of the fuction.  
