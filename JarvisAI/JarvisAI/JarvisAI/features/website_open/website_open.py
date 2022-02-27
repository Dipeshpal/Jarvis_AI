import webbrowser
import requests
import re

DOMAINS = [
    ".com",
    ".io",
    ".xyz",
    ".co",
    ".uk",
    ".gov.uk",
    ".gov",
    ".scot",
    "co.uk",
    ".shop",
    ".org",
    ".org.uk",
    ".net",
    ".ai",
    ".ca",
    ".dev",
    ".me",
    ".art",
    ".health",
    ".live",
    ".info",
    ".studio",
    ".biz",
    ".gay",
    ".cc",
    ".so",
    ".to",
    ".ac",
    ".cx",
    ".sh"
]


def website_opener(domain):
    extension = re.search(r"[.]", domain)
    if not extension:
        for i in DOMAINS:
            try:
                result = requests.get(f'http://{domain}{i}', timeout=10)
                result = str(result).split(" ")
                result = result[1].replace(">", "")

                if result == "[200]":
                    domain = domain + i
                    print(domain)
            except:
                continue
    try:
        url = 'https://www.' + domain
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    website_opener("facebook")
