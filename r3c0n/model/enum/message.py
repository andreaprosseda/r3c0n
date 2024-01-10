from enum import Enum
from .status import Status
  
class Message(Enum):
    
    COMMAND_ERROR               = {'status': Status.ERROR,   'text': 'Error executing command [{}]'}
    WK_CREATE                   = {'status': Status.IO,      'text': '[WORKSPACE] Creating workspace {}...'}
    WK_EXISTS                   = {'status': Status.ERROR,   'text': '[WORKSPACE] Workspace already exists! Removing...'}
    WK_CREATED                  = {'status': Status.IO,      'text': '[WORKSPACE] Workspace {} created!'}
    FILE_SAVED                  = {'status': Status.IO,      'text': '[WORKSPACE] File saved in workspace {}'}
    ROOT_PRIVILEGES_REQUIRED    = {'status': Status.WARNING, 'text': '[ROOT] Root privileges are required for this command [{}], skipping...'}
    
    PING_START                  = {'status': Status.INFO,    'text': '[PING] Ping {}, please wait...'}
    PING_OK                     = {'status': Status.SUCCESS, 'text': '[PING] {} is up and running!'}
    PING_KO                     = {'status': Status.ERROR,   'text': '[PING] {} unreachable!'}
    
    NMAP_LITE_START             = {'status': Status.INFO,    'text': '[NMAP_1/5] Looking for open ports [{}], please wait...'}
    NMAP_VERSION_START          = {'status': Status.INFO,    'text': '[NMAP_2/5] Looking for service versions [{}], please wait...'}
    NMAP_ALL_PORTS_START        = {'status': Status.INFO,    'text': '[NMAP_3/5] Looking for all open ports [{}], please wait...'}
    NMAP_FULL_OPEN_PORTS_START  = {'status': Status.INFO,    'text': '[NMAP_4/5] Looking for info on all open ports [{}], please wait...'}
    NMAP_UDP_START              = {'status': Status.INFO,    'text': '[NMAP_5/5] Looking for UDP ports [{}], please wait...'}
    
    DIRSEARCH_START             = {'status': Status.INFO,    'text': '[DIRSEARCH] Port {} is open, looking for directories [{}], please wait...'}
    
    PORTS_OPEN_ONLY             = {'status': Status.SUCCESS, 'text': 'Open Ports:\n{}'}
    PORTS                       = {'status': Status.SUCCESS, 'text': 'Open Ports:\n{}\n\nFiltered Ports:\n{}'}
    
    
    TODO                        = {'status': Status.ERROR, 'text': 'Not implemented yet'}