from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return{"message: hello world"}

@app.get("/item/{n}")
def Fibonacci(n: int):
    count = 0
    nterms = 10
    n1 = 0
    n2 = 1
    l=[]
    while count < n:

        l.append(n1)
        nth = n1 + n2
       # update values
        n1 = n2
        n2 = nth
        count += 1
    return l 
if __name__ == '__main__':
    uvicorn.run(app)   