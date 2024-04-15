from file.file_reader import FileReader
from file.file_writer import FileWriter
from base64util.decoder import Base64Decoder


from logging import getLogger, StreamHandler, DEBUG, Formatter

logger = getLogger(__name__)

logger.setLevel(DEBUG) 
console_handler = StreamHandler()
format = Formatter("%(asctime)s:%(levelname)s:%(filename)s(%(lineno)s):%(funcName)s:%(message)s")
console_handler.setFormatter(format)
logger.addHandler(console_handler)

input = "C:/Users/kero/ssl/privatekey/decodetest.pem"
outfile = "C:/Users/kero/ssl/privatekey/output.bin"

in_file = FileReader(input)
in_file.read()
data = Base64Decoder.decode(in_file.read())
out_file = FileWriter(outfile)
out_file.data = data
out_file.write_binary()