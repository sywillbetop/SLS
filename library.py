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
		self.books = []
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
	
	def draw_books(self, items, isRanking=False):
		if not items:
			warn("! 데이터가 없습니다 !")
		
		max_title = max(len(b.title) for b in items)
		max_author = max(len(b.author) for b in items)
		max_pub = max(len(b.published) for b in items)
		max_isbn = max(len(b.isbn) for b in items)

		max_width = [max_title, max_author, max_pub, max_isbn]
		
		normal(f"{'─'*90}")
		print(f"{('순위' if isRanking else 'No'):<5}", end=' ')
		print(f"{'도서명':<{max_title}}", end=' ')
		print(f"{'':<{max_title+2}}{'저자':<{max_author}}", end=' ')
		print(f"{'':<{max_author+2}}{'출판일':<{max_pub}}", end=' ')
		print(f"{'':<{max_pub}}{'ISBN':<{max_isbn}}")
		print(f"{'─'*90}")
		
		idx = 1
		for b in items:
			if isRanking:
				print(f"\033[{91 if idx==1 else 0}m{idx:<5}", end=' ')
			else:
				print(f"\033[0m{idx:<5}", end=' ')
			idx+=1
			for i, item in enumerate([b.title, b.author, b.published, b.isbn]):
				if i==0:
					print(f"{item:<{max_width[i]}}", end=' ')
				else:
					pad = max_width[i]-len(item)
					print(f"{' ':>{len(item)+pad}}{item:<{max_width[i]}}", end=' ')
			print()
		return items

	def show_books_available(self):
		"""
		현재 대여 가능한 도서 목록을 출력합니다.
		"""
		info("↓ 현재 대여 가능한 도서 목록입니다 ↓")
  
		books_list = [b for b in self.books if not b.rented]
		available_books = self.draw_books(books_list)
		if not available_books:
			warn("※ 대여 가능한 도서가 없습니다. ※")
			return False

		
	def show_books_for_choose(self, forWhat):
		"""
		대여 또는 반납을 위해 선택 가능한 책 목록을 출력하고 사용자가 선택한 책을 반환합니다.
		
		Args:
			forWhat (str): "rent"이면 대여 가능한 책, "return"이면 대여 중인 책 목록을 보여줌
		
		Returns:
			Book: 사용자가 선택한 Book 객체
		"""
		info(f"↓ {'대여' if forWhat=="rent" else '반납'}하실 도서의 번호를 선택해주세요. ↓")

		if forWhat == "rent":
			books_list = [b for b in self.books if not b.rented]
		elif forWhat == "return":
			books_list = [b for b in self.books if b.rented]
		else:
			books_list = []
		
		if not books_list:
			warn(f"※ {'대여' if forWhat=="rent" else '반납'}할 도서가 없습니다. ※")
			return
		
		self.draw_books(books_list)
		while True:
			try:
				answer("번호 선택:")
				sel = int(input())
				if 1<= sel <= len(books_list):
					return books_list[sel-1]
				else:
					warn("!! 없는 번호 입니다 !!")
			except ValueError:
				warn("!! 숫자만 입력해주세요 !!")
    
	def rent(self):
		"""
		ISBN에 해당하는 책을 대여 처리합니다.
		이미 대여 중인 경우 안내 메시지를 출력합니다.
		대여 성공 시 대여 횟수를 증가시키고 저장합니다.
		"""
		selected = self.show_books_for_choose("rent")
		if selected:
			for b in self.books:
				if b.isbn == selected.isbn:
					if not b.rented:
						b.book_rent()
						b.rent_count += 1
						self.update_books()
						complete(f"【 {b.title} 】 대여 완료되었습니다.")
					else:
						warn("※ 이미 대여중인 도서입니다. ※")
						return
 
		
	def book_return(self):
		"""
		ISBN에 해당하는 책을 반납 처리합니다.
		이미 반납된 책인 경우 안내 메시지를 출력합니다.
		반납 성공 시 대여 횟수를 증가시키고 저장합니다.
		"""
		selected = self.show_books_for_choose("return")
		if selected:
			for b in self.books:
				if b.isbn == selected.isbn:
					if b.rented:
						b.book_return()
						self.update_books()
						complete(f"【 {b.title} 】 반납 완료되었습니다.")
					else:
						warn("※ 이미 반납되어있습니다 ※")
						return
 

	def add_books(self):
		"""
		새로운 책을 도서관에 추가하고 저장합니다.
		
		Args:
			book (Book): 추가할 Book 객체
		"""
		info("↓ 추가할 도서의 정보를 입력해주세요 ↓")
		answer("▶︎ 도서명:")
		title = input()
		answer("▶︎ 저자:")
		author = input()
		answer("▶︎ 출판일:")
		published = input()
		answer("▶︎ ISBN:")
		isbn = input()
		book = Book(title, author, published, isbn)
		self.books.append(book)
		complete(f"【 {book.title} 】추가 완료되었습니다.")
		self.update_books()

	
	def remove_books(self):
		"""
		책 목록을 번호로 보여주고, 선택된 책을 삭제합니다.
		삭제 후 JSON 파일을 갱신합니다.
		"""
		
		books_list = [b for b in self.books]
		if not books_list:
			warn("※ 도서가 없습니다. ※")
			return
		
		self.draw_books(books_list)
  
		warn("↓ 제거할 도서의 번호를 입력해주세요 ↓")
		
		while True:
			try:
				answer("번호 선택: ")
				sel = int(input())
				if 1 <= sel <= len(self.books):
					removed_book = books_list.pop(sel - 1)
					self.books.remove(removed_book) # 실질적 제거
					complete(f"【 {removed_book.title} 】제거 완료되었습니다.")
					self.update_books()
					break
				else:
					warn("!! 없는 번호 입니다 !!")
			except ValueError:
				warn("!! 숫자만 입력해주세요 !!")
    
		
	def show_books_most_rented(self):
		"""
		대여 횟수 기준 상위 5권의 책을 랭킹 형식으로 출력합니다.
		"""
  
		rank = sorted(self.books, key=lambda b: b.rent_count, reverse=True)
		
		select(f"{'。':>13}{'。':>4}{'。':>4}\n")
		print(f"{'│＼':>14}{'／':>1}{'＼':>2}{'／│':>1}")
		print(f"{'│':>13}{'│':>10}")
		print(f"{'대여 랭킹 TOP 5':>21}")   
		print(f"{'└':>13}{'─'*9}┘")
  
		self.draw_books(rank[:5], True)

		
	def book_search(self):
		"""
		도서명 또는 저자명 기준으로 책을 검색하여 결과를 출력합니다.
		
		Args:
			type (str): "1"이면 도서명 기준, 그 외는 저자명 기준 검색
			keyword (str): 검색할 키워드 문자열
		"""
		info("↓ 검색할 항목을 선택해주세요. ↓")
		while True:
			try:
				answer(f"1. 제목 / 2. 저자: ")
				type = int(input())
				if 1<=type<=2:
					keyword = input("\n▶ 검색어: ")
					if len(keyword.strip()) == 0:
						warn("※ 검색어를 입력해주세요 ※")
						continue
					
					books_list = [b for b in self.books if(str(b.title if type==1 else b.author).find(keyword) != -1)]
					if not books_list:
						warn("※ 해당하는 도서가 없습니다 ※")
						break
					
					self.draw_books(books_list)
					break
				else :
					warn("!! 없는 번호 입니다 !!")
					continue
			except ValueError:
				warn("!! 숫자만 입력해주세요 !!")
				continue

