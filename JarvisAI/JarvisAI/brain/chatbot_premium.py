import requests
from googlesearch import search
import wikipedia
import html2text
from bs4 import BeautifulSoup
from markdown import markdown
import re


def search_google_description(query):
    try:
        ans = search(query, advanced=True, num_results=5)

        desc = ''
        for i in ans:
            desc += i.description

        return desc
    except:
        return ''


def query_pages(query):
    return list(search(query))


def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    for e in soup.find_all():
        if e.name not in ['p']:
            e.unwrap()
    text = ''.join([i.strip() for i in soup.findAll(text=True)])
    return text


def format_text(text):
    text = markdown_to_text(text)
    text = text.replace('\n', ' ')
    return text


def search_google(query):
    try:
        def query_to_text(query):
            html_conv = html2text.HTML2Text()
            html_conv.ignore_links = True
            html_conv.escape_all = True
            text = []
            for link in query_pages(query)[0:3]:
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

                    req = requests.get(link, headers=headers)
                    text.append(html_conv.handle(req.text))
                    text[-1] = format_text(text[-1])
                except:
                    pass
            return text

        return query_to_text(query)
    except:
        return ''


def search_wiki(query):
    try:
        ans = wikipedia.summary(query, sentences=2)
        return ans
    except:
        return ''


def search_all(query, advance_search=False):
    combined = search_google_description(query) + "\n" + search_wiki(query)
    if advance_search:
        combined += "\n" + ' '.join(search_google(query))
    return combined


def try_to_get_response(*args, **kwargs):
    api_key = kwargs.get("api_key")
    query = kwargs.get('query')
    context = search_all(query, advance_search=False)
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    params = {
        'secret_key': api_key,
        'text': query,
        'context': context,
    }
    response = requests.post('https://www.jarvisai.in/chatbot_premium_api', params=params, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return response.json().get("message", "Server is facing some issues. Please try again later.")


def premium_chat(*args, **kwargs):
    # try 3 times to call try_to_get_response(*args, **kwargs) function and if it fails then return error message
    for i in range(3):
        try:
            return try_to_get_response(*args, **kwargs)
        except Exception as e:
            pass
    return "Server is facing some issues. Please try again later."
    # try:
    #     try_to_get_response(*args, **kwargs)
    # except Exception as e:
    #     return f"An error occurred while performing premium_chat, connect with developer. Error: {e}"


if __name__ == "__main__":
    print(premium_chat(query="who is naredra modi", api_key='ae44cc6e-0d5c-45c1-b8a3-fe412469510f'))
