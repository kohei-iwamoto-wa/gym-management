
### イメージのビルド

docker build -t gym-management-test-container .

### コンテナ起動

docker run -d --name gym-management-test-container -p 8000:80 gym-management-test-image

```
DynamoDbにテーブルを作成するコマンド
aws dynamodb create-table --table-name Users --attribute-definitions AttributeName=UserID,AttributeType=S --key-schema AttributeName=UserID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

```
DynamoDBのテーブルにデータを流し込む
aws dynamodb put-item --table-name Users --item "{\"UserID\":{\"S\":\"user123\"},\"Name\":{\"S\":\"Alice\"},\"Age\":{\"N\":\"30\"}}"
```
※ DynamoDB Localに対して実行する場合は、 `--endpoint-url http://localhost:8001` オプションを付与する必要がある。

