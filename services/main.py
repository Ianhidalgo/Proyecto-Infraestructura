import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "Su red está siendo atacada"
    }

if __name__ == "__main__":
    uvicorn.run(app)
