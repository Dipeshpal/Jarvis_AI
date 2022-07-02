import random


def greet(*args, **kwargs):
    ch = ['hi', 'hello', 'hey', 'howdy', 'hi how are you', 'whats up', 'hey there', 'hello there', 'hey there',
          'hello there', 'hi there']
    return random.choice(ch)
