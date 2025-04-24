from typing import Union
from fastapi import FastAPI
import logging
import boto3
from botocore.exceptions import ClientError

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# DynamoDB接続
dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb-local:8000', region_name='us-west-2')
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
        logger.info("Fetching item from DynamoDB")
        get_response = table.get_item(Key={"UserID": "user123"})
        logger.info(f"DynamoDB get response: {get_response}")
        
        item = get_response.get("Item", {})
        logger.info(f"Retrieved item: {item}")
        
        # 正常なレスポンスを返す
        return {"get_result": "success", "item": item}

    except ClientError as e:
        logger.error(f"ClientError occurred: {e.response['Error']['Message']}")
        return {"error": e.response["Error"]["Message"]}
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")
        return {"error": "Internal Server Error"}