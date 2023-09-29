from logging import getLogger
import logging
from botocore.exceptions import ClientError
import time
# ロガーの作成
logger = getLogger(__name__)

botocore = logging.getLogger("botocore")
botocore.setLevel(logging.ERROR)
urllib3 = logging.getLogger("urllib3")
urllib3.setLevel(logging.ERROR)
boto3 = logging.getLogger("boto3")
boto3.setLevel(logging.ERROR)

class dynamo2():
    """dynamodbをtable resourceを使ってアクセスするユーティリティ
    """

    def __init__(self, dynamo):
        """コンストラクタ

        Args:
            dynamo (_type_): DynamoDB Resource
        """
        logger.debug({
            "action": "init",
            "param": {
                "dynamo": dynamo
            }
        })
        self.dynamo = dynamo

    def create_table(self,table_name: str, key_schema: list[dict], attribute_definitions: list[dict], local_secondary_indexes: list[dict], global_secondary_indexes: list[dict] ):
        """テーブルの作成

        Args:
            table_name (str): テーブル名
            key_schema (list[dict]): _description_
            attribute_definitions (list[dict]): _description_
            local_secondary_indexes (list[dict]): _description_
            global_secondary_indexes (list[dict]): _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "key_schema": key_schema,
                "attribute_definitions": attribute_definitions,
                "local_secondary_indexes": local_secondary_indexes,
                "global_secondary_indexes": global_secondary_indexes
            }
        })
        try:
            response = self.dynamo.create_table(
                TableName = table_name,
                KeySchema = key_schema,
                AttributeDefinitions = attribute_definitions,
                ProvisionedThroughput = {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                },
                LocalSecondaryIndexes =local_secondary_indexes,
                GlobalSecondaryIndexes=global_secondary_indexes,
            )
            logger.info({
                "action": "success"
            })
        except ClientError as err:
            if err.response['Error']['Code'] == 'ResourceInUseException':
                logger.info({
                    "action": "fail",
                    "message": f"ResourceInUseException({table_name})"
                })
            else:
                logger.error({
                    "action": "fail",
                    "code": err.response['Error']['Code'],
                    "Message": err.response['Error']['Message']
                })

    def list_all_tables(self) -> list[str]:
        """すべてのテーブル名を取得する

        Returns:
            list[str]: すべてのテーブル名
        """
        logger.debug({
            "action": "start"
        })
        response = self.dynamo.tables.all()
        logger.debug({
            "action": "run",
            "message": "tables.all",
            "type": type(response),
            "response": response
        })
        result = []
        for x in response:
            result.append(x._name)

        logger.info({
            "action": "success",
            "result": {
                "type": type(result),
                "size": len(result),
                "value": result
            }
        })
        return result

    def table_detail(self, table_name) -> dict:
        """テーブルの詳細情報を取得する
        ・テーブル名
        ・属性定義
        ・キー情報
        ・データ件数
        ・テーブル作成日
        Args:
            table_name (_type_): テーブル名

        Returns:
            dict: テーブル情報
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name
            }
        })
        try:
            table = self.dynamo.Table(table_name)
            table.load()
            logger.debug({
                "action": "run",
                "message": "Table",
                "type": type(table),
                "response": table
            })
            result = {}
            # テーブル名
            result["table_name"] = table.table_name
            # 属性定義
            result["attribute_definitions"] = table.attribute_definitions
            # KeySchema
            result["key_schema"] = table.key_schema
            # item_count
            result["item_count"] = table.item_count
            # table_status
            result["table_status"] = table.table_status
            # creation_date_time
            result["creation_date_time"] = table.creation_date_time.isoformat()
            # for i in dir(table):
            #     print(i)
            logger.info({
                "action": "success",
                "result": {
                    "type": type(result),
                    "size": len(result),
                    "value": result
                }
            })
            return result
        except ClientError as err:
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                logger.info({
                    "action": "fail",
                    "message": f"ResourceNotFoundException({table_name})"
                })
            else:
                logger.error({
                    "action": "fail",
                    "code": err.response['Error']['Code'],
                    "Message": err.response['Error']['Message']
                })

    def list_put_items(self, table_name: str, items: list[str]):
        """データの一括登録

        Args:
            table_name (str): _description_
            items (list[str]): _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "items": items,
            }
        })
        table = self.dynamo.Table(table_name)
        with table.batch_writer() as batch:
            for item in items:
                response = batch.put_item(Item=item)
                logger.debug({
                    "action": "run",
                    "message": "tables.all",
                    "type": type(response),
                    "response": response
                })
        logger.info({
            "action": "success"
        })

    def scan_all_items(self, table_name):
        """データ全件取得

        Args:
            table_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name
            }
        })

        table = self.dynamo.Table(table_name)
        response = table.scan()
        logger.debug({
            "action": "run",
            "message": "tables.all",
            "type": type(response),
            "response": response
        })
        result = response["Items"]
        logger.info({
            "action": "success",
            "count": len(result)
        })
        return result
    
    def scan_filter_items(self, table_name, filter_expression):
        """スキャン

        Args:
            table_name (_type_): _description_
            filter_expression (_type_): _description_

        Returns:
            _type_: _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "filter_expression": filter_expression
            }
        })

        table = self.dynamo.Table(table_name)
        result = []
        options = {
            "FilterExpression": filter_expression,
            "Limit": 1
        }
        while True:
            response = table.scan(**options)
            result += response.get('Items', [])
            logger.debug({
                "action": "run",
                "message": "tables.all",
                "type": type(response),
                "response": response
            })
            if 'LastEvaluatedKey' not in response:
                break
            options['ExclusiveStartKey'] = response['LastEvaluatedKey']

        logger.info({
            "action": "success",
            "count": len(result)
        })
        return result
    
    def query_filter_items(self, table_name, key_condition_expression):
        """クエリー

        Args:
            table_name (_type_): _description_
            key_condition_expression (_type_): _description_

        Returns:
            _type_: _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "key_condition_expression": key_condition_expression
            }
        })

        table = self.dynamo.Table(table_name)
        result = []
        options = {
            "KeyConditionExpression": key_condition_expression
        }
        while True:
            response = table.query(**options)
            result += response.get('Items', [])
            logger.debug({
                "action": "run",
                "message": "query",
                "type": type(response),
                "response": response
            })
            if 'LastEvaluatedKey' not in response:
                break
            options['ExclusiveStartKey'] = response['LastEvaluatedKey']

        logger.info({
            "action": "success",
            "count": len(result)
        })
        return result
    
    def index_items(self, table_name, index_name, key_condition_expression = None):
        """_summary_

        Args:
            table_name (_type_): _description_
            index_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "index_name": index_name,
                "key_condition_expression": key_condition_expression
            }
        })

        table = self.dynamo.Table(table_name)
        result = []
        options = {
            "IndexName": index_name,
            "Limit": 1
        }
        if key_condition_expression:
            options["KeyConditionExpression"] = key_condition_expression

        while True:
            response = table.query(**options)
            result += response.get('Items', [])
            logger.debug({
                "action": "run",
                "message": "query",
                "type": type(response),
                "response": response
            })
            if 'LastEvaluatedKey' not in response:
                break
            options['ExclusiveStartKey'] = response['LastEvaluatedKey']

        logger.info({
            "action": "success",
            "count": len(result)
        })
        return result
    
    def insert(self, table_name, item, condition_expression):
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "item": item,
                "condition_expression": condition_expression
            }
        })
        table = self.dynamo.Table(table_name)
        try:
            result = table.put_item(Item=item, ConditionExpression=condition_expression)
            logger.info({
                "action": "run",
                "message": "put_item",
                "type": type(result),
                "response": result
            })
            logger.info({
                "action": "success",
            })
        except ClientError as err:
            if err.response['Error']['Code'] == 'ConditionalCheckFailedException':
                logger.info({
                    "action": "fail",
                    "message": f"ConditionalCheckFailedException({condition_expression})"
                })
            else:
                logger.error({
                    "action": "fail",
                    "code": err.response['Error']['Code'],
                    "Message": err.response['Error']['Message']
                })

    def update(self, table_name, key, update_expression, expression_attribute_names,expression_attribute_values,condition_expression):
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
                "key": key,
                "update_expression": update_expression,
                "expression_attribute_names": expression_attribute_names,
                "expression_attribute_values": expression_attribute_values,
                "condition_expression": condition_expression
            }
        })
        table = self.dynamo.Table(table_name)
        try:
            result = table.update_item(Key=key, UpdateExpression=update_expression, ExpressionAttributeNames=expression_attribute_names, ExpressionAttributeValues=expression_attribute_values, ConditionExpression=condition_expression)
            logger.info({
                "action": "run",
                "message": "update_item",
                "type": type(result),
                "response": result
            })
            logger.info({
                "action": "success",
            })
        except ClientError as err:
            if err.response['Error']['Code'] == 'ConditionalCheckFailedException':
                logger.info({
                    "action": "fail",
                    "message": f"ConditionalCheckFailedException({condition_expression})"
                })
            else:
                logger.error({
                    "action": "fail",
                    "code": err.response['Error']['Code'],
                    "Message": err.response['Error']['Message']
                })

    def delete_table(self, table_name:str):
        logger.debug({
            "action": "start",
            "param": {
                "table_name": table_name,
            }
        })
        try:
            table = self.dynamo.Table(table_name)
            table.delete()
            logger.debug({
                "action": "success",
                "message": f"Table({table_name}) is deleted.",
            })
        except ClientError as err:
            if err.response['Error']['Code'] == 'ResourceNotFoundException':
                logger.info({
                    "action": "fail",
                    "message": f"Table({table_name}) is not found."
                })
            else:
                logger.error({
                    "action": "fail",
                    "message": f"予期せぬエラー",
                    "exception": err
                })