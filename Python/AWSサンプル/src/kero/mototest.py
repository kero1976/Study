import boto3
import moto
import pytest

# テスト対象の関数
def upload_file_to_s3(bucket_name, file_name, content):
    s3 = boto3.client('s3', region_name='us-east-1')
    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=content)
    except Exception as e:
        raise e

# テストケース
@moto.mock_s3
def test_upload_file_to_s3_exception():
    # モックのS3バケットを作成
    bucket_name = 'test-bucket'
    conn = boto3.client('s3', region_name='us-east-1')
    conn.create_bucket(Bucket=bucket_name)

    # ファイルの内容
    file_name = 'test.txt'
    content = b'This is a test file.'

    # エラーレスポンスをシミュレート
    # 特定の条件でエラーを発生させるためのエラーレスポンスを定義
    error_response = {
        'Error': {
            'Code': 'AccessDenied',  # エラーコードを設定
            'Message': 'Permission denied',  # エラーメッセージを設定
        }
    }

    # モックのS3クライアントにエラーレスポンスを設定
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.exceptions.put_object = error_response  # put_objectアクションのエラーを設定

    # ファイルをアップロードし、エラーをキャッチ
    with pytest.raises(Exception) as excinfo:
        upload_file_to_s3(bucket_name, file_name, content)

    # 例外が正しく発生したことを確認
    assert 'AccessDenied' in str(excinfo.value)

# テストを実行
if __name__ == '__main__':
    test_upload_file_to_s3_exception()
