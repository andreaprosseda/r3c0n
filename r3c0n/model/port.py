class Port:
    
    def __init__(self, lineValue):
        self.value = lineValue
        self.isValid = isValid(lineValue)
        
        values = getValues(lineValue)
        self.number = getNumber(values)
        self.state = getState(values)
        self.service = getService(values)
        self.version = getVersion(values)


    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value


def getValues(lineValue):
    values = []
    tempValues = lineValue.split(" ")
    for value in tempValues:
        value = value.strip()
        if value != '':
            values.append(value)
    return values
    
    
def getNumber(values):
    return values[0].split("/")[0]

 
def getState(values):
    return values[1].strip()


def getService(values):
    return values[2].strip()


def getVersion(values):
    if (len(values)>3):
        return values[3].strip()
    return None


def isValid(value):
    return value.strip() != ''