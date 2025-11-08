from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI(title="Моё первое веб приложение")


@app.get("/")
def home():
    return "Hello world"

@app.get("/hello")
def html_hello():
    html = """
    <html>
        <head>
       
        </head>
        <body style="background-color: green; ">
            <h1>Hello world</h1>
            <p>Наша первая страница</p>
            <a href="http://localhost:8000/file">На страницу file</a>
        </body>
        
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/file")
def from_file():
    with open("templates/index.html", "r", encoding="utf-8") as fl:
        content = fl.read()
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) # Сервер автоматически перезагружается когда мы вносим изменения в коде