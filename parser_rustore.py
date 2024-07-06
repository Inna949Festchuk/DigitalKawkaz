# # Программа на Python, которая распарсит все страницы сайта https://www.rustore.ru/
# # с помощью библиотеки BeautifulSoup4 и сохранением результат в единый файл .txt

# # Получаем HTML-код основной страницы.
# # Находим все ссылки на остальные страницы из тега <aside>.
# # Переходим по каждой ссылке и распарсиваем страницу по тегу <article>.
# # Отдельно находим ссылки на изображения из тега <img>
# # Объединяем результаты парсинга и сохраняем их в файл.

# import requests
# from bs4 import BeautifulSoup
# import time

# # Функция для парсинга одной страницы и получения данных и ссылок на новые страницы
# def parse_page(url):
#     # - - - - - - - - - - - - - - - - - - - - - - - - - -
#     # ФИШКА 1: Обеспечение безопасности приложения за счет проверки сертификатов шифрования SSL/TLS сайта для парсинга,
#     # а для исключения перегрузки сайта для парсинга запросами искусственно добавленно время задержки 
#     # для обработки каждой страницы по-умолчанию равное 0.5 секунды, которое можно регулировать
#     # - - - - - - - - - - - - - - - - - - - - - - - - - -
#     try:
        
#         # Включение проверки сертификата является важным шагом для обеспечения безопасности 
#         # вашего приложения при работе с HTTPS-сайтами. Это поможет защитить ваше приложение 
#         # от атак и обеспечить конфиденциальность данных.
#         # Включить проверку сертификата, установив параметр verify=True
#         response = requests.get(url, verify=True)
#         response = requests.get(url)
#         response.encoding = 'utf-8'  # Устанавливаем кодировку ответа на utf-8
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Сохранение заголовков и параграфов страницы в список
#         data = []
#         data.append(soup.title.text)

#         header = soup.find('header')
#         if header:
#             data.append(header.text)

#         article = soup.find('article')
#         if article:
#             data.append(article.text)

#             # - - - - - - - - - - - - - - - - - - - - - - - - - -
#             # ФИШКА 2: При парсинге извлекается не только текстовая информация, но и 
#             # ссылки на изображения сайта, что не мало важно для понимания инструкций представленных на сайте
#             # - - - - - - - - - - - - - - - - - - - - - - - - - -

#             # Ищем все теги <img> внутри <article> и сохраняем ссылки на изображения
#             images = article.find_all('img')
#             for img in images:
#                 img_src = img['src']
#                 if img_src.startswith('/'):
#                     img_src = 'https://www.rustore.ru' + img_src
#                 data.append(f"Image: {img_src}")

#         # Ищем все ссылки в теге aside и добавляем их в список ссылок
#         aside_links = soup.find_all('aside')
#         links = []
#         for aside in aside_links:
#             for a in aside.find_all('a', href=True):
#                 href = a['href']
#                 # Конструируем полный URL ссылки и добавляем в список
#                 if href.startswith('/'):
#                     href = 'https://www.rustore.ru' + href
#                 links.append(href)

#         return data, links
    
#     # В функции parse_page добавлена обработка исключений requests.exceptions.SSLError и общего Exception. 
#     # Если возникает ошибка SSL, программа возвращает пустые списки data и links. 
#     # Это позволит программе продолжить работу, даже если возникнут проблемы с SSL/TLS соединением на некоторых страницах.

#     except requests.exceptions.SSLError as e:
#         print(f"SSL Error occurred for URL: {url}")
#         print(e)
#         return [], []
#     except Exception as e:
#         print(f"Error occurred for URL: {url}")
#         print(e)
#         return [], []
    
# # Основная функция для парсинга сайта и сохранения результатов в файл
# def parse_website(start_urls, output_file, timeout=0.5):
#     parsed_urls = set()  # Используем множество для хранения уникальных URL
#     urls_to_parse = start_urls[:]  # Создаем копию списка start_urls
#     all_data = []

#     # Цикл для обработки всех ссылок
#     while urls_to_parse:
#         url = urls_to_parse.pop(0)
#         if url not in parsed_urls:
#             print(f"Парсим страницу: {url}")
#             page_data, new_links = parse_page(url)
#             all_data.extend(page_data)  # Добавляем данные страницы в общий список
#             urls_to_parse.extend(new_links)
#             parsed_urls.add(url)
#             time.sleep(timeout)  # Добавляем задержку, чтобы не перегружать сервер

#     # Сохраняем все данные в файл
#     with open(output_file, 'w', encoding='utf-8') as file:
#         for line in all_data:
#             file.write(line + '\n')

# # Список стартовых страниц
# start_urls = [
#     'https://www.rustore.ru/help/users/',
#     'https://www.rustore.ru/help/developers/',
#     'https://www.rustore.ru/help/sdk/',
#     'https://www.rustore.ru/help/work-with-rustore-api/',
#     'https://www.rustore.ru/help/guides/'
# ]

# # Имя выходного файла
# output_file = 'parsed_data.txt'

# # Запуск парсинга сайта
# parse_website(start_urls, output_file, timeout=0.1)


# - - - - - - - - - - - - - - - - - - - - - - - - - -
# версия 2
# - - - - - - - - - - - - - - - - - - - - - - - - - -

# Программа на Python, которая распарсит все страницы сайта https://www.rustore.ru/
# с помощью библиотеки BeautifulSoup4 и сохранением результата в единый файл .md

