<h1>PyChatbotLib</h1>
<hr/>
<b>Exclusive library for creating chatbots.<br>
It uses a very simple algorithm which helps to recognize possible answers to messages.<br>
You just need to train it in chats with 2 types of messages: reply and original.<br>
</b>
<h3>Installation</h3>

```pip install pychatbotlib```
<h3>Example of usage</h3>

```python
import telebot # pip3 install PyTelegramBotAPI==2.2.3
from time import sleep
from pychatbotlib.pychatbotlib import Chatbot
bot = telebot.TeleBot('APIKEY')
chatbot = Chatbot("chatbot_data")

@bot.message_handler(content_types=["text"])
def handle_message(message):
    try:
        chatbot.add_data(message.text, message.reply_to_message.text)
        answer = chatbot.get_reply(message.text)
        if answer is not None:
            bot.reply_to(message, answer)
    except Exception as e:
        answer = chatbot.get_reply(message.text)
        if answer is not None:
            bot.reply_to(message, answer)
        print("Not a reply")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        bot.polling(none_stop=True)
  
  ```
