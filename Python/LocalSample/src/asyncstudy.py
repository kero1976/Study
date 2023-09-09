import asyncio
import time

async def f(tag):
    for i in range(3):
        await asyncio.sleep(1)
        print("waiting for f(%d)" % tag)
    return "hello %d" % tag

loop = asyncio.get_event_loop()
tasks = [f(n) for n in range(3)]
ret = loop.run_until_complete(asyncio.gather(*tasks))
print(ret)