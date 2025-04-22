from fastapi import FastAPI, HTTPException
from jose import jwt

app = FastAPI()

SECRET = "saqiba"
ALGORITHM ="HS256"

#>>>>>>>> api for login user and get token
@app.get("/login/{user_id}")
def login(user_id:str):
    token = jwt.encode({"user_id":user_id},SECRET,algorithm=ALGORITHM)
    return {"token":token}


@app.get("/verify")
def verify_user(token:str):
    try:
        data = jwt.decode(token,SECRET,algorithms=ALGORITHM)
        return {"data":data}
    except Exception as e:
        raise HTTPException(status_code=401,detail="Invalid token")