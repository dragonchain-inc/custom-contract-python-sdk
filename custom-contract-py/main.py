  
import sys
import json
from calculator import calculator


def get_stdin():
    buf = ""
    while(True):
        line = sys.stdin.readline()
        buf += line
        if line == "":
            break
    return buf


if __name__ == "__main__":
    st = get_stdin()
    ret = calculator.main(st)
    if ret is not None:
        sys.stdout.write(json.dumps(ret))