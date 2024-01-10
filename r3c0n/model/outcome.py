from .port import Port

class Outcome:
    
    def __init__(self, target_name, target_url):
        self.url = target_url
        self.target_name = target_name
        self.isReachable = False
        self.workspace = None
        self.tcp_open_ports = []
        self.tcp_filtered_ports = []
        self.udp_open_ports = []
        self.udp_filtered_ports = []


    def getOpenPortsNumber(self):
        return [port.number for port in self.tcp_open_ports]
            
    def setTcpOpenPorts(self, ports: [str]):
        self.tcp_open_ports = getPortFromList(ports)
    

    def setTcpFilteredPorts(self, ports: [str]):
        self.tcp_filtered_ports = getPortFromList(ports)

    
    def setUdpOpenPorts(self, ports: [str]):
        self.udp_open_ports = getPortFromList(ports)

    
    def setUdpFilteredPorts(self, ports: [str]):
        self.udp_filtered_ports = getPortFromList(ports)


def getPortFromList(ports: [str]):
    result = []
    if ports is None:
        return result
    
    for portString in ports:
        port = Port(portString)
        if port:
            result.append(port)
    
    return result
            

def getPort(portString: str):
    if portString is None:
        return None
    
    port = Port(portString)
    if port.isValid():
        return port
    
    return None