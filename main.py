from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "message": "ကျွန်ုပ်၏ Cloud Server အဆင်သင့်ဖြစ်နေပါပြီ။ နောက်မှ ကုဒ်များ ထပ်ထည့်နိုင်ပါသည်။"
    }
