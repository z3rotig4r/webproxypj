from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_form():
    return '''
        <form method="post">
            URL: <input type="text" name="url">
            <input type="submit" value="Load">
        </form>
    '''

@app.post("/")
def load_url(url: str = Form(...)):
    try:
        response = requests.get(url)
        return HTMLResponse(content=response.content)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
