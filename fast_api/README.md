# NOTES

## 1. Modern and Fast Web Framework for building API's

## 2. Steps to run an FAST API App:

`uvicorn app:app --reload`

The first app refers to the name of your Python file ( app.py) without the extension. The second app must be identical to how you named your FastAPI instance (app = FastAPI()). The -reload indicates that you want the API to automatically refresh as you save the file without restarting the entire thing.

## 3. Interactive documentation exploration

    `http://127.0.0.1:8000/docs`
    `http://127.0.0.1:8000/redoc `