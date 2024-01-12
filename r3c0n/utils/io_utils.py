import os
import shutil

from .config import *
from .log_utils import *
from r3c0n.model.enum.message import Message

def createWorkspace(name):
    wkPath = getWorkspace(name)
    log(Message.WK_CREATE,wkPath) 
    if os.path.exists(wkPath):
        log(Message.WK_EXISTS, wkPath)
        shutil.rmtree(wkPath, ignore_errors=True)
        
    os.mkdir(wkPath)
    log(Message.WK_CREATED, wkPath)
    newLine()
    return wkPath


def writeFile(file, content, workspace):
    file_path = getFilePath(workspace, file)
    f = open(file_path, "w")
    f.write(content)
    f.close()
    log(Message.FILE_SAVED, file_path)


def getWorkspace(name):
    desktop = getBaseFolder()
    workspace = getFilePath(desktop, name)
    return workspace


def getFilePath(workspace, fileName):
    return workspace+"/"+fileName