import os
import requests
from pymessenger.bot import Bot


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAFHtRQRdEsBAEaUuxMtcKeZBOIdSpFHG7G7XijgjtNZAuKxUac48LmxJz4wMfCv7L76FZBmIUOh5YS5q0ohPqq1wQUcAi7r3oiB1ZCn9fbrmMkbeaeKayFb6uRZAZAumzFZCqT80ZA0TA1IxOb1Pk9zc4cjJDB4V4ZC5mjimAVksVuIALxlP9YDE"

bot = Bot(ACCESS_TOKEN)


#chooses a random message to send to the user


#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_imgurl(recipient_id, url):
    print(url)
    bot.send_image_url(recipient_id, url)
    return "success"

def send_img(recipient_id, path):
    bot.send_image(recipient_id, path)
    return "success"

def send_fileurl(recipient_id, url):
    print(url)
    bot.send_file_url(recipient_id, url)
    return "success"

def send_vid(recipient_id, url):
    print(url)
    current_path = os.path.abspath("test.mp4")
    print(current_path)
    bot.send_video(recipient_id, current_path)
    return "success"


