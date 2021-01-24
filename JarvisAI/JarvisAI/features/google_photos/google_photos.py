import webbrowser


def google_photos():
    try:
        url = "https://photos.google.com/"
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False
