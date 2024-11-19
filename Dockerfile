# 使用python映像
FROM python:3.9-slim


# 設置工作目錄
WORKDIR /app


# 複製當前目錄下的所有文件到容器的工作目錄
COPY . /app

# 安裝應用所需的 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放容器端口
EXPOSE 5000

# 定義容器啟動時執行的指令
CMD ["python", "app.py"]
