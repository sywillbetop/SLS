'''
2. book.py
	2.1 하나의 클래스로 구성되며, 클래스 이름은 Book이다
	2.2 한 권의 책 정보는 책 제목, 저자, 출판일 그리고 ISBN으로 구성
	2.3 Book 클래스는 책을 대여하는 메소드 (book_rent)와 읽은 후 
	반납(book_return)하는 메소드를 가지며, 기타 더 필요한 기능이 
	있다면 추가해도 좋다
'''

class Book:
    def __init__(self, title, author, published, isbn, rented=False, rent_count=0) :
        self.title = title
        self.author = author
        self.published = published
        self.isbn = isbn
        self.rented = rented
        self.rent_count = rent_count
    
    def __str__(self):
        return f"{self.title} / {self.author} / {self.published} / {self.isbn} / {'대출중' if self.rented else '대여가능'}"
    
    def book_rent(self):
        self.rented = True
        print(f"{self.title} 대출 완료되었습니다.")
        
    def book_return(self):
        self.rented = False
        print(f"{self.title} 반납 완료되었습니다.")
        
    # 추후 json으로 책 정보 저장 하기 위해 딕셔너리를 변환해주는 메소드
    def convert_dict(self):
        return {
            "title"     : self.title,
            "author"    : self.author,
            "published" : self.published,
            "isbn"      : self.isbn,
            "rented"    : self.rented,
            "rent_count" : self.rent_count
        }
    
    @staticmethod
    def from_dict(data):
        return Book (
            title=data["title"],
            author=data["author"],
            published=data["published"],
            isbn=data["isbn"],
            rented=data["rented"],
            rent_count=data["rent_count"]
        )

