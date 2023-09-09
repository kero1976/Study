import os
from pathlib import Path
from typing import Optional

import boto3
from dataclasses import dataclass
from lauda import stopwatch


@dataclass
class S3Manager:
    source_bucket: str
    source_prefix: str
    profile: Optional[str] = None

    def _session(self):
        s = boto3.session.Session(
            profile_name=self.profile
        )
        return s

    def list_all_test(self):
        s3_resource = self._session().resource('s3')
        a = s3_resource.Bucket(self.source_bucket).objects.filter(Prefix=self.source_prefix)
        b = [k.key for k in a]
        print(len(b))
        print(b)


if __name__ == '__main__':
    os.chdir(Path(__file__).parents[1])

    @stopwatch
    def test():
        s3 = S3Manager(
            source_bucket='u10.jp',
            source_prefix='sample',
        )
        # s3.list_all()
        s3.list_all_test()

    test()