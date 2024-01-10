from .ping import Ping
from .nmap import Nmap
from .nmap_version import Nmap_Version
from .nmap_allports import Nmap_AllPorts
from .nmap_allports_version import Nmap_AllPorts_Version
from .nmap_udp import Nmap_Udp
from .dir_search import DirSearch

def allPlugins():
    return [
        Ping(), 
        Nmap(), 
        Nmap_Version(),
        Nmap_AllPorts(),
        Nmap_AllPorts_Version(),
        Nmap_Udp()#,
        #DirSearch()
    ]