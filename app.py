from flask import Flask
from langflow import LangFlow  # 假設 LangFlow 是這樣導入的

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vercel!"

@app.route('/langflow')
def langflow():
    return LangFlow()  # 假設 LangFlow 是一個可以直接調用的函數

# Vercel 需要這個行來運行 Flask 應用
if __name__ == "__main__":
    app.run() 