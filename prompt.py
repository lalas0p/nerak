

from nerak import Nerak
from threading import Thread
import asyncio

nerak = Nerak()
a = ""
def aType():
    nerak.typeReply(a)

def between_callback(args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(aType(args))
    loop.close()

while True:
    a = nerak.getInput()
    t = Thread(target=aType)
    t.daemon = True
    t.start()
    nerak.speakReply(a)