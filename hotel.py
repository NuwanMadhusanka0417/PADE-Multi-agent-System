
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
import json

class hotel(Agent):
    def __init__(self, aid):
        super(hotel, self).__init__(aid=aid, debug=False)

    def get_hotel_data(self,coutry_name):
        data = {
            "america": ["apache","Sam","fortune","atlanta","bellagio"],
            "japan": ["osaka","shinjuku","ueno","santiago"],
            "canada": ["bonaventure","fairmont","ritz","niagara"]
        }
        return data["%s"%(coutry_name)]

    def react(self, message):
        super(hotel, self).react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name.split('@')))
        #display_message(self.aid.localname,message.content)
        sender_name = message.sender.name.split('@')[0]
        if sender_name == "country":
            cnty_data = message.content
            print(type(cnty_data))

            data = json.loads(str(cnty_data))
            data= data.items()
            cnty_name = None
            cnty_val = None
            for key,val in data:
                cnty_name = key
                cnty_val=val
            # print(cntr_name)
            #if****
            #print("data in hotel", cnty_name)
            data = self.get_hotel_data(cnty_name)
            new_json = {
                "country":cnty_name,
                "time":cnty_val,
                "hotels":data
            }
            #print(new_json)

            # display_message(self.aid.localname,'message is {}'.format(message.content))
            # print(data)
            self.sending_message(new_json)
    def sending_message(self,content):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('agency'))
        message.set_content(content)
        self.send(message)