# Получаем HTML-код основной страницы.
# Находим все ссылки на остальные страницы из тега <aside>.
# Переходим по каждой ссылке и распарсиваем страницу по тегу <article>.
# Отдельно находим ссылки на изображения из тега <img>
# Объединяем результаты парсинга и сохраняем их в файл.

import requests
from bs4 import BeautifulSoup
import time

# Функция для парсинга одной страницы и получения данных и ссылок на новые страницы
def parse_page(url):
    try:
        # Включение проверки сертификата является важным шагом для обеспечения безопасности 
        # вашего приложения при работе с HTTPS-сайтами. Это поможет защитить ваше приложение 
        # от атак и обеспечить конфиденциальность данных.
        # Включить проверку сертификата, установив параметр verify=True
        response = requests.get(url, verify=True)
        response.encoding = 'utf-8'  # Устанавливаем кодировку ответа на utf-8
        soup = BeautifulSoup(response.text, 'html.parser')

        # Сохранение заголовков и параграфов страницы в список
        data = []
        data.append(f"# {soup.title.text}")

        h1 = soup.find('h1')
        if h1:
            data.append(f"# {h1.text}")

        header = soup.find('header')
        if header:
            data.append(f"## {header.text}")

        h2 = soup.find('h2')
        if h2:
            data.append(f"## {h2.text}")

        article = soup.find('article')
        tables = article.find_all('table')
        if article and not tables:
            data.append(article.text)

            # Ищем все теги <img> внутри <article> и сохраняем ссылки на изображения
            images = article.find_all('img')
            for img in images:
                img_src = img['src']
                if img_src.startswith('/'):
                    img_src = 'https://www.rustore.ru' + img_src
                
                # Находим ближайший заголовок <h2> и используем его текст в качестве подписи
               
                if h2:
                    img_caption = h2.text.strip()
                else:
                    img_caption = "Image"
                
                data.append(f"![{img_caption}]({img_src})")
        
        if article and tables:

            # Ищем все параграфы внутри <article>
            paragraphs = article.find_all('p')
            for p in paragraphs:
                data.append(p.text.strip())

            # Ищем все списки внутри <article>
            lists = article.find_all(['ul', 'ol'])
            for lst in lists:
                data.append("\n")
                for li in lst.find_all('li'):
                    data.append(f"- {li.text.strip()}")
                data.append("\n")

            
            # Ищем все таблицы внутри <article> и преобразуем их в формат Markdown
            
            for table in tables:
                data.append("\n")
                data.append("| " + " | ".join([th.text.strip() for th in table.find_all('th')]) + " |")
                data.append("| " + " | ".join(["---"] * len(table.find_all('th'))) + " |")
                for row in table.find_all('tr'):
                    cells = [td.text.strip() for td in row.find_all('td')]
                    data.append("| " + " | ".join(cells) + " |")
                data.append("\n")


            # Ищем все теги <img> внутри <article> и сохраняем ссылки на изображения
            images = article.find_all('img')
            for img in images:
                img_src = img['src']
                if img_src.startswith('/'):
                    img_src = 'https://www.rustore.ru' + img_src
                
                # Находим ближайший заголовок <h2> и используем его текст в качестве подписи
               
                if h2:
                    img_caption = h2.text.strip()
                else:
                    img_caption = "Image"
                
                data.append(f"![{img_caption}]({img_src})")

        # Ищем все ссылки в теге aside и добавляем их в список ссылок
        aside_links = soup.find_all('aside')
        links = []
        for aside in aside_links:
            for a in aside.find_all('a', href=True):
                href = a['href']
                # Конструируем полный URL ссылки и добавляем в список
                if href.startswith('/'):
                    href = 'https://www.rustore.ru' + href
                links.append(href)

        return data, links
    
    except requests.exceptions.SSLError as e:
        print(f"SSL Error occurred for URL: {url}")
        print(e)
        return [], []
    except Exception as e:
        print(f"Error occurred for URL: {url}")
        print(e)
        return [], []
    
# Основная функция для парсинга сайта и сохранения результатов в файл
def parse_website(start_urls, output_file, timeout=0.5):
    parsed_urls = set()  # Используем множество для хранения уникальных URL
    urls_to_parse = start_urls[:]  # Создаем копию списка start_urls
    all_data = []

    # Цикл для обработки всех ссылок
    while urls_to_parse:
        url = urls_to_parse.pop(0)
        if url not in parsed_urls:
            print(f"Парсим страницу: {url}")
            page_data, new_links = parse_page(url)
            all_data.extend(page_data)  # Добавляем данные страницы в общий список
            urls_to_parse.extend(new_links)
            parsed_urls.add(url)
            time.sleep(timeout)  # Добавляем задержку, чтобы не перегружать сервер

    # Сохраняем все данные в файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in all_data:
            file.write(line + '\n')

# Список стартовых страниц
start_urls = [
    'https://www.rustore.ru/help/users/',
    'https://www.rustore.ru/help/developers/',
    'https://www.rustore.ru/help/sdk/',
    'https://www.rustore.ru/help/work-with-rustore-api/',
    'https://www.rustore.ru/help/guides/'
]

# Имя выходного файла
output_file = 'parsed_data.md'

# Запуск парсинга сайта
parse_website(start_urls, output_file, timeout=0.5)
 
