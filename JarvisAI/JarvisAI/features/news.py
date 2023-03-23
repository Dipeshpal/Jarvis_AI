import webbrowser


def news(*args, **kwargs):
    """
    This method will open the browser and show the news "https://thetechport.in/"
    :return: list / bool
    """
    try:
        url = "https://thetechport.in/"
        webbrowser.open(url)
        return True
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
        url = "https://www.youtube.com/c/TechPortOfficial"
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    print(news())
    print(show_me_some_tech_news())
