from pprint import pprint

from app.db import BaseModel

class Order(BaseModel):

    SHEET_NAME = "orders"

    COLUMNS = ["user_email", "book_id", "book_title", "book_author", "book_year"]

    SEEDS = []

if __name__ == "__main__":

    orders = Order.all()
    print("FOUND", len(orders), "ORDERS")
    for order in orders:
        pprint(dict(order))
