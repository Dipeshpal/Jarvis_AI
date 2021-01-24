import pyjokes


def tell_me_joke(lang, cat):
    """
    Function to tell a joke
    Read https://pyjok.es/api/ for more details
    :param language: str
    :param category: str
    :return: str
        "Joke:
    """
    return pyjokes.get_joke(language=lang, category=cat)


if __name__ == '__main__':
    print(tell_me_joke())
