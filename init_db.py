from database.db import Base, SessionLocal, engine
from models.orders import Order
from models.products import Product


def init_database():
    Base.metadata.drop_all(bind=engine) # Удалить все таблички из базы данных
    Base.metadata.create_all(bind=engine) # Создать все таблички в базе данных

    # Будем заполнять таблички примерами
    session = SessionLocal() # Создали подключение к базе данных

 # Как добавлять одну строчку
    p1 = Product(name = "Молоко 1л", price=85, count=15)
    session.add(p1)

     # Как добавить несколько  записей
    lst = [
        Product(name = "Хлеб", price=25, count=5),
        Product(name = "Гречка", price=85, count=56),
        Product(name = "Сахар", price=60, count=50)
    ]

    session.add_all(lst)
    session.commit()


    lst2 = [
        Order(
        customer_name="Петя",
        phone_number="89991112233",
        product_id=1,
        count=5),


        Order(
        customer_name="Вася",
        phone_number="80001112246",
        product_id=2,
        count=7),

        Order(
        customer_name="Иван",
        phone_number="89991112233",
        product_id=3,
        count=9)
    ]

    session.add_all(lst2)
    session.commit()

    session.close()

if __name__ == "__main__":
    init_database()