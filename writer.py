from reader import *
import datetime as dt
from parser import *
import json

def send_mail(book, today):
    parser_mail(book)
    print(f"Relance ajoutée pour {book.get('entreprise', 'Inconnu')} le {today}")
    return

def write_mail(book, full_data):
    current_date = dt.datetime.today()
    days_send_relance = dt.datetime.strptime(book['first contact'], "%d-%m-%Y")

    if current_date.date() >= (days_send_relance + dt.timedelta(days=10)).date():
        create_send_relance(book, full_data)

def create_send_relance(book, full_data):
    if book.get('contact') or book.get('mail'):
        if book.get('plateforme') != "linkedin" or not book.get('plateforme'):
            today_str = dt.datetime.today().strftime("%d-%m-%Y")
            book['relance'] = today_str
            with open("data.json", "w") as file:
                json.dump(full_data, file, indent=4)
            if book.get('mail'):
                send_mail(book, today_str)
            else:
                contact_phone(book)
    return