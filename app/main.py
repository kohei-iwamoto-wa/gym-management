from typing import Union
from fastapi import FastAPI
import boto3
from botocore.exceptions import ClientError

app = FastAPI()

# DynamoDB接続
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000', region_name='us-west-2')
table_name = 'Users'
table = dynamodb.Table(table_name)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    
@app.get("/ping-dynamodb")
def ping_dynamodb():
    try:
        # データを put
        put_response = table.put_item(Item={"UserID": "test001", "name": "Sample Name", "age": 25})

        # データを get
        get_response = table.get_item(Key={"UserID": "test001"})
        item = get_response.get("Item", {})

        return {
            "put_result": "success",
            "get_result": "success" if item else "not_found",
            "item": item
        }

    except ClientError as e:
        return {
            "error": e.response["Error"]["Message"]
        }