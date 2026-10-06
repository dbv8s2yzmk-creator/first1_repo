# Завдання 1.
from datetime import datetime
def get_days_from_today(date):
       try:
              date_time_object = datetime.strptime(date,'%Y-%m-%d')
              date_now = datetime.now()
              date_day = date_now - date_time_object
              return date_day.days
       except ValueError:
              print("Неправильний формат дати. Будь ласка, використовуйте YYYY-MM-DD.")
              return None
print(get_days_from_today("2020-10-09"))

# Завдання 2.

import random

def get_numbers_ticket(min, max,quantity):
        
        rand_list=[]
        if not 0 < min < max < 1000:
            return rand_list
        if not 0 < quantity < max - min + 1:
            return rand_list
        for _ in range(quantity):
             num = random.randint(min, max)
             
             rand_list.append(num)
             while rand_list.count(num) > 1:
                    rand_list.remove(num)
                    num = random.randint(min, max)
                    rand_list.append(num)
            
        return sorted(rand_list)


print(get_numbers_ticket(10,15,5))


