
import sys
import json
import ast
from lib import contract


def get_stdin():
    buf = ""
    while True:
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return buf


def arg_as_dict(self):
    v = ast.literal_eval(self)
    if type(v) is not dict:
        raise "Issues"
    return v

if __name__ == "__main__":
    st = get_stdin()
    ret = contract.handler(arg_as_dict(st))
    if ret is not None:
        sys.stdout.write(json.dumps(ret))