def formatting_msg(type, msg):
	color_dict = {
		"normal"	: 0,
		"gray"		: 90,
		"red"		: 91,
		"green"		: 92,
		"yellow"	: 93,
		"blue"		: 94,
		"purple"	: 95,
		"skyblue"	: 96
	}
		
	code = color_dict["normal"]

	if type in("select","info"):
		code = color_dict["yellow"]
	elif type == "answer":
		code = color_dict["purple"]
	elif type == "warn":
		code = color_dict["red"]
	elif type == "complete":
		code = color_dict["skyblue"]
	elif type == "quest":
		code = color_dict["gray"]
	elif type == "menu":
		code = color_dict["green"]
	else :
		if color_dict[type]:
			code = color_dict[type]
	return f"\033[{code}m{msg}"

def normal(msg): print(formatting_msg("normal", msg))		
def warn(msg): print("\n"+formatting_msg("warn", msg))
def info(msg): print("\n"+formatting_msg("info", msg)+"\n")
def select(msg): print(formatting_msg("select", msg), end=' ')
def answer(msg): print("\n"+formatting_msg("answer", msg), end=' ')
def complete(msg): print(formatting_msg("complete", msg))
def quest(msg): print("\n"+formatting_msg("quest", msg), end=' ')
def menu(msg): print(formatting_msg("menu", msg))
	

			



	
	
			
			

