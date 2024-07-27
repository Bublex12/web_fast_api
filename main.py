import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/items/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
