
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

class country(Agent):
    def __init__(self, aid):
        super(country, self).__init__(aid=aid, debug=False)

    def get_coutry_data(self,coutry_name):
        data = {
            "america": [5.20,7.25],
            "japan": [5.96,9.25],
            "caneda": [8.45,9.25],
        }
        print("country name is : ",coutry_name)
        x = data["%s"%(coutry_name)]
        return x


    def react(self, message):
        super(country, self).react(message)
        display_message(self.aid.localname, 'Message received from {}'.format(message.sender.name.split('@')))
        sender_name = message.sender.name.split('@')[0]
        if sender_name == "agency":
            data = self.get_coutry_data(message.content)
            json = "{\""+message.content+"\":"+str(data)+"}"
            display_message(self.aid.localname,'message is {}'.format(message.content))
            print("json in coutry : ",json)
            self.sending_message(json)
    def sending_message(self,content):
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('hotel'))
        message.set_content(content)
        self.send(message)





