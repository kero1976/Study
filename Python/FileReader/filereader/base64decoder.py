from filereader.file_reader import FileReader
import base64

def decode(strdata: str, outputfile):
    data = base64.b64decode(strdata)
    with open(outputfile, 'wb') as file:
        file.write(data)
    
    
if __name__ == "__main__":
    print("START")
    input_file = "C:/作成したKey/test.txt"
    output_file = "C:/作成したKey/test2.bin"
    file = FileReader(input_file)
    file.read()
    decode(file.file_data, output_file)