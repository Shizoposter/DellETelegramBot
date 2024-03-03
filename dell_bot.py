import telebot
import requests
import openai
import time
token = 'your token'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types='text')
@bot.callback_query_handler(func=lambda call: True)
def message_reply(message):
    if '/start' in message.text and message.text.count('/') == 1:
        bot.send_message(message.chat.id, 'Здравствуй. Данный бот позволяет выполнять запросы к онлайн-нейросети Dell-E и с помощью них генерировать картинки по заданному описанию')
        time.sleep(2)
        bot.send_message(message.chat.id, 'Для создания запроса отправьте отдельное сообщение, соответсвующее структуре «/dell описание фото» без кавычек.')
    if '/dell' in message.text and message.text.count('/') == 1:
            if len(message.text.split()) > 1 and message.text.split()[::-1][0] != '/dell':
                dell_request_name = ' '.join(message.text.split()[message.text.split().index('/dell')+1:])
                #print(dell_request_name)
                API_KEY = "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"
                prompt = dell_request_name
                url = f"https://api.openai.com/v1/images/generations"
                data = {
                    "model": "image-alpha-001",
                    "prompt": prompt,
                    "num_images": 1,
                    "size": "256x256",
                    "response_format": "url"
                }

                headers = {
                    "Authorization": f"Bearer {API_KEY}"
                }
                openai.api_key = API_KEY
                response = openai.Image.create(
                    prompt=dell_request_name,
                    n=1,
                    size="1024x1024")
                image_url = response['data'][0]['url']
                bot.send_photo(message.chat.id, image_url)
            else:
                bot.send_message('Запрос введен некорректно.')

        
bot.infinity_polling()