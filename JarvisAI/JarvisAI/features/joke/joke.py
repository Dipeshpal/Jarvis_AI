import pyjokes


def tell_me_joke(inp_command=None, lang='en', cat='neutral'):
    """
    Function to tell a joke
    Read https://pyjok.es/api/ for more details
    :param inp_command: input command
    :param lang: str
    :param cat: str
    :return: str
    """
    return pyjokes.get_joke(language=lang, category=cat)


if __name__ == '__main__':
    print(tell_me_joke())
