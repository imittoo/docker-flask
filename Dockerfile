FROM python:3.6.4

# 安装依赖
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -i https://pypi.doubanio.com/simple --disable-pip-version-check -r requirements.txt

# 拷贝应用文件
COPY . /usr/src/app

CMD ["gunicorn", "-c", "gunicorn.py", "manager:app"]
