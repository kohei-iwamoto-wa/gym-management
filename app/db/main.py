from typing import Union
from fastapi import FastAPI
import logging
import boto3
from botocore.exceptions import ClientError
import os
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# DynamoDB接続
# dynamodb = boto3.resource('dynamodb', endpoint_url='http://dynamodb-local:8000', region_name='us-west-2')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table_name = 'Users'
table = dynamodb.Table(table_name)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/aloha")
# def read_root():
#     return {"aloha": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
    
# @app.get("/ping-dynamodb")
# def ping_dynamodb():
#     try:
#         logger.info("Fetching item from DynamoDB")
#         get_response = table.get_item(Key={"UserID": "user123"})
#         logger.info(f"DynamoDB get response: {get_response}")
        
#         item = get_response.get("Item", {})
#         logger.info(f"Retrieved item: {item}")
        
#         # 正常なレスポンスを返す
#         return {"get_result": "success", "item": item}

#     except ClientError as e:
#         logger.error(f"ClientError occurred: {e.response['Error']['Message']}")
#         return {"error": e.response["Error"]["Message"]}
#     except Exception as e:
#         logger.error(f"Unexpected error occurred: {str(e)}")
#         return {"error": f"Internal Server Error: {e}"}

# @app.post("/aurora-connection-test")
# def aurora_connection_test():
#     try:
#         ssm = boto3.client('ssm', region_name='us-west-2')
#         # パラメータを取得
#         response = ssm.get_parameter(Name='database_pw', WithDecryption=True)
#         # 値を取得
#         db_password = response['Parameter']['Value']
#         print(f"DB Password: {db_password}")
#         # db_password = os.getenv("DB_PASSWORD")

#         engine = create_engine(f'mysql+pymysql://admin_user:{db_password}@gym-management-database.cluster-cduo888s8cr1.us-west-2.rds.amazonaws.com:3306/gym_db')

#         metadata = MetaData()

#         users = Table('users', metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String(255)),
#                     Column('age', Integer),
#                     Column('email', String(255))
#                     )

#         metadata.create_all(engine)

#         insert_stmt = users.insert().values(
#             name='Alice', age=25, email='alice@example.com')
#         conn = engine.connect()
#         conn.execute(insert_stmt)
#         conn.commit()
#         print("commit finish")
#         select_stmt = users.select()
#         result = conn.execute(select_stmt)
#         for row in result:
#             print(row)
#     except ClientError as e:
#         logger.error(f"ClientError occurred: {e.response['Error']['Message']}")
#         return {"error": e.response["Error"]["Message"]}
#     except Exception as e:
#         logger.error(f"Unexpected error occurred: {str(e)}")
#         return {"error": f"Internal Server Error: {e}"}
