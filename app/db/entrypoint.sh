#!/bin/bash
set -e

# DBが起動するまで待機する（オプション）
# ここでは、DBが起動するまで待機するために、`wait-for-it` などのツールを使うことが一般的です
# wait-for-it.sh db:5432
# マイグレーションファイルの作成
alembic --config /app/db/alembic.ini revision --autogenerate -m "create initial tables"

ls -la
# Alembic マイグレーションを実行
alembic --config /app/db/alembic.ini upgrade head
# アプリケーションを起動
exec uvicorn db.main:app --host 0.0.0.0 --port 8090
