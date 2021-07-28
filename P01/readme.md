
# 常用Django指令

- 啟動網頁伺服器
python manage.py runserver 

- 開啟Jupyter
python manage.py shell_plus --notebook 

- 建立django project
django-admin.py startproject project-name

- 建立django app,依功能建立
python manage.py startapp fbCrawler

- 建立管理者
python manage.py createsuperuser

- 建立makemigrations檔,結尾接app名稱
python manage.py makemigrations xxx

- 執行資料庫migrate
python manage.py migrate

- 啟用python編輯器
python manage.py shell

- 啟用fastapi
uvicorn stock_fleets.wsgi:app --reload

- 啟用django-Q
python manage.py qcluster
