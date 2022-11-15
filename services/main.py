import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
        <body>
            <h1>Su red está siendo atacada</h1>
            <p>Estado de la red: Inactiva</p>
            <p>Tipo de Ataque: DDOS</p>
            <p>Sistemas comprometidos: 192.168.1.14, 192.168.1.15, 192.168.1.15"</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app)
    # uvicorn.run(app, host="0.0.0.0", port=80)
