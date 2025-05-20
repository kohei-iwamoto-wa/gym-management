import os
from dotenv import load_dotenv
load_dotenv()

from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig

# Alembic Config オブジェクト取得
config = context.config

# alembic.ini にあるロギング設定を反映
fileConfig(config.config_file_name)

# 環境変数から DB URL を取得して、alembic.ini の設定を上書き
config.set_main_option('sqlalchemy.url', 'mysql+pymysql://admin:admin@local-aurora-mysql:3306/gym_db')

# モデルの Base を import
import sys
import os
sys.path.append(os.path.dirname(__file__))

print("現在のカレントディレクトリ")
print(os.getcwd())
print("---------------------------------")

files = os.listdir()
print("現在のディレクトリ内のファイル一覧:")
for f in files:
    print(f)
print("---------------------------------")

from models import Base, User, Bukken, Kukaku

target_metadata = Base.metadata

print("target_metadata", target_metadata)