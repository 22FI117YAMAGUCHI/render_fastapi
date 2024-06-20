from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "山田先生"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>こんにちは！Googleへのリンクを示します。</h1>
            <a href="https://www.google.co.jp/" title="Googleへ">ここを押してください</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def new_naming(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}


class Payment(BaseModel):
    amount_given: float
    price: float

@app.post("/pay")
async def calculate_change(payment: Payment):
    change = payment.amount_given - payment.price
    if change < 0:
        return {"response": "金額が不足しています。"}
    return {"response": f"代金を頂きました。お釣りは{change}円です。"}