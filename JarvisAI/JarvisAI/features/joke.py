import pyjokes


def tell_me_joke(*args, **kwargs):
    """
    Function to tell a joke
    Read https://pyjok.es/api/ for more details
    :return: str
    """
    lang = kwargs.get("lang", "en")
    cat = kwargs.get("cat", "neutral")
    return pyjokes.get_joke(language=lang, category=cat)


if __name__ == '__main__':
    print(tell_me_joke())
