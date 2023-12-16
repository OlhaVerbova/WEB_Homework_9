""" 
Реалізуйте скрипт для пошуку цитат за тегом, за ім'ям автора або набором тегів. 
Скрипт виконується в нескінченному циклі і за допомогою звичайного оператора input
приймає команди у наступному форматі команда: значення.
Виведення результатів пошуку лише у форматі utf-8;
"""
from models import Authors, Qoutes

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pymongo import MongoClient

client = MongoClient("mongodb+srv://userweb17:567234@cluster0.x8roo9r.mongodb.net/hw9_1", ssl=True)
db = client["hw9_1"]


def find_qouotes_by_the_tag(value):    
    quotes_for_tag = list(db.qoutes.find({'tags':value}))    
    for quote in quotes_for_tag:
        return quote['quote']
    
def find_qouotes_by_the_tags(value):    
    list_of_tags = value.split(',')
    quotes_for_tags = list(db.qoutes.find({'tags': {'$in': list_of_tags}}))
    
    result = []
    for quote in quotes_for_tags:
        result.append(quote['quote'])    
    return result

def find_qouotes_by_the_author(value):    
    quotes_for_author = list(db.qoutes.find({'author': value})) 

    result = []    
    for quote in quotes_for_author:
        result.append(quote['quote'])    
    return result


def main():
    stop = "close"
    print("Hello! Enter commands in format'tag:live' or 'author:Albert Einstein' or 'tags:world, thinking'")    

    while True:
        user_input = input("--> ")

        if user_input == stop:
            break

        user_case, mongo_value = user_input.split(":", 1)

        match user_case:
            case "tag":
                sys.stdout.reconfigure(encoding='utf-8')
                print(find_qouotes_by_the_tag(mongo_value))    

            case "tags":
                sys.stdout.reconfigure(encoding='utf-8')
                print(find_qouotes_by_the_tags(mongo_value))    
            
            case "author":
                sys.stdout.reconfigure(encoding='utf-8')
                print(find_qouotes_by_the_author(mongo_value)) 
    

if __name__ == "__main__":
    main()