import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from cb_RF1 import get_course
from wiki import get_article


vk_session = vk_api.VkApi(token="vk1.a.5FBE1ZZYl-KMv7EOdMX3gZJIMjU0Jukc3q8ju5jLeeiJAxXKRQ4iaHfqcMucIu4HIAzzGu9WhkwrFUMoCdxP6ZsdDwkPaTpYqdwt5no81ctWK3ZuOg9ytO9a1oeom0Mg0NlOR-q6cabjzUm0_u1qAQptryrkZhDPM2hpJEw5NcXD0dwzHsRTuSYhWbKsz43eE7TLmRW6lrrB46nu5fbKjA")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        if user_message[0:2] == '-к':
            response = "Курс доллара {0} руб. за 1 шт.\nКурс евро {1} руб. за 1 шт.\nКурс юаня {2} руб. за 1 шт.".format(
                get_course("R01235"), get_course("R01239"), get_course("R01375")
            )
        elif user_message[0:2] == '-в':
            article = user_message[2:]
            response = f'Вот, что я нашел:\n\n{get_article(article)}'
        else:
            response = "Не знаю такой команды."
        vk.messages.send(user_id=event.user_id, message=response, random_id=random.randint(-10 ** 7, 10 ** 7))