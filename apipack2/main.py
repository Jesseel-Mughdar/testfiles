from fastapi import FastAPI
import uvicorn
from testapi.Fibo import Fibonacci
app = FastAPI()
list =[]
@app.get("/")
def root():
    return{"message: hello world"}

@app.get("/getitem/{n}")
def inp(n:int):
    user_saved = Fibonacci(n)
    return user_saved
                  


if __name__=='__main__':
    uvicorn.run(app)      