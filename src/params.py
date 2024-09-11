from json import dumps
from typing import Dict, Optional

from src.constants import ACCESS_KEY, POST_METHOD


class Param:
    def __init__(self, event: Dict):

        self.event = event

        self.headers = dict()
        self.http = dict()

        self.__set_headers()
        self.__set_http()

    def __set_headers(self) -> None:
        self.headers = self.event["headers"]

    def __set_http(self) -> None:
        self.http = self.event.get("requestContext").get("http")

    def have_issues(self) -> Optional[Dict]:

        if self.http.get("method") != POST_METHOD:
            return {
                "statusCode": 501,
                "body": dumps({"message": "method not allowed"}),
            }

        if self.headers.get("x-api-key") != ACCESS_KEY:
            return {
                "statusCode": 502,
                "body": dumps({"message": "user not allowed"}),
            }

        return None
