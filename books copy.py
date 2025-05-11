'''
2. book.py
	2.1 하나의 클래스로 구성되며, 클래스 이름은 Book이다
	2.2 한 권의 책 정보는 책 제목, 저자, 출판일 그리고 ISBN으로 구성
	2.3 Book 클래스는 책을 대여하는 메소드 (book_rent)와 읽은 후 
	반납(book_return)하는 메소드를 가지며, 기타 더 필요한 기능이 
	있다면 추가해도 좋다
'''

import json, os

class Book:
    def __init__(self) :
        self.books = {} # 도서 목록 저장 할 변수 초기화
        self.load_books() # 현재 도서 목록 로드 함수 호출

    def load_books(self):
        file_path = './files/books.json'
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0 :
            with open(file_path, 'r', encoding="utf-8") as f:
                self.books = json.load(f)
        else :
            self.books = {}
        
        # 도서가 없을 경우
        if not self.books :
            print("책이 없습니다.")
        else :
            print("도서 목록 로드 완료.")
            
    def update_books(self):
        with open('./files/books.json', 'w', encoding="utf-8") as fw:
            json.dump(self.books, fw, indent=2, ensure_ascii=False)
    
    def book_rent(self, isbn):
        for book in self.books :
            if(book["isbn"] == isbn) :
                book["rented"] = True
                print(f"{book["title"]} 대출 완료.")
                break
        else :
            print("해당 도서를 찾을 수 없습니다.")
        self.update_books()
       
    def book_return(self, isbn):
        for book in self.books :
            if(book["isbn"] == isbn) :
                book["rented"] = False
                print(f"{book["title"]} 반납 완료.")
                break
        else:
            print("해당 도서를 찾을 수 없습니다.")

        self.update_books()

b = Book()
#b.book_rent("222-22-22-22222-2")
b.book_return("222-22-22-22222-2")
