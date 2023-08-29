from logging import getLogger


logger = getLogger(__name__)


class GetBucket:
    """
    S3のバケット情報を取得するクラス.
    """
    def __init__(self, client):
        logger.debug({
            "action": "init",
            "param": {
                "client": client
            }
        })
        self.client = client

    def get_reasion_bucket(self, reagion: str) -> list[str]:
        """
        """
        pass

    def _get_all_bucket_name(self) -> list[str]:
        """バケット名の一覧を取得する.

        Returns:
            list[str]: バケット名のリスト
        """
        logger.debug({
            "action": "start"
        })
        try:
            response = self.client.list_buckets()
            result = [i['Name'] for i in response['Buckets']]
            logger.debug({
                "action": "success",
                "result": result
            })
            return result
        except Exception as e:
            logger.debug({
                "action": "fail",
                "message": "Error!",
                "Exception": e
            })