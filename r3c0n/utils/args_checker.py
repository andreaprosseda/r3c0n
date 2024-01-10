from ..model.outcome import Outcome

import argparse

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", dest="name", help="Machine Name", action='store', required=True)
    parser.add_argument("-u", "--url", dest="url", help="Target URL", action='store', required=True)
    args = parser.parse_args()
    validate(args)
    outcome = Outcome(args.name, args.url)
    return outcome

def validate(args):
    pass
