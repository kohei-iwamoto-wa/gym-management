
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
```
DynamoDBのデータを取得する。
aws dynamodb get-item --table-name Users --key "{\"UserID\":{\"S\":\"user123\"}}" --endpoint-url http://localhost:8000
```


※ DynamoDB Localに対して実行する場合は、 `--endpoint-url http://localhost:8001` オプションを付与する必要がある。



project-root/
│
├── app/                            # アプリケーション本体
│   ├── __init__.py
│   ├── models/                     # SQLAlchemy ORM モデル
│   │   ├── __init__.py
│   │   ├── base.py                 # Declarative Base定義
│   │   ├── user.py                 # users テーブル
│   │   └── ...                     # 他のテーブル定義
│   ├── db/                         # DB 接続・初期化処理
│   │   ├── __init__.py
│   │   └── engine.py               # SQLAlchemy エンジン作成ロジック
│   ├── services/                   # 業務ロジック層
│   └── main.py                     # エントリポイント（Flask / FastAPI など）
│
├── alembic/                        # Alembic 管理ディレクトリ
│   ├── versions/                   # マイグレーションファイルがここに保存される
│   ├── env.py                      # Alembic 環境設定（metadata を参照）
│   └── script.py.mako              # 自動生成テンプレート
│
├── migrations/                     # （任意）マイグレーション実行用スクリプト置き場
│   └── run_migrations.py
│
├── Dockerfile                      # ECS 用の Dockerfile
├── docker-compose.yml              # ローカル開発用（MySQLなど）
├── .env                            # 環境変数（ローカル用）
├── alembic.ini                     # Alembic 設定ファイル（DB URL）
├── requirements.txt                # ライブラリ定義
└── README.md


