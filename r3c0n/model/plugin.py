from ..model.outcome import Outcome

class Plugin:
    
    def getCommand(self, context: Outcome):
        name = type(self).__name__
        raise NotImplementedError("[{}] Method getCommand() not implemented yet".format(name))
    
    def execute(self, context: Outcome):
        name = type(self).__name__
        raise NotImplementedError("[{}] Method run() not implemented yet".format(name))
    
    def preExec(self, context: Outcome):
        name = type(self).__name__
        raise NotImplementedError("[{}] Method preExec() not implemented yet".format(name))

    def postExec(self, context: Outcome):
        name = type(self).__name__
        raise NotImplementedError("[{}] Method postExec() not implemented yet".format(name))