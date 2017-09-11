import pya3rt
import os
env = os.environ

apikey = env["TALK_API"]
client = pya3rt.TalkClient(apikey)

def send_messages(message):
    return client.talk(message)

while 1:
    msg = input()
    rep = send_messages(msg)
    rep = rep["results"][0]["reply"]
    print("(bot) " + rep)
    if msg == "さようなら":
        break