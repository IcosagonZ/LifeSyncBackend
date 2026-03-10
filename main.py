from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "OK",
        "version": "0.1.0"
    }

@app.get("/client/version/{client_version}")
def read_client_version(client_version: str | None = None):
    print("Client > Version {}".format(client_version))
    return {
        "status": "OK",
        "version": "0.1.0"
    }
