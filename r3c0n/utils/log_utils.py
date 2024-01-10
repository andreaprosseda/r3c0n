from termcolor import colored
from ..model.enum.message import Message

def newLine():
    print()
    
    
def log(message, *args):
    msg = message.value['text'].format(*args)
    color = message.value['status'].value
    print(colored(msg, color))
    
    
def logPorts(open, filtered):
    open = "\n".join(str(port) for port in open)
    filtered = "\n".join(str(port) for port in filtered)
    message = Message.PORTS if filtered == '\n' else Message.PORTS_OPEN_ONLY
    log(message, open, filtered)