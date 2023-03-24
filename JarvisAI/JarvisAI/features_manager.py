try:
    from features.date_time import date_time
    from features.greet import greet, goodbye
    from features.joke import tell_me_joke
    from features.click_photo import click_pic
    from features.covid_cases import check_command_is_for_covid_cases
    from features.games import play_games
    from features.iambored import get_me_suggestion
    from features.internet_speed_test import speed_test
    from features.news import news
    from features.places_near_me import get_places_near_me
    from features.screenshot import take_screenshot
    from features.send_email import send_email
    from features.tell_me_about import tell_me_about
    from features.volume_controller import start_volume_control
    from features.weather import get_weather
    from features.website_open import website_opener
    from features.whatsapp_message import send_whatsapp_message
    from features.youtube_play import yt_play
    from features.youtube_video_downloader import download_yt_video
    from brain import chatbot_premium
except Exception as e:
    from .features.date_time import date_time
    from .features.greet import greet, goodbye
    from .features.joke import tell_me_joke
    from .features.click_photo import click_pic
    from .features.covid_cases import check_command_is_for_covid_cases
    from .features.games import play_games
    from .features.iambored import get_me_suggestion
    from .features.internet_speed_test import speed_test
    from .features.news import news
    from .features.places_near_me import get_places_near_me
    from .features.screenshot import take_screenshot
    from .features.send_email import send_email
    from .features.tell_me_about import tell_me_about
    from .features.volume_controller import start_volume_control
    from .features.weather import get_weather
    from .features.website_open import website_opener
    from .features.whatsapp_message import send_whatsapp_message
    from .features.youtube_play import yt_play
    from .features.youtube_video_downloader import download_yt_video
    from .brain import chatbot_premium


def show_what_can_i_do(*args, **kwargs):
    print("I can do following things:")
    for key in action_map.keys():
        print(key)


action_map = {
    "asking time": date_time,
    "asking date": date_time,
    "greet and hello hi kind of things": greet,
    "goodbye": goodbye,
    "tell me joke": tell_me_joke,
    "tell me about": tell_me_about,  # TODO: improve this
    "i am bored": get_me_suggestion,
    "volume control": start_volume_control,
    "tell me news": news,
    "click photo": click_pic,
    "places near me": get_places_near_me,
    "play on youtube": yt_play,
    "play games": play_games,
    "what can you do": show_what_can_i_do,
    "send email": send_email,
    "download youtube video": download_yt_video,
    "asking weather": get_weather,
    "take screenshot": take_screenshot,
    "open website": website_opener,
    "send whatsapp message": send_whatsapp_message,
    "covid cases": check_command_is_for_covid_cases,
    "check internet speed": speed_test,
    "others": chatbot_premium.premium_chat,
}
