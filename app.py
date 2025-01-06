from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vercel!"

# Vercel 需要這個行來運行 Flask 應用
if __name__ == "__main__":
    app.run() 