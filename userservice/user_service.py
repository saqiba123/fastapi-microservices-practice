from fastapi import FastAPI

app =FastAPI()

fake_user_db = {
    "1":{"id":1,"name":"saqiba"},
    "2":{"id":2,"name":"hina"}
}

@app.get("/")
def hello_world():
    return "hello world!"


@app.get("/users/{user_id}")
def get_user(user_id:str):
    return fake_user_db.get(user_id,{"error":"Not found!"})