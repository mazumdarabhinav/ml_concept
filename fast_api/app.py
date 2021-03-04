# Make a simple API with two endpoints

# Required Imports
import uvicorn
from fastapi import FastAPI

# Create App Object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "hello world"}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


@app.get("/{name}")
def get_name(name: str):
    return {"message": f"Hello, {name}"}


# Run the app through uvicorn.
# Will run on http://127.0.0.1:8000

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
