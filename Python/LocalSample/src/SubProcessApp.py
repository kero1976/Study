import subprocess
from logging import getLogger, config
import os
import asyncio
from stopwatch import StopWatch
from termcolor import colored


config.fileConfig(os.path.join(os.path.dirname(__file__), "./logging.ini"), encoding='utf-8')
logger = getLogger(__name__)


def call(execute: str) -> int:
    """
    同期呼び出し
    """
    logger.debug({"ACTION": "START",
                  "PARAM": execute})
    runcmd = subprocess.call(execute.split())
    return runcmd


async def run_subprocess(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    return stdout, stderr


async def asyncCall(executes: list):
    """
    非同期呼び出し
    """
    logger.debug({"ACTION": "START",
                  "PARAM": executes})
    tasks = []
    for command in executes:
        tasks.append(asyncio.create_task(run_subprocess(command)))

    result = await asyncio.gather(*tasks)
    for i in result:
        stdout = i[0].decode('cp932', 'ignore').strip()
        logger.debug(stdout)


if __name__ == "__main__":
    watch = StopWatch()
    call1 = call("ping localhost")
    logger.debug(colored(watch.stop(), 'red'))
    call2 = call("ping 127.0.0.1")
    logger.debug(colored(watch.stop(), 'red'))
    print(f"**********{call1}")
    print(f"**********{call2}")
    watch.print()

    # 非同期実行用
    # watch = StopWatch()
    # asyncio.run(asyncCall(['ping localhost', 'ping 127.0.0.1']))
    # logger.debug(colored(watch.stop(),'red'))
    # watch.print()
