import webbrowser


def play_games(inp_command):
    url = 'https://poki.com/'
    try:
        webbrowser.open(url)
        return "Successfully opened Poki.com, Play your games!"
    except Exception as e:
        print(e)
        return "Failed to open Poki.com, please try again!"


if __name__ == '__main__':
    play_games('inp_command')
