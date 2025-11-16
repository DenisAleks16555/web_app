from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse # Ответ перенаправлением на другую сьраницу
import uvicorn
from fastapi.templating import Jinja2Templates
from database.db import SessionLocal
from models.orders import Order
from models.products import Product

app = FastAPI(title="Моё первое веб приложение")

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def index(request: Request):
    context = {
        "request": request,
        "title": "Главная страница",
        "main_text": "Здесь будет текст для главной страницы с описаниием"
    }
    return templates.TemplateResponse("index.html", context=context)

@app.get("/about",response_class=HTMLResponse)
def about(request: Request):
    context = {
        "request": request,
        "title": "О нас",
        "people_count": 15,
        "mission": "Наша цель - помогать людям переходить дорогу"
    }
    return templates.TemplateResponse("about.html", context=context)

@app.get("/contacts",response_class=HTMLResponse)
def contacts(request: Request):
    context = {
        "request": request,
        "title": "Контакты",
        "adress": "Павловский Посад, ул. Павловская д. 26",
        "phone": "8 (800) 555-35-35",
        "email": "top@secret.com"
    }
    return templates.TemplateResponse("contacts.html", context=context)

@app.get("/orders",response_class=HTMLResponse)
def orders(request: Request):
    session = SessionLocal()
    data = session.query(Order).all()
    session.close()

    context = {
        "request": request,
        "title": "Заказы",
        "orders": data
        
    }
    return templates.TemplateResponse("orders.html", context=context)

@app.get("/orders/create",response_class=HTMLResponse)
def order_create(request: Request):
    session = SessionLocal()  
    data = session.query(Product).all()
    session.close()

    context = {
        "request": request,
        "title": "Создать заказ",
        "products": data   
    }
    return templates.TemplateResponse("order_create.html", context=context)


@app.post("/orders/create",response_class=RedirectResponse)
def order_create_data(
    customer_name: str = Form(...),
    phone_number: str = Form(...),
    product_id: int = Form(...),
    count: int = Form(...),
):
    session = SessionLocal()  
    new_order = Order(
        customer_name=customer_name,
        phone_number=phone_number,
        product_id=product_id,
        count=count
    )
    session.add(new_order)
    session.commit()
    session.close()

   
    return RedirectResponse("/orders/create", status_code=303)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) # Сервер автоматически перезагружается когда мы вносим изменения в коде