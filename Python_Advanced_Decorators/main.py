import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from apps.logger import logger1, logger2

# Необходимо парсить страницу со свежими статьями (https://habr.com/ru/all/) и выбирать те статьи, в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта). Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы). Вывести в консоль список подходящих статей в
# формате: <дата> - <заголовок> - <ссылка>.

KEYWORDS = ['привет', 'код', 'web', 'python', 'API']

url = "https://habr.com"
habr_ru = "https://habr.com/ru/all"

content = requests.get(habr_ru, headers={'User-Agent': UserAgent().chrome})
soup = BeautifulSoup(content.text, 'html.parser')
posts = soup.find_all('article')

# 1 Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# 2 Написать декоратор из п.1, но с параметром – путь к логам.
# 3 Применить написанный логгер к приложению из любого предыдущего д/з.

path = 'Python_Advanced_Decorators/logs/log.txt'

@logger2(path)
@logger1
def habr_parser():
    for post in posts:
        preview_text = post.find(class_ = "tm-article-body tm-article-snippet__lead").text    
        if any(word in preview_text for word in KEYWORDS):
            publish_date = post.find(class_= "tm-article-snippet__datetime-published").text        
            title = post.find('h2').find('span').text        
            link = url + post.find(class_="tm-article-snippet__title-link").attrs['href']
            result = f'{publish_date} - {title} - {link}'            
    return result

if __name__ == '__main__':
    habr_parser()