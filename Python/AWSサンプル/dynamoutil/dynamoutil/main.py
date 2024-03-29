from dynamoutil.aws.dynamodb import DynamoDb
from dynamoutil.localfile.app import create_dir_file

if __name__ == "__main__":
    db = DynamoDb()
    dynamodb = db.get_resource()
    table = db.get_table(dynamodb, "idolmaster")
    alldata = db.get_all_data(table)
    create_dir_file("idolmaster", alldata)
    print("OK")