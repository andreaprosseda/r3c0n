from .log_utils import log
from ..model.enum.message import Message

import os
import subprocess

def execute(command):
    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.DEVNULL)
        return result
    except:
        log(Message.COMMAND_ERROR, command)
        exit()
    
def run(command):
    try:
        result = subprocess.run(command.split(" "), capture_output=True)
        return result
    except:
        log(Message.COMMAND_ERROR, command)
        exit()
        
def isRoot():
    return os.geteuid() == 0
