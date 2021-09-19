import webbrowser
import re


def website_opener(domain):
    extension = re.search(r"[.]", domain)
    if not extension:
        if not domain.endswith(".com"):
            domain = domain + ".com"
    try:
        url = 'https://www.' + domain
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    website_opener("facebook")
