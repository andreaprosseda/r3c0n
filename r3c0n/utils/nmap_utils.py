
def getTcpOpen(file):
    return find(file, "/tcp", "open")


def getTcpFiltered(file):
    return find(file, "/tcp", "filtered")


def getUdpOpen(file):
    return find(file, "/udp", "open")


def getUdpFiltered(file):
    return find(file, "/udp", "filtered")


def find(file, protocol, state):
    result = []
    lines = file.split("\n")

    for line in lines:
        line = line.strip()
        if line != '' and protocol in line and state in line:
            result.append(line)

    return result