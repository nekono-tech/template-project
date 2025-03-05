# 変数定義
SHELL := /bin/bash

# デフォルトターゲット
.PHONY: help
help:
	@echo "使用可能なコマンド:"
	@echo "  make build       - Dockerイメージをビルドする"
	@echo "  make up          - コンテナを起動する"
	@echo "  make down        - コンテナを停止する"
	@echo "  make restart     - コンテナを再起動する"
	@echo "  make logs        - コンテナのログを表示する"
	@echo "  make shell       - Djangoコンテナにシェルで接続する"
	@echo "  make migrate     - マイグレーションを実行する"
	@echo "  make migrations  - マイグレーションファイルを作成する"
	@echo "  make showmigrations - マイグレーション状態を確認する"
	@echo "  make showmigrations-app - アプリケーションのマイグレーション状態を確認する"
	@echo "  make superuser   - スーパーユーザーを作成する"
	@echo "  make test        - テストを実行する"
	@echo "  make clean       - キャッシュファイルなどを削除する"
	@echo "  make setup       - 一連の操作をまとめて実行する"
	@echo "  make startapp    - 新しいアプリケーションを作成する"
	@echo "  make requirements - 依存関係を更新する"
	@echo "  make format      - コードを整形する"
	@echo "  make check       - コードをチェックする"
	@echo "  make fix         - コードを修正する"
	@echo "  make quality     - コード品質をチェックする"
	@echo "  make check-app   - アプリケーション別にコードをチェックする"
	@echo "  make check-errors - エラーレベル別にコードをチェックする"
	@echo "  make check-verbose - 詳細な結果を表示する"

# ビルド関連コマンド
.PHONY: build
build:
	export UID=$$(id -u) GID=$$(id -g) && \
	docker-compose build

.PHONY: up
up:
	export UID=$$(id -u) GID=$$(id -g) && \
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

.PHONY: restart
restart: down up

# コンテナ操作コマンド
.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: shell
shell:
	docker-compose exec web bash || docker-compose exec web sh

# Django関連コマンド
.PHONY: migrate
migrate:
	docker-compose exec web python manage.py migrate

.PHONY: migrations
migrations:
	docker-compose exec web python manage.py makemigrations

.PHONY: showmigrations
showmigrations:
	docker-compose exec web python manage.py showmigrations

.PHONY: showmigrations-app
showmigrations-app:
	@read -p "アプリ名を入力してください: " app_name; \
	docker-compose exec web python manage.py showmigrations $$app_name

.PHONY: superuser
superuser:
	docker-compose exec web python manage.py createsuperuser

.PHONY: collectstatic
collectstatic:
	docker-compose exec web python manage.py collectstatic --no-input

.PHONY: test
test:
	docker-compose exec web python manage.py test

# コード整形とリンティング用コマンド
.PHONY: format
format:
	docker-compose exec web ruff format .

.PHONY: check
check:
	docker-compose exec web ruff check .

.PHONY: fix
fix:
	docker-compose exec web ruff check --fix .

# 包括的なコード品質チェックコマンド
.PHONY: quality
quality: format fix check
	@echo "コード品質チェック完了"

# アプリケーション別チェック用コマンド
.PHONY: check-app
check-app:
	@read -p "チェックするアプリ名を入力してください: " app_name; \
	docker-compose exec web ruff check ./app/$$app_name

# エラーレベル別チェック用コマンド
.PHONY: check-errors
check-errors:
	docker-compose exec web ruff check . --select E

# 詳細な結果を表示するコマンド
.PHONY: check-verbose
check-verbose:
	docker-compose exec web ruff check . --verbose

# クリーンアップコマンド
.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "*.pyo" -delete
	find . -name "*.orig" -delete

# 一連の操作をまとめたコマンド
.PHONY: setup
setup: build up migrate

# アプリケーション作成コマンド
.PHONY: startapp
startapp:
	@read -p "アプリ名を入力してください: " app_name; \
	docker-compose exec web python manage.py startapp $$app_name

# 依存関係の更新
.PHONY: requirements
requirements:
	docker-compose exec web pip freeze > requirements.txt