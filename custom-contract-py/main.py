import sys
import json
import ast
from lib import contract


def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return buf

def convert_type(param):
    """ Convert paramters input int expected type """
    if not (param is None):
        return ast.literal_eval(param)

if __name__ == "__main__":
    st = get_stdin()
    ret = contract.handler(convert_type(st))
    if ret is not None:
        sys.stdout.write(json.dumps(ret))