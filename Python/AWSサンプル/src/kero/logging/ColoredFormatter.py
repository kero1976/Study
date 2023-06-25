from logging import Formatter, ERROR, WARNING, INFO, DEBUG
from termcolor import colored


class ColoredFormatter(Formatter):
    def format(self, record):
        # ログメッセージに色を付ける
        if record.levelno == ERROR:
            # エラーレベルのログメッセージを赤色で表示
            record.msg = colored(record.msg, 'red')
        elif record.levelno == WARNING:
            # 警告レベルのログメッセージを黄色で表示
            record.msg = colored(record.msg, 'yellow')
        elif record.levelno == INFO:
            # 情報レベルのログメッセージを青色で表示
            record.msg = colored(record.msg, 'blue')
        elif record.levelno == DEBUG:
            # デバッグレベルのログメッセージをシアンで表示
            record.msg = colored(record.msg, 'cyan')
        return super().format(record)
