import boto3

def sample1():
    """キー項目でスキャン
    """
    client = boto3.client("dynamodb")

    response = client.scan(
        ExpressionAttributeNames={
            '#AT': 'AlbumTitle',
            '#ST': 'SongTitle',
        },
        ExpressionAttributeValues={
            ':a': {
                'S': 'No One You Know',
            },
        },
        FilterExpression='Artist = :a',
        ProjectionExpression='#ST, #AT',
        TableName='Music',
    )

    print(response)


def sample2():
    """キー項目以外でスキャン
    """
    client = boto3.client("dynamodb")

    response = client.scan(
        ExpressionAttributeNames={
            '#AT': 'AlbumTitle',
            '#ST': 'SongTitle',
        },
        ExpressionAttributeValues={
            ':a': {
                'S': 'Somewhat Famous',
            },
        },
        FilterExpression='AlbumTitle = :a',
        ProjectionExpression='#ST, #AT',
        TableName='Music',
    )

    print(response)

sample2()