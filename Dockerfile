FROM python:3.13

WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ホストのユーザーIDとグループIDを指定するための引数
ARG UID=1000
ARG GID=1000

# ユーザーとグループを作成
RUN groupadd -g ${GID} appuser || groupmod -o -g ${GID} appuser || true
RUN useradd -u ${UID} -g ${GID} -s /bin/bash -m appuser || usermod -o -u ${UID} appuser || true

# Python 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリの所有者を変更
RUN mkdir -p /app/media /app/static && \
    chown -R appuser:appuser /app

# ユーザーを変更
USER appuser

# ポート設定
EXPOSE 8888

# 起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]