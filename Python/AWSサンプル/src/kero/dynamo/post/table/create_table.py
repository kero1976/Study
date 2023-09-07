import boto3

def sample1():
    """_summary_
    パーティションキー:Artist 
    ソートキー:SongTitle
    """
    client = boto3.client("dynamodb")

    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SongTitle',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SongTitle',
                'KeyType': 'RANGE',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        },
        TableName='Music',
    )

    print(response)


def sample2():
    """_summary_
    パーティションキー:Artist 
    ソートキー:なし
    """
    client = boto3.client("dynamodb")

    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },

        ],
        KeySchema=[
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        },
        TableName='Music2',
    )

    print(response)

sample1()