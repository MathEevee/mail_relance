from reader import *
import datetime as dt
from parser import *

def write_mail(data):
    # print(data['first contact'])
    current_date = dt.date.today()
    current_date_string = current_date.strftime("%d-%m-%Y")
    parse_date(data['first contact'], current_date_string)
    
    return