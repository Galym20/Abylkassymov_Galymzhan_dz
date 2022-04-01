from requests import get
from decimal import *

response = get('http://www.cbr.ru/scripts/XML_daily.asp').text

def currency_rates(val_name):

    if val_name in response:
        value = response[response.find('<Value>', response.find(val_name)) + 7:response.find('</Value>', response.find(val_name))]
        return f"{Decimal(value.replace(',', '.'))} "
    else:
        return None

print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('AAA'))
