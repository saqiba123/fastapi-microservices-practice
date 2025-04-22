from fastapi import FastAPI, HTTPException, Depends
from jose import jwt

#for getting jwt token  1st is secret key and another is alogirhtim
SECRET_KEY="saqiba"
ALGORITHM ="HS256"

app = FastAPI()

@app.get("/login/{user_id}")
def login(user_id:str):
    token = jwt.encode({"user_id":user_id},SECRET_KEY,algorithm=ALGORITHM)
    return {"token":token}

@app.get("/verify")
def verify_token(token:str):
    try:
        #do something
        data = jwt.decode(token, SECRET_KEY,algorithms=ALGORITHM)
        return {"valid":True,"data":data}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401,detail="invalid token")