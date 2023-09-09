
from logging import getLogger, config
import os
import asyncio
config.fileConfig(os.path.join(os.path.dirname(__file__), "./logging.ini"), encoding='utf-8')
logger = getLogger(__name__)
from stopwatch import StopWatch

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    logger.debug(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     stdout2 = stdout.decode('cp932', 'ignore').strip()
    #     logger.debug(f'[stdout]\n{stdout2}')
    # if stderr:
    #     logger.debug(f'[stderr]\n{stdout}')

async def main():
    await asyncio.gather(
        run('ping localhost'),
        run('ping 127.0.0.1'))

watch = StopWatch()
logger.debug('開始')
asyncio.run(main())
watch.stop()
logger.debug('終了')