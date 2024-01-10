from r3c0n.model.plugin import Plugin
from ..model.outcome import Outcome
from ..model.enum.message import Message
from ..utils.log_utils import *
from ..utils.io_utils import writeFile
from ..utils.system import *

COMMAND = "dirsearch -u {}"
FILE_NAME = "6_dirsearch" 

class DirSearch(Plugin):
    
    def getCommand(self, context: Outcome):    
        return COMMAND.format(context.url, '80')
        
        
    def execute(self, context: Outcome):
        cmd = self.getCommand(context)
        result = execute(cmd)
        writeFile(FILE_NAME, result, context.workspace)
    
    
    def preExec(self, context: Outcome):
        cmd = self.getCommand(context)
        log(Message.DIRSEARCH_START, cmd, '80')
        
        
    def postExec(self, context: Outcome):
        log(Message.TODO)
        newLine()