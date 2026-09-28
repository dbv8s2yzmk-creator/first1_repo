# Завдання 1.
from datetime import datetime

def get_days_from_today(date):
       try:
             date_time_object = datetime.strptime(date, '%Y-%m-%d')
             date_now = datetime.now()
             date_day = date_now - date_time_object
             return date_day.days
       except ValueError:
              print ("Неправильний формат дати. Використовуйте формат YYYY-MM-DD")
              return None
print(get_days_from_today('2020-10-09'))
# Завдання 2.
import random
def get_numbers_ticket(min, max,quantity):
        rand_list=[]
        for _ in range(quantity):
             num = random.randint(min, max)
             #num = int(num)
             rand_list.append(num)
            #print (f"{num:.0f}")
        return rand_list

print(get_numbers_ticket(1,49,6))


