try:
    from features.date_time import date_time
    from features.joke import joke
    from features.news import news
    from features.tell_me_about import tell_me_about
    from features.weather import weather
    from features.website_open import website_open
    from features.youtube_play import youtube_play
    from features.whatsapp_message import whatsapp_message
    from features.send_email import send_email
    from features.chatbot import chatbot
    from features.chatbot import greet
    from features.chatbot import goodbye
    from features.screenshot import screenshot
    from features.click_photo import click_photo
    # from features.internet_speed_test import internet_speed_test
    from features.youtube_video_downloader import youtube_video_downloader
    from features.covid_cases import covid_cases
    from features.games import games
    from features.places_near_me import places_near_me
    from features.iambored import iambored
    from features.volume_control import volume_controller
except ImportError as e:
    # print("ImportError: {}".format(e))
    from .features.date_time import date_time
    from .features.joke import joke
    from .features.news import news
    from .features.tell_me_about import tell_me_about
    from .features.weather import weather
    from .features.website_open import website_open
    from .features.youtube_play import youtube_play
    from .features.whatsapp_message import whatsapp_message
    from .features.send_email import send_email
    from .features.chatbot import chatbot
    from .features.chatbot import greet
    from .features.chatbot import goodbye
    from .features.screenshot import screenshot
    from .features.click_photo import click_photo
    # from .features.internet_speed_test import internet_speed_test
    from .features.youtube_video_downloader import youtube_video_downloader
    from .features.covid_cases import covid_cases
    from .features.games import games
    from .features.places_near_me import places_near_me
    from .features.iambored import iambored
    from .features.volume_control import volume_controller


dict_of_features = {
    'asking date': date_time.date,
    'asking time': date_time.time,
    'tell me joke': joke.tell_me_joke,
    'tell me news': news.news,
    'asking weather': weather.get_weather,
    'tell me about': tell_me_about.tell_me_about,
    'open website': website_open.website_opener,
    'play on youtube': youtube_play.yt_play,
    'send whatsapp message': whatsapp_message.send_whatsapp_message,
    'send email': send_email.send_email,
    'greet': greet.greet,
    'goodbye': goodbye.goodbye,
    # 'conversation': chatbot.chatbot_general_purpose,
    'take screenshot': screenshot.take_screenshot,
    'click photo': click_photo.click_pic,
    # 'check internet speed': internet_speed_test.speed_test,
    'download youtube video': youtube_video_downloader.download_yt_video,
    'covid cases': covid_cases.check_command_is_for_covid_cases,  #
    'play games': games.play_games,
    'places near me': places_near_me.get_places_near_me,
    'i am bored': iambored.get_me_suggestion,
    'volume control': volume_controller.start_volume_control,
}

what_can_i_do = {
    'you can ask me date ': 'Say- "what is the date today"',
    'you can ask me time ': 'Say- "what is the time now"',
    'you can ask me joke ': 'Say- "tell me a joke"',
    'you can ask me news ': 'Say- "tell me news"',
    'you can ask me weather ': 'Say- "what is the weather", "tell me weather", "tell me about weather",'
                               ' "what is the weather in <city>"',
    'you can ask me about ': 'Say- "tell me about <topic>"',
    'you can open website ': 'Say- "open websiteopen website <website name>", "open website <website name><.extension>"'
                             '"open website techport.in"',
    'you can play on youtube ': 'Say- "play on youtube <video name>", "play <video name> on youtube"',
    'you can send whatsapp message ': 'Say- "send whatsapp message',
    'you can send email ': 'Say- "send email',
    'greet': 'Say- "greet", "hello", "hey", "hi", "good morning", "good afternoon", "good evening"',
    'goodbye': 'Say- "goodbye", "bye", "see you later"',
    # 'conversation': 'Say- "conversation", "chat", "talk", "talk with chatbot"',
    'you can take a screenshot of current screen': 'Say- "take screenshot"',
    'you can click a photo': 'Say- "click photo"',
    # 'you can check internet speed': 'Say- "check internet speed"',
    'you can download youtube video': 'Say- "download youtube video"',
    'you can check covid cases': 'Say- "covid cases in <country>", "covid cases <country>"',
    'you can ask to play games': 'Say- "play games"',
    'you can ask places near me': 'Say- "cafe near me"',
    'you can ask to suggest something': 'Say- "i am bored"',
    'you can control volume': 'Say- "open volume control"'
}

if __name__ == '__main__':
    print(', '.join(list(dict_of_features.keys())))
