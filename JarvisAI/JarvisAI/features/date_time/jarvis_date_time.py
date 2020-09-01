# import statements
import datetime


# do not remove inp=None the function format should be same, name can be change
# inp is the input from the user (query ask by user)
# you can use this inp inside the function. LOL, because you may need user input
# Function should return something because this is the output we want to show user
def tell_me_date(data=None, model=None):
    # inp = inp_and_userconfig['inp']  # user input as string
    # user_config = inp_and_userconfig['user_config']  # user_config as dict
    # user_config = {
    #     "name": "Sir",
    #     "age": 22,
    #     "city": "Indore"
    # }
    # inp (do something if you want to do with inp)
    date = datetime.datetime.now().strftime("%b %d %Y")
    # the return format should be string or integer only
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
