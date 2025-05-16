class Book:
    """
    도서 정보를 관리하는 클래스.

    Attributes:
        title (str): 도서명
        author (str): 저자
        published (str): 출판일
        isbn (str): 국제 표준 도서번호 (숫자 xxx-xx-xxxx-xxxx-x)
        rented (bool): 대여 여부
        rent_count (int): 대여 횟수
    """

    def __init__(self, title, author, published, isbn, rented=False, rent_count=0):
        """
        Book 객체를 초기화합니다.

        Args:
            title (str): 도서명
            author (str): 저자
            published (str): 출판일
            isbn (str): 국제 표준 도서번호
            rented (bool, optional): 대여 여부. 기본값은 False.
            rent_count (int, optional): 대여 횟수. 기본값은 0.
        """
        self.title = title
        self.author = author
        self.published = published
        self.isbn = isbn
        self.rented = rented
        self.rent_count = rent_count

    def book_rent(self):
        """도서를 대여 처리합니다."""
        self.rented = True

    def book_return(self):
        """도서 반납 처리합니다."""
        self.rented = False

    def convert_dict(self):
        """도서 정보를 딕셔너리 형태로 변환합니다.

        Returns:
            dict: 도서 정보가 담긴 딕셔너리
        """
        return {
            "title": self.title,
            "author": self.author,
            "published": self.published,
            "isbn": self.isbn,
            "rented": self.rented,
            "rent_count": self.rent_count
        }

    @staticmethod
    def from_dict(data):
        """
        딕셔너리 데이터를 바탕으로 Book 객체를 생성합니다.

        Args:
            data (dict): 도서 정보가 담긴 딕셔너리

        Returns:
            Book: 생성된 Book 객체
        """
        return Book(
            title=data["title"],
            author=data["author"],
            published=data["published"],
            isbn=data["isbn"],
            rented=data["rented"],
            rent_count=data["rent_count"]
        )
