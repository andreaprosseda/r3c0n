import configparser


def getBaseFolder():
    config = getConfig()
    return config.get('misc', 'base_folder')


def getConfig():
    configPath = 'config.ini'
    config = configparser.ConfigParser()
    config.read(configPath)
    return config