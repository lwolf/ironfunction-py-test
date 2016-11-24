import sys
sys.path.append("packages")
import os
import json
from slacker import Slacker


if not os.isatty(sys.stdin.fileno()):
    obj = json.loads(sys.stdin.read())
    if all([x in obj for x in ['token', 'channel', 'message']]):
        slack = Slacker(obj['token'])
        slack.chat.post_message(obj['channel'], obj['message'])
        print("posting `{message}` to channel #{channel}".format(**obj))
