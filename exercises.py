from faker import Faker
from operator import itemgetter
import requests
from bs4 import BeautifulSoup as bs


class Exercises:
    @staticmethod
    def ex_1(sort: str) -> list:
        fake = Faker('ru_RU')
        people_list = [{
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "phone_number": fake.phone_number()
        } for _ in range(100)]
        if sort == 'sort_by_first_name':
            people_list.sort(key=itemgetter('first_name'))
        elif sort == 'sort_by_last_name':
            people_list.sort(key=itemgetter('last_name'))
        else:
            people_list.sort(key=itemgetter('phone_number'))
        return people_list

    @staticmethod
    def ex_2(sort: str) -> list and int:
        page_link = 'https://libcat.ru/'
        response_page = requests.get(page_link)
        response_page_body = bs(response_page.content, 'html.parser')
        cards = response_page_body.find('div', {'id': 'dle-content'}).find_all('div', {'class': 'item'})
        books = []
        for card in cards:
            link = card.find('div', {'class': 'tg-booktitle'}).find('a')
            book_page_response = requests.get(link['href'])
            book_page = bs(book_page_response.content, 'html.parser')
            title_of_book = book_page.find('div', attrs={'itemprop': 'name'}).get_text()
            year_of_book = book_page.find('div', attrs={'itemprop': 'copyrightYear'}).get_text()
            author_of_book = book_page.find('a', attrs={'itemprop': 'author'}).get_text()
            summary_of_book = book_page.find('div', attrs={'itemprop': 'about'}).get_text()
            books_info = {
                'title': title_of_book,
                'year': year_of_book,
                'author': author_of_book,
                'summary': summary_of_book
            }
            books.append(books_info)
        if sort == 'sort_by_title_of_book':
            books.sort(key=itemgetter('title'))
        elif sort == 'sort_by_author_of_book':
            books.sort(key=itemgetter('author'))
        else:
            books.sort(key=itemgetter('year'))
        amount_of_books = len(books)
        return books, amount_of_books
