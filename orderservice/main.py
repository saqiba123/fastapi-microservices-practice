from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/order/{user_id}")
def place_order(user_id:str):
    user_url = f"http://localhost:8001/users/{user_id}"
    auth_url = f"http://localhost:8002/login/{user_id}"
    
    with httpx.Client() as client:
        user = client.get(user_url).json()
        token = client.get(auth_url).json()
        
        return {"user":user, "token":token["token"],"order_status":"created"}