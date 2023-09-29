from kero.dynamo.dynamotable import dynamo2
import boto3
import logging
import pytest
import pprint
from boto3.dynamodb.conditions import Attr, Key
import datetime

dynamodb = boto3.resource('dynamodb', endpoint_url='http://192.168.50.204:8000')
# dynamodb = boto3.resource('dynamodb')
botocore = logging.getLogger("botocore")
botocore.setLevel(logging.ERROR)
urllib3 = logging.getLogger("urllib3")
urllib3.setLevel(logging.ERROR)

@pytest.mark.skip
def test_listtables():
    """登録されているテーブルの一覧を取得する
    """
    dynamo = dynamo2(dynamodb)
    dynamo.list_all_tables()

@pytest.mark.skip
def test_table_datail():
    """指定したテーブルの詳細情報を取得する
    """
    dynamo = dynamo2(dynamodb)
    # dynamo.table_detail("Music")
    dynamo.table_detail("sample")


@pytest.mark.skip
def test_table_create():

    TableName = 'idolmaster'
    KeySchema = [
        {
            'AttributeName': 'series',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'
        },
    ]
    AttributeDefinitions = [
        {
            'AttributeName': 'series',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'type',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'birthday',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'height',
            'AttributeType': 'N'
        },
    ]
    LocalSecondaryIndexes=[
        {
            'IndexName': 'typeLSIndex',
            'KeySchema': [
                {
                    'AttributeName': 'series',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'type',
                    'KeyType': 'RANGE'
                }
            ],
            'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': [
                    'name',
                ]
            }
        },
    ]
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'birthHeightGSIndex',
            'KeySchema': [
                {
                    'AttributeName': 'birthday',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'height',
                    'KeyType': 'RANGE'
                },
            ],
            'Projection': {
                'ProjectionType': 'KEYS_ONLY',
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        },
    ]
    dynamo = dynamo2(dynamodb)
    dynamo.create_table(TableName, KeySchema, AttributeDefinitions, LocalSecondaryIndexes, GlobalSecondaryIndexes)

@pytest.mark.skip
def test_list_put_items():
    """データの登録
    """
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    Items = [{
                'series': 'シンデレラガールズ',
                'name': '島村卯月',
                'type': 'キュート',
                'birthday': '0424',
                'height': 159,
                'home': '東京'
            },
            {
                'series': 'シンデレラガールズ',
                'name': '渋谷凛',
                'type': 'クール',
                'birthday': '0810',
                'height': 165,
                'home': '東京'
            },{
                'series': 'シンデレラガールズ',
                'name': '本田未央',
                'type': 'パッション',
                'birthday': '1201',
                'height': 161,
                'home': '千葉'
            },{
                'series': 'SideM',
                'name': '天ヶ瀬冬馬',
                'type': 'フィジカル',
                'birthday': '0303',
                'height': 175,
                'home': '神奈川'
            },{
                'series': 'SideM',
                'name': '伊集院北斗',
                'type': 'インテリ',
                'birthday': '0214',
                'height': 180,
                'home': '京都'
            },{
                'series': 'SideM',
                'name': '御手洗翔太',
                'type': 'メンタル',
                'birthday': '0420',
                'height': 163,
                'home': '東京'
            },{
                'series': 'ミリオンライブ',
                'name': '箱崎星梨花',
                'type': 'エンジェル',
                'birthday': '0220',
                'height': 146
            },{
                'series': 'ミリオンライブ',
                'name': '北沢志保',
                'type': 'フェアリー',
                'birthday': '0118',
                'height': 161
            },{
                'series': 'ミリオンライブ',
                'name': '七尾百合子',
                'type': 'プリンセス',
                'birthday': '0318',
                'height': 154

            }]
    dynamo.list_put_items(TableName, Items)

@pytest.mark.skip
def test_scan_all_items():
    """データ全件取得
    """
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    response = dynamo.scan_all_items(TableName)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)

@pytest.mark.skip
def test_scan_filter_items():
    """データ抽出(スキャン)
    """
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    FilterExpression=Attr('home').eq('東京')
    # FilterExpression=Attr('home').eq('東京') | Key('series').eq('シンデレラガールズ')
    # FilterExpression=Attr('home').eq('東京') & Key('series').eq('シンデレラガールズ')
    # FilterExpression=Attr('home').eq('東京') & Attr('series').eq('シンデレラガールズ')
    response = dynamo.scan_filter_items(TableName, FilterExpression)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)

@pytest.mark.skip
def test_query_filter_items():
    """データ抽出(クエリ)
    """
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    # KeyConditionExpression=Key('series').eq('SideM')
    KeyConditionExpression=Key('series').eq('シンデレラガールズ') & Key('name').begins_with('島')
    response = dynamo.query_filter_items(TableName, KeyConditionExpression)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)

@pytest.mark.skip
def test_index_items():
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    IndexName="typeLSIndex"
    KeyConditionExpression=Key('series').eq('ミリオンライブ') & Key('type').begins_with('フ')
    # response = dynamo.index_items(TableName, IndexName)
    response = dynamo.index_items(TableName, IndexName, KeyConditionExpression)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)

@pytest.mark.skip
def test_insert():
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    dt_now = datetime.datetime.now()
    series = "hoo4"
    name = "bar1"
    Item = {
                'series': series,
                'name': name,
                'type': 'キュート',
                'birthday': '0424',
                'height': 159,
                "time": dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
            }
    # ConditionExpression = "attribute_not_exists(series) and attribute_not_exists(series)"
    ConditionExpression=Attr('series').eq(series) 
    dynamo.insert(TableName, Item, ConditionExpression)
    KeyConditionExpression=Key('series').eq(series) 
    response = dynamo.query_filter_items(TableName, KeyConditionExpression)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)


def test_update():
    dynamo = dynamo2(dynamodb)
    TableName = 'idolmaster'
    dt_now = datetime.datetime.now()
    series = "hoo4"
    name = "bar1"
    UpdateKey = {
                'series': series,
                'name': name
            }
    UpdateExpression = "SET #time = :time, #height = :height"
    ExpressionAttributeNames = {
        "#time": "time",
        "#height": "height"
    }
    ExpressionAttributeValues = {
        ":time": dt_now.strftime('%Y年%m月%d日 %H:%M:%S'),
        ":height": 161
    }

    # ConditionExpression = "attribute_not_exists(series) and attribute_not_exists(series)"
    ConditionExpression=Attr('height').eq(159)
    dynamo.update(TableName, UpdateKey, UpdateExpression, ExpressionAttributeNames, ExpressionAttributeValues, ConditionExpression)

    KeyConditionExpression=Key('series').eq(series) 
    response = dynamo.query_filter_items(TableName, KeyConditionExpression)
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(response)

@pytest.mark.shijo
def testshijo():
    dynamo = dynamo2(dynamodb)
    # response = dynamo.list_all_tables()
    # pp = pprint.PrettyPrinter(width=41, compact=True)
    # dynamo.delete_table("idolmaster3")
    # pprint.pprint(response)
    dynamo.delete_all_items("idolmaster")