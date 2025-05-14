'''
3. library.py
	3.1 하나의 클래스로 구성되며, 클래스 이름은 Library이다
	3.2 Library 클래스는 도서관에 신간 책을 추가하는 add_books, 
	오래된 책을 제거하는 remove_books, 대여 가능한 책들을 보여주는
	show_books_available, 책을 대여하는 rent, 그리고 책을 반납하는
	book_return 메소드들로 구성되며, 기타 다 필요하다고 생각되는 
	기능들은 추가하기 바란다.
'''
import json
import os
from book import Book


class Library:
	"""
	도서관 관리 클래스입니다.
	책 추가, 삭제, 대여, 반납, 대여 가능한 책 조회, 대여 랭킹 출력 등 
	도서관 운영에 필요한 주요 기능들을 제공합니다.
	"""
	def __init__(self, file_path="./files/books.json"):
		"""
		Library 객체를 초기화합니다.
		
		Args:
			file_path (str): 도서 정보를 저장하는 JSON 파일 경로 (기본값: "./files/books.json")
		"""
		self.file_path = file_path
		self.books = {}
		self.load_books()
	
	def load_books(self):
		"""
		저장된 JSON 파일에서 도서 정보를 불러와서 books 리스트를 초기화합니다.
		파일이 없거나 비어있으면 빈 리스트로 초기화합니다.
		"""
		if os.path.exists(self.file_path) and os.stat(self.file_path).st_size > 0 :
			with open(self.file_path, "r", encoding="utf-8") as f:
				data = json.load(f)
				self.books = [Book.from_dict(b) for b in data]
			print(self.books)
		else:
			self.books = {}
		
	def update_books(self):
		"""
		현재 books 리스트의 도서 정보를 JSON 파일에 저장합니다.
		"""
		with open(self.file_path, "w", encoding="utf-8") as f:
			json.dump([b.convert_dict() for b in self.books], f, indent=2, ensure_ascii=False)
	
	def draw_box(self, items):
			
		padding = 4
		max_title = max(len(b.title) for b in items)
		min_title = min(len(b.title) for b in items)
		max_author = max(len(b.author) for b in items)
		max_pub = max(len(b.published) for b in items)
		max_isbn = max(len(b.isbn) for b in items)

		max_width = [max_title, max_author, max_pub, max_isbn]

		print(f"{'─'*70}")
		print(f"{'No':<5}", end=' ')
		print(f"{'도서명':<{max_title}}", end=' ')
		print(f"{'':<{max_title+2}}{'저자':<{max_author}}", end=' ')
		print(f"{'':<{max_author+2}}{'출판일':<{max_pub}}", end=' ')
		print(f"{'':<{max_pub}}{'ISBN':<{max_isbn}}")
		print(f"{'─'*70}")
		
		isHead = False
		idx = 1
		for b in items:
			print(f"{idx:<5}", end=' ')
			idx+=1
			for i, item in enumerate([b.title, b.author, b.published, b.isbn]):
				pad = max_width[i]-len(item)
				width = (max_width[i]+pad) if max_width[i] != len(item) else (max_width[i]+pad+2)
				print(f"{item:<{width}}{' ':<{padding}}", end=' ')
			print()
		return items

	def add_books(self, book):
		"""
		새로운 책을 도서관에 추가하고 저장합니다.
		
		Args:
			book (Book): 추가할 Book 객체
		"""
		self.books.append(book)
		print(f"'{book.title}' 추가 완료.")
		self.update_books()
	
	def remove_books(self):
		"""
		책 목록을 번호로 보여주고, 선택된 책을 삭제합니다.
		삭제 후 JSON 파일을 갱신합니다.
		"""
		if not self.books:
			print("삭제할 도서가 없습니다.")
			return
		
		print("\n삭제할 도서를 선택하세요:")
		
		for i, b in enumerate(self.books, start=1):
			print(f"{i}. {b.title} ({b.author}) / {b.isbn}")
		
		while True:
			try:
				choice = int(input("번호 선택: "))
				if 1 <= choice <= len(self.books):
					removed_book = self.books.pop(choice - 1)
					print(f"'{removed_book.title}' 도서 삭제 완료.")
					self.update_books()
					break
				else:
					print("없는 번호입니다.")
			except ValueError:
				print("숫자만 입력해주세요.")
				
	
	def show_books_available(self):
		"""
		현재 대여 가능한 책 목록을 출력합니다.
		"""
		books_list = [b for b in self.books if not b.rented]
		available_books = self.draw_box(books_list)
		if not available_books:
			print("대여 가능한 도서가 없습니다.")
		
			
	
	def show_books_for_choose(self, forWhat):
		"""
		대여 또는 반납을 위해 선택 가능한 책 목록을 출력하고 사용자가 선택한 책을 반환합니다.
		
		Args:
			forWhat (str): "rent"이면 대여 가능한 책, "return"이면 대여 중인 책 목록을 보여줌
		
		Returns:
			Book: 사용자가 선택한 Book 객체
		"""
		if forWhat == "rent":
			books_list = [b for b in self.books if not b.rented]
		elif forWhat == "return":
			books_list = [b for b in self.books if b.rented]
		else:
			books_list = []
		
		#for i, b in enumerate(books_list, start=1):
		#	print(f"{i}. {b.title} ({b.author}) / {b.isbn}")
		if not books_list:
			print("목록이 없습니다.")
			return
		
		self.draw_box(books_list)
		while True:
			try:
				sel = int(input("번호 선택: "))
				if 1<= sel <= len(books_list):
					return books_list[sel-1]
				else:
					print("없는 번호 입니다.")
			except ValueError:
				print("숫자만 입력해주세요.")
    
	def show_books_most_rented(self):
		"""
		대여 횟수 기준 상위 5권의 책을 랭킹 형식으로 출력합니다.
		"""
		rank = sorted(self.books, key=lambda b: b.rent_count, reverse=True)
		print(f"{'。':>13}{'。':>4}{'。':>4}")
		print(f"{'│＼':>14}{'／':>1}{'＼':>2}{'／│':>1}")
		print(f"{'│':>13}{'│':>10}")
		print(f"{'대여 랭킹 TOP 5':>21}")   
		print(f"{'└':>13}{'─'*9}┘")
		print("-" * 60)
  
		print(f"{'─'*95:>14}")
		print(f"{'순위':>5}{'│':>3}{'도서명':>20}{'│':>17}{'저자':>13}{'│':>12}{'대여 횟수':>10}")
		print(f"{'─'*95:>14}")
		
		for idx, book in enumerate(rank[:5], start=1):
			print(f"{idx:>5}{book.title:>11}{book.author:>35}{book.rent_count:>21}")
		print("-" * 60)

	
	def rent(self, isbn):
		"""
		ISBN에 해당하는 책을 대여 처리합니다.
		이미 대여 중인 경우 안내 메시지를 출력합니다.
		대여 성공 시 대여 횟수를 증가시키고 저장합니다.
		
		Args:
			isbn (str): 대여할 책의 ISBN 번호
		"""
		for b in self.books:
			if b.isbn == isbn:
				if not b.rented:
					b.book_rent()
					b.rent_count += 1
					self.update_books()
				else:
					print("이미 대출 중입니다.")
				return
		
	def book_return(self, isbn):
		"""
		ISBN에 해당하는 책을 반납 처리합니다.
		이미 반납된 책인 경우 안내 메시지를 출력합니다.
		반납 성공 시 대여 횟수를 증가시키고 저장합니다.
		
		Args:
			isbn (str): 반납할 책의 ISBN 번호
		"""
		for b in self.books:
			if b.isbn == isbn:
				if b.rented:
					b.book_return()
					b.rent_count += 1
					self.update_books()
				else:
					print("이미 반납되어있습니다.")
				return

	def book_search(self):
		"""
		도서명 또는 저자명 기준으로 책을 검색하여 결과를 출력합니다.
		
		Args:
			type (str): "1"이면 도서명 기준, 그 외는 저자명 기준 검색
			keyword (str): 검색할 키워드 문자열
		"""
		print("\n검색할 항목을 선택해주세요.")
		while True:
			try:
				type = int(input("1. 제목 / 2. 저자: "))
				if 1<=type<=2:
					if not (type == 1 or type == 2):
						print("없는 번호입니다.")
						continue
					keyword = input("검색어: ")
					if len(keyword.strip()) == 0:
						print("검색어를 입력해주세요.")
						continue
					
					books_list = [b for b in self.books if(str(b.title if type==1 else b.author).find(keyword) != -1)]
					if not books_list:
						print("목록이 없습니다.")
						break
					
					self.draw_box(books_list)

				else :
					print("없는 번호 입니다.")
				break
			except ValueError:
				print("숫자만 입력해주세요.")

	
	
			
			

