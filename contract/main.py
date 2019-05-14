
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


if __name__ == "__main__":
    st = get_stdin()
    ret = contract.handler(st)
    if ret is not None:
        sys.stdout.write(json.dumps(ret))
