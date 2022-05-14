import json

import requests
import abc



def lambda_handler(event, context):
    r=requests.get("https://lerneprogrammieren.de")
    print(r.content)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello akshay",
        }),
    }
