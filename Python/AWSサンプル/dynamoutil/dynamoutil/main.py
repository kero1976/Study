from dynamoutil.aws.dynamodb import dynamodb_all_data
from dynamoutil.localfile.app import create_dir_file

if __name__ == "__main__":
    
    print("START")
    table_name = "idolmaster"
    alldata = dynamodb_all_data(table_name)
    create_dir_file(table_name, alldata)
    print("END")