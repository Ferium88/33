import vk_api
import random
from cb_RF import get_dollar_course

vk = vk_api.VkApi(token="vk1.a.5FBE1ZZYl-KMv7EOdMX3gZJIMjU0Jukc3q8ju5jLeeiJAxXKRQ4iaHfqcMucIu4HIAzzGu9WhkwrFUMoCdxP6ZsdDwkPaTpYqdwt5no81ctWK3ZuOg9ytO9a1oeom0Mg0NlOR-q6cabjzUm0_u1qAQptryrkZhDPM2hpJEw5NcXD0dwzHsRTuSYhWbKsz43eE7TLmRW6lrrB46nu5fbKjA")


while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >= 1:
        msg_text = messages['items'][0]['last_message']['text']

        if msg_text.lower() == "курс":
            ans = f"Курс доллара на сегодня составляет {get_dollar_course()} руб."
        else:
            ans = "Неизвестная команда"

        user_id = messages['items'][0]['last_message']['from_id']
        vk.method(
            "messages.send",
            {
                'random_id': random.randint(-10 ** 7, 10 ** 7),
                'user_id': user_id,
                'message': ans
            }
        )
