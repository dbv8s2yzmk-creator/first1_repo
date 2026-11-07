#Завдання 1. Модуль 4

from pathlib import Path

def total_salary(path):
    total = 0
    count = 0
    if Path(path).exists():
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
        if count == 0:
            return (0, 0)
    average = (int) (total / count )           
    return total, average
total,average = total_salary('/Users/admin/Documents/My_repo/first1_repo/example.txt')
print(f" Загальна заробінта плата: {total}, Середня заробітна плата: {average}")

#Завдання 2. Модуль 4
   
def get_cat_info(path):
    cat_info = []
    if Path(path).exists():
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cat = {
                    
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cat_info.append(cat)
    for cat in cat_info:
        print(cat)
    #return cat_info
print(get_cat_info('/Users/admin/Documents/My_repo/first1_repo/cats.txt'))   