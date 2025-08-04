import json
from writer import *

def reader_file():
    with open("data.json", "r") as f:
        data = json.load(f)
    for book in data['DataCenter']:
        try:
            book['relance']
        except :
            write_mail(book)
    # write_mail(data['DataCenter'][0])
    return

