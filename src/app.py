from json import dumps
from typing import Dict

from src.params import Param


def main(event, context) -> Dict:

    param = Param(event)

    issue = param.have_issues()

    if issue is not None:
        return issue

    return {
        "statusCode": 200,
        "body": dumps({"event": param.event}),
    }
