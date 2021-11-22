from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import webbrowser


def news():
    """
    This method will tells top 15 current NEWS
    :return: list / bool
    """
    try:
        news_url = "https://news.google.com/news/rss"
        Client = urlopen(news_url)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")
        news_list = soup_page.findAll("item")
        li = []
        for news in news_list[:15]:
            li.append(str(news.title.text.encode('utf-8'))[1:])
        return li
    except Exception as e:
        print(e)
        return False


def show_me_some_tech_news():
    try:
        url = "https://thetechport.in/"
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False


def show_me_some_tech_videos():
    try:
        url = "https://www.youtube.com/channel/UCGEoRAK92fUk2kY3kSJMR_Q"
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False
