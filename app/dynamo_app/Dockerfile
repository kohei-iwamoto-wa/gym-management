FROM python:3.12

WORKDIR /code

ENV PYTHONPATH=/code/app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y unzip curl && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && ./aws/install && rm -rf awscliv2.zip ./aws

# 依存ライブラリのインストール
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# アプリケーションのコードだけコピー
COPY ./app /code/app

RUN ls -la
RUN ls -la app

# FastAPI 起動
CMD ["uvicorn", "dynamo_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
