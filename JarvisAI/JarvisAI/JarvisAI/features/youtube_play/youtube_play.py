import pywhatkit as kit


def yt_play(inp_command, *arg, **kwargs):
    kit.playonyt(inp_command)
    return "Playing Video on Youtube"


if __name__ == "__main__":
    yt_play('play on youtube shape of you')
