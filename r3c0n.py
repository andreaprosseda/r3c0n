from r3c0n.model.plugin import Plugin
from r3c0n.plugins.all import allPlugins
from r3c0n.utils.args_checker import getArgs
from r3c0n.utils.ascii_art import showAsciiArt
from r3c0n.utils.io_utils import createWorkspace, getContinueOrExitAnswer
from r3c0n.utils.system import isRoot
from r3c0n.utils.log_utils import *

showAsciiArt()

context = getArgs()
context.workspace = createWorkspace(context.target_name)

if not isRoot():
    log(Message.NO_ROOT_PRIVILEGES)
    getContinueOrExitAnswer()

plugins: [Plugin] = allPlugins()
for plugin in plugins:
    plugin.preExec(context)
    plugin.execute(context)
    plugin.postExec(context)