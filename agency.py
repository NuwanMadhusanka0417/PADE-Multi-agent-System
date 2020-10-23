from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID


class agency(Agent):
    def __init__(self, aid):
        super(agency, self).__init__(aid=aid, debug=False)
        # self.sending_message()
    #     self.check()
    #     # call_later(1.0, self.sending_message)
    # def check(self):
    #
    #
    #     self.sending_message('america')
    #     # call_later(1.0, self.sending_message,"america")
    def on_start(self):
        super(agency, self).on_start()
        display_message(self.aid.localname, 'sending Message...')
        call_later(8.0, self.sending_message)

    def sending_message(self):
        fl = open("data/name.txt")
        var = fl.read()
        var = var.strip()
        print(type(var))
        message = ACLMessage(ACLMessage.INFORM)
        message.add_receiver(AID('country'))
        message.set_content(var)
        self.send(message)


    def react(self, message):
        super(agency, self).react(message)
        display_message(self.aid.localname, 'Mensagem received from {}'.format(message.sender.name.split('@')))
        #display_message(self.aid.localname, 'message is {}'.format(message.content))
        if (message.sender.name.split('@')[0]=="hotel"):
            print("Data from hotel = ",message.content)



