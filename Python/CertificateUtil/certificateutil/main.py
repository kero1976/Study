from file.file_reader import FileReader
from file.file_writer import FileWriter
from base64util.decoder import Base64Decoder
import base64

# from logging import getLogger, StreamHandler, DEBUG, Formatter
from logging import getLogger, StreamHandler, DEBUG, Formatter, basicConfig

# logger = getLogger(__name__)

# logger.setLevel(DEBUG) 
# console_handler = StreamHandler()
# format = Formatter("%(asctime)s:%(levelname)s:%(filename)s(%(lineno)s):%(funcName)s:%(message)s")
# console_handler.setFormatter(format)
# logger.addHandler(console_handler)

basicConfig(level=DEBUG, format="%(asctime)s:%(levelname)-5s:<%(process)d:%(thread)d>%(filename)s(%(lineno)s):%(funcName)s:%(message)s")

input_file = "C:/Users/kero/ssl/privatekey/server.key"
output_file = "C:/Users/kero/ssl/privatekey/output2.bin"

in_file = FileReader(input_file)
in_file._read_binary()
data = Base64Decoder.decode(in_file.file_data)
out_file = FileWriter(output_file)
out_file.data = data
out_file.write_binary()

# # base64形式のファイルを読み込みます
# with open(input_file, "rb") as f:
#     encoded_data = f.read()

# # base64デコードを行います
# decoded_data = base64.b64decode(encoded_data)

# # デコードされたデータを出力ファイルに書き込みます
# with open(output_file, "wb") as f:
#     f.write(decoded_data)