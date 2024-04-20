import tempfile
import shutil
from certificateutil.file.file_writer import FileWriter
import pytest


def test_write_text_utf8_ok():
    text = "これはUTF-8です"
    writer = FileWriter("test-utf8.txt")

    writer.write_text_utf8(text)


def test_write_binary_ok():
    text = "これはバイナリです"
    writer = FileWriter("test-bin.txt")

    writer.write_text_utf8(text)
