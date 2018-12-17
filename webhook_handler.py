#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from bottle import static_file
from fsm import TocMachine
import os
from send_msg import send_message

webhook_handler = Flask(__name__)
ACCESS_TOKEN = 'EAAFHtRQRdEsBALpCb6If7X2tKwZAR4b10GtnDaye6XXII6LypemuznzgvxasD3fvSeZA6x0fJ0YDqMSSSgaCcH037hawprNUWlSKvtKv49SurV6vMweXvaoYE3Iyw1cOrktKmzFurSvZAxlux2MK1WNVIyqwruVNSWLCjA8bwZDZD'
VERIFY_TOKEN = 'Rmp4951344'


#initial fsm
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'go_back_to_state2',
            'source': [
                'state3',
                'state4',
                'state5'
            ],
            'dest': 'state2',
            'conditions': 'back_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state1',
            'conditions': 'back_to_state2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)
#end fsm

#We will receive messages that Facebook sends our bot at this endpoint 
@webhook_handler.route("/webhook", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       print(output)
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    text = message['message']['text']
                    machine.advance(message)
                    #if text == 'image':
                        #http = os.path.abspath('google.png')
                        #http = 'https://hant.helplib.com/images/logo.png'
                        #http = text
                    #send_imgurl(recipient_id, text)
                    #send_vid(recipient_id, 'Bastille - Pompeii (Official Music Video).mp4')
                    #send_message(recipient_id, '哈哈哈')
                    '''
                    else:
                        machine.advance(text)
                        response_sent_text = 'state + ' +  machine.state
                        send_message(recipient_id, response_sent_text)
                    
                    
                    if text == "damn":
                        send_message(recipient_id, "Everything will be ok!")
                    else:
                        response_sent_text = get_message()
                        print(response_sent_text)
                        send_message(recipient_id, response_sent_text)
                    '''
                #if user sends us a GIF, photo,video, or any other non-text item
                #if message['message'].get('attachments'):
                    #response_sent_nontext = get_message()
                    #send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

'''
@webhook_handler.route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    print('hihihi')
    return static_file('fsm.png', root='./', mimetype='image/png')
'''
'''
#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

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
'''

if __name__ == "__main__":
    webhook_handler.run(host='0.0.0.0', debug=True)