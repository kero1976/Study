import asyncio
import subprocess
from termcolor import colored

from logging import getLogger, config
import os
import asyncio
config.fileConfig(os.path.join(os.path.dirname(__file__), "./logging.ini"), encoding='utf-8')
logger = getLogger(__name__)

# async def run_subprocess(cmd):
#     proc = await asyncio.create_subprocess_shell(
#         cmd,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
#     stdout, stderr = await proc.communicate()
#     return stdout, stderr


# def main(command):

#     # サブプロセスを非同期で実行
#     # stdout, stderr = await run_subprocess(command)
#     stdout, stderr = asyncio.run(run_subprocess(command))
#     stdout = stdout.decode('cp932', 'ignore').strip()
#     stderr = stderr.decode('cp932', 'ignore').strip()
#     print(f'Stdout: {stdout}')
#     print(f'Stderr: {stderr}')

async def run_subprocess(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()
    return stdout, stderr

async def main(commands):
    tasks = []
    for command in commands:
        tasks.append(asyncio.create_task(run_subprocess(command)))

    result = await asyncio.gather(*tasks)
    # stdout = stdout.decode('cp932', 'ignore').strip()
    for i in result:
        stdout = i[0].decode('cp932', 'ignore').strip()
        logger.debug(stdout)


logger.debug(colored('開始', 'red'))
# asyncio.run(main())
asyncio.run(main(['ping localhost', 'ping 127.0.0.1']))

logger.debug(colored('終了', 'red'))