# import statements
import datetime


# do not remove data=None, model=None the function format should be same, name can be change
# inp is the input from the user (query ask by user)
# you can use this inp inside the function. LOL, because you may need user input
# Function should return something because this is the output we want to show user
def tell_me_date(data=None, model=None):
    """
    Do not remove data=None, model=None
    data is:
    data = {
            'user_input': inp, # input from user
            'features_config': jarvis_obj.features_config, # this will use to find the correct funtion which needs to be call
            'user_config': jarvis_obj.user_config, # user releated configurations. Just print it for more details.
            'DEV_MODE': DEV_MODE, # True / False is only possible values
            'jarvis_obj': jarvis_obj # jarvis_obj is object of Jarvis class. Read the jarvis.py for more details.
        }
    """
    date = datetime.datetime.now().strftime("%b %d %Y")
    # the return format should be string or integer only. The only one return should be here.
    return date


def tell_me_time(data=None, model=None):
    time = datetime.datetime.now().strftime("%H:%M")
    # the return format should be string or integer only
    return time


# you can run and test your script by calling from main
if __name__ == '__main__':
    response = tell_me_date()
    print(response)
    response = tell_me_time()
    print(response)
