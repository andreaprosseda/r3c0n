from r3c0n.model.plugin import Plugin
from ..model.outcome import Outcome
from ..model.enum.message import Message
from ..utils.log_utils import *
from ..utils.nmap_utils import *
from ..utils.system import execute, isRoot
from ..utils.io_utils import writeFile

COMMAND = "nmap -F -sU -sV {}"
FILE_NAME = "5_nmap+udp"

class Nmap_Udp(Plugin):
    
    def getCommand(self, context: Outcome):    
        return COMMAND.format(context.url)
        
    
    def execute(self, context: Outcome):            
        cmd = self.getCommand(context)
        
        if not isRoot():
            log(Message.ROOT_PRIVILEGES_REQUIRED, cmd)
            return
        
        result = execute(cmd)
        writeFile(FILE_NAME, result, context.workspace)
        context.setUdpOpenPorts(getUdpOpen(result))
        context.setUdpFilteredPorts(getUdpFiltered(result))


    def preExec(self, context: Outcome):
        cmd = self.getCommand(context)
        log(Message.NMAP_UDP_START, cmd)

        
    def postExec(self, context: Outcome):
        if isRoot():
            logPorts(context.udp_open_ports, context.udp_filtered_ports)
        newLine()
