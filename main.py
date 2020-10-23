from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from agency import agency
from country import country
from hotel import hotel
if __name__ == '__main__':

    agents = list()
    # port = int(argv[1])
    port = 4004
    receiver_agent = agency(AID(name='agency@localhost:{}'.format(port)))
    agents.append(receiver_agent)

    port += 1
    sender_agent = country(AID(name='country@localhost:{}'.format(port)))
    agents.append(sender_agent)

    port += 1
    sender_agent = hotel(AID(name='hotel@localhost:{}'.format(port)))
    agents.append(sender_agent)

    start_loop(agents)