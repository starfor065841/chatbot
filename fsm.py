from transitions.extensions import GraphMachine
from send_msg import send_message, send_imgurl
from pchome import search, firstPage
from min_price import min_sort
import time

items = []
prices = []
urls = []
img_urls = []
min_target = []
describe = []
searchTarget = ''
state2_flag = False


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == '開始使用'
        return False

    def is_going_to_state2(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            print(text)
        return True

    def back_to_state1(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == '重新搜尋'
        return False

    
    def back_to_state2(self, event):
        global state2_flag
        state2_flag = True
        print('flaggggggggggggggggggggg' + str(state2_flag))
        return True
    
    def is_going_to_state3(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == '最便宜'
        return False

    def is_going_to_state4(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == '預覽'
        return False

    def is_going_to_state5(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == '列表'
        return False

    def is_going_to_state6(self, event):
        if event['message'].get('text'):
            text = event['message']['text']
            return text == 'Demo'
        return False       

    def on_enter_state1(self, event):
        print("I'm entering state1")

        global state2_flag
        global prices
        global items
        global urls
        global img_urls
        global describe
        state2_flag = False
        prices = []
        items = []
        urls = []
        img_urls = []
        describe = []

        sender_id = event['sender']['id']
        send_message(sender_id, "請輸入商品名稱")
        #self.go_back()

    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")
        
        #print(event['message']['text'])
        #send_message(sender_id, event['message']['text'])
        global prices
        global items
        global urls
        global img_urls
        global describe

        #print(items)
        #print(prices)
        #print(urls)
        #for item in items:
        global state2_flag
        global searchTarget
        print('flaggggggggggggggggggggg' + str(state2_flag))
        if state2_flag == False:
            sender_id = event['sender']['id']
            searchTarget = event['message']['text']
            items, prices, urls, img_urls, describe = search(event['message']['text'])
            print('ffffffffffffffffffffff' + str(state2_flag))
            l = len(items)
            s = '共' + str(l) + '項商品'
            send_message(sender_id, s)
            #time.sleep(2)


        #self.go_back_to_state2()
       

    def on_exit_state2(self, event):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        global prices
        global items
        global urls
        global describe
        global min_target

        print(prices)
        min_target = min_sort(prices)
        print(min_target)
        sender_id = event['sender']['id']
        for every in min_target:
            send_message(sender_id, items[every])
            send_message(sender_id, prices[every])
            send_message(sender_id, urls[every])
            send_message(sender_id, describe[every])
        self.go_back_to_state2('back state2')

    def on_exit_state3(self, event):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")
        
        global min_target
        global img_urls

        sender_id = event['sender']['id']
        if min_target != []:
            for every in min_target:
                send_imgurl(sender_id, img_urls[every])
        else:
            send_message(sender_id, '不好意思 目前尚未建立商品列表')
            send_message(sender_id, '請先輸入欲搜尋商品')
            
        self.go_back_to_state2('back state2')


    def on_exit_state4(self, event):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        global searchTarget
        
        sender_id = event['sender']['id']
        url = firstPage(searchTarget)
        send_message(sender_id, url)
            
        self.go_back_to_state2('back state2')


    def on_exit_state5(self, event):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        global searchTarget
        
        sender_id = event['sender']['id']
        url = firstPage(searchTarget)
        send_message(sender_id, 'Demo')
            
        self.go_back_to_state2('back state2')


    def on_exit_state6(self, event):
        print('Leaving state6')


'''
if __name__ == "__main__":
    while True:
        text = input('input: ')
        print('---')
        print('LAST STATE: ' + machine.state)

        machine.advance(text)
        #machine.advance('go to state2')
        #machine.advance('go to state1')
        #machine.state1
        print('FINAL STATE: ' + machine.state)
        print('---')
'''