import boto3
from logging import getLogger


logger = getLogger(__name__)

def sample1(data1, data2, data3):
    client = boto3.client("dynamodb")


    response = client.put_item(
        Item={
            'AlbumTitle': {
                'S': data1,
            },
            'Artist': {
                'S': data2,
            },
            'SongTitle': {
                'S': data3,
            },
        },
        ReturnConsumedCapacity='TOTAL',
        TableName='Music',
    )

    print(response)

# sample1('Somewhat Famous', 'No One You Know', 'Call Me Today')
sample1('Somewhat Famous', 'No One You Know', 'Call Me Today2')