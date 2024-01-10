from r3c0n.model.plugin import Plugin
from ..model.outcome import Outcome
from ..model.enum.message import Message
from ..utils.log_utils import *
from ..utils.nmap_utils import *
from ..utils.system import execute
from ..utils.io_utils import writeFile

COMMAND = "nmap -sC -sV -A -p '{}' {}"
FILE_NAME ="4_nmap+all_ports+version"

class Nmap_AllPorts_Version(Plugin):
    
    def getCommand(self, context: Outcome):    
        openPorts = context.getOpenPortsNumber()
        portString = ", ".join(map(str, openPorts))
        return COMMAND.format(portString, context.url)
        
    
    def execute(self, context: Outcome):
        cmd = self.getCommand(context)
        result = execute(cmd)
        writeFile(FILE_NAME, result, context.workspace)
        context.setTcpOpenPorts(getTcpOpen(result))

    
    def preExec(self, context: Outcome):
        cmd = self.getCommand(context)
        log(Message.NMAP_FULL_OPEN_PORTS_START, cmd)

        
    def postExec(self, context: Outcome):
        logPorts(context.tcp_open_ports, context.tcp_filtered_ports)
        newLine()