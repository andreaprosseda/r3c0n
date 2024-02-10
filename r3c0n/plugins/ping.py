from ..model.plugin import Plugin
from ..model.outcome import Outcome
from ..model.enum.message import Message
from ..utils.io_utils import getContinueOrExitAnswer
from ..utils.log_utils import *
from ..utils.system import run

COMMAND = "ping -c 1 {}"

class Ping(Plugin):
    
    def getCommand(self, context: Outcome):    
        return COMMAND.format(context.url)
        
        
    def execute(self, context: Outcome):
        cmd = self.getCommand(context)
        result = run(cmd)
        context.isReachable = result.returncode == 0
    
    
    def preExec(self, context: Outcome):
        log(Message.PING_START, context.url)
    
        
    def postExec(self, context: Outcome):
        if context.isReachable:
            log(Message.PING_OK, context.url)
        else:
            log(Message.PING_KO, context.url)
            getContinueOrExitAnswer()
        newLine()