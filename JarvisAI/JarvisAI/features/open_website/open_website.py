import re
import webbrowser


def website_opener(data, models):
    inp = data['user_input']
    reg_ex = re.search('open (.+)', inp)
    if reg_ex:
        domain = reg_ex.group(1)
        print(domain)
        url = 'https://www.' + domain
        webbrowser.open(url)
        return 'The website you have requested has been opened for you Sir.'
    else:
        return 'Unable to open website'
