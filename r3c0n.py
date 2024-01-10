from r3c0n.model.plugin import Plugin
from r3c0n.plugins.all import allPlugins
from r3c0n.utils.ascii_art import showAsciiArt
from r3c0n.utils.args_checker import getArgs
from r3c0n.utils.io_utils import createWorkspace

showAsciiArt()

context = getArgs()
context.workspace = createWorkspace(context.target_name)

plugins: [Plugin] = allPlugins()
for plugin in plugins:
    plugin.preExec(context)
    plugin.execute(context)
    plugin.postExec(context)