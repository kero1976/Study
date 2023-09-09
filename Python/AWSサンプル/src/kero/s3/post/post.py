from pathlib import Path

import boto3
import io

s3 = boto3.resource('s3')
bucket = s3.Bucket('kerodoc')

KEY = 'yougoyashikumi_2023.pdf'
ORIGIN_PATH = Path('G:/本/セキュリティ/IPA/2023/yougoyashikumi_2023.pdf')

bucket.upload_file(str(ORIGIN_PATH), KEY)