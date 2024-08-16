from logging import getLogger

import boto3
from botocore.config import Config

logger = getLogger(__name__)


class Coonnection:

    no_proxy_config = Config(proxies={"http": None, "https": None})

    def __init__(self, profile_name: str = None, endpoint_url: str = None):
        logger.debug(f"init({profile_name=}, {endpoint_url=})")
        self.profile_name = profile_name
        self.endpoint_url = endpoint_url

    def get_resource(self, name: str):
        logger.debug(f"start resource({name=})")
        try:
            if self.endpoint_url is None:
                if self.endpoint_url is None:
                    logger.debug(
                        f"Create {name} resource for AWS connections with default profile."
                    )
                    resource = boto3.resource(name)
                else:
                    logger.debug(
                        f"Create {name} resource for local connections with default profile."
                    )
                    resource = boto3.resource(
                        name,
                        endpoint_url=self.endpoint_url,
                        config=self.no_proxy_config,
                    )
            else:
                if self.endpoint_url is None:
                    logger.debug(
                        f"Create {name} resource for AWS connections with {self.profile_name} profile."
                    )
                    session = boto3.Session(profile_name=self.profile_name)
                    resource = session.resource(name)
                else:
                    logger.debug(
                        f"Create {name} resource for local connections with {self.profile_name} profile."
                    )
                    session = boto3.Session(profile_name=self.profile_name)
                    resource = session.resource(
                        name,
                        endpoint_url=self.endpoint_url,
                        config=self.no_proxy_config,
                    )
            logger.debug(f"success({resource=})")
            return resource
        except Exception as e:
            logger.error(f"fail({e=})")
            return None
