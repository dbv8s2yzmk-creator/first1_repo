
# Завдання 2.
import random
def get_numbers_ticket(min, max,quantity):
        rand_list=[]
        if min>max:
               return rand_list
        if quantity>max-min+1:
               return rand_list
        if quantity <= 0 or min <= 0 or max <= 0:
                return rand_list
        for _ in range(quantity):
             num = random.randint(min, max)
             
             rand_list.append(num)
             if rand_list.count(num) > 1:
                    rand_list.remove(num)
                    while rand_list.count(num) > 0:
                           num = random.randint(min, max)
                           rand_list.append(num)
            
        return sorted(rand_list)

print(get_numbers_ticket(1,49,6))


