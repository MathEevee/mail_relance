import json
from writer import *

def reader_file():
    with open("data.json", "r") as file:
        data = json.load(file)

    for book in data['DataCenter']:
        if 'relance' not in book:
            write_mail(book, data)

    return

