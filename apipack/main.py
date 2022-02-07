from fastapi import FastAPI
import uvicorn
from testapi.Fibo import Fibonacci
app = FastAPI()

@app.get("/")
def root():
    return{"message: hello world"}

@app.get("/item/{n}")
async def inp(n:int):
    user_saved = Fibonacci(n)
    return user_saved
if __name__=='__main__':
    uvicorn.run(app)      