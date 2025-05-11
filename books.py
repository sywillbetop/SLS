'''
2. book.py
	2.1 하나의 클래스로 구성되며, 클래스 이름은 Book이다
	2.2 한 권의 책 정보는 책 제목, 저자, 출판일 그리고 ISBN으로 구성
	2.3 Book 클래스는 책을 대여하는 메소드 (book_rent)와 읽은 후 
	반납(book_return)하는 메소드를 가지며, 기타 더 필요한 기능이 
	있다면 추가해도 좋다
'''

import json

class Book:
    books = {}
    def get_books():
        global books
        with open('./files/books.json', 'r', encoding="utf-8") as f:
            books = json.load(f)
            print(books)
            
            # 도서가 없을 경우
            if not books :
                print("책이 없습니다.")
        
        with open('./files/books.json', 'w', encoding="utf-8") as fw:
            json.dump(books, fw, indent=2, ensure_ascii=False)
    
    get_books()
    
    def book_rent(isbn):
        result = [key for key, value in books.items() if value["isbn"] == isbn]
        print(result)
    
    book_rent("222-22-22-22222-2")
                
    
    def book_return():
        pass