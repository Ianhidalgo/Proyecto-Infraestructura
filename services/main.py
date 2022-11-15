import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "Su red está siendo atacada"
        "Estado de la red": "Inactiva"
        "Tipo de Ataque:" "DDOS"
        "Sistemas comprometidos:" "192.168.1.14, 192.168.1.15, 192.168.1.15"
    }

if __name__ == "__main__":
    uvicorn.run(app)
