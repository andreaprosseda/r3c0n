from r3c0n.model.plugin import Plugin
from ..model.outcome import Outcome
from ..model.enum.message import Message
from ..utils.log_utils import *
from ..utils.nmap_utils import *
from ..utils.system import execute
from ..utils.io_utils import writeFile

COMMAND = "nmap {}"
FILE_NAME = "1_nmap"

class Nmap(Plugin):    
    
    def getCommand(self, context: Outcome):    
        return COMMAND.format(context.url)
        
        
    def execute(self, context: Outcome):
        cmd = self.getCommand(context)
        result = execute(cmd)
        writeFile(FILE_NAME, result, context.workspace)
        context.setTcpOpenPorts(getTcpOpen(result))
        context.setTcpFilteredPorts(getTcpFiltered(result))
        
        
    def preExec(self, context: Outcome):
        cmd = self.getCommand(context)
        log(Message.NMAP_LITE_START, cmd)
        
        
    def postExec(self, context: Outcome):
        logPorts(context.tcp_open_ports, context.tcp_filtered_ports)
        newLine()