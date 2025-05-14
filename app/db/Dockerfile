FROM python:3.12

ENV PYTHONPATH=/app/db

WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y unzip curl && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && ./aws/install && rm -rf awscliv2.zip ./aws

# Python依存ライブラリのインストール
COPY ./requirements.txt ./db/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./db/requirements.txt
# アプリケーションをコピー
COPY . /app/db
# ls で確認
RUN ls -la /app/db
CMD ["/app/db/entrypoint.sh"]
