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
	def __init__(self, file_path="./files/books.json"):
		self.file_path = file_path
		self.books = {}
		self.load_books()
	
	def load_books(self):
		if os.path.exists(self.file_path) and os.stat(self.file_path).st_size > 0 :
			with open(self.file_path, "r", encoding="utf-8") as f:
				data = json.load(f)
				self.books = [Book.from_dict(b) for b in data]
			print(self.books)
		else:
			self.books = {}
		
	def update_books(self):
		with open(self.file_path, "w", encoding="utf-8") as f:
			json.dump([b.convert_dict() for b in self.books], f, indent=2, ensure_ascii=False)
	
	def add_books(self, book):
		self.books.append(book)
		print(f"'{book.title}' 추가 완료.")
		self.update_books()
	
	def remove_books(self, isbn):
		prev = len(self.books)
		self.books = [b for b in self.books if b.isbn != isbn]
		if len(self.books) < prev:
			print(f"{isbn} 도서 삭제 완료.")
			self.update_books()
		else:
			print("해당 ISBN의 도서를 찾을 수 없습니다.")
	
	def show_books_available(self, isMenu=False):
		print(f"{'【 대여 가능한 도서 목록 】':>30}")
		print(f"┌"+"─"*119+"┐")
		print(f"│{'도서명':>15}{'│':>15}{'저자':>12}{'│':>11}{'출판일':>12}{'│':>11}{'ISBN':>18}{'│':>13}")
		print(f"│"+"─"*119+"│")
		found = False
		for b in self.books:
			if not b.rented:
				print(f"{b.title:<5}{b.author:>30}{b.isbn:>18}")
				found = True
		if not found:
			print("대여 가능한 도서가 없습니다.")
	
	def show_books_for_choose(self, forWhat):
		if forWhat == "rent":
			books_list = [b for b in self.books if not b.rented]
		elif forWhat == "return":
			books_list = [b for b in self.books if b.rented]
		else:
			books_list = []
		
		for i, b in enumerate(books_list, start=1):
			print(f"{i}. {b.title} ({b.author}) / {b.isbn}")
		
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
		rank = sorted(self.books, key=lambda b: b.rent_count, reverse=True)
		print("==대여가 가장 많이 된 책 순위 (TOP 5)==")
		print("-" * 60)
		print(f"{'순위':<6}{'제목':<30}{'저자':<15}{'횟수':>5}")
		print("-" * 60)
	
		for idx, book in enumerate(rank[:5], start=1):
			print(f"{idx:<6}{book.title:<30}{book.author:<15}{book.rent_count:>5}")
		print("-" * 60)

	
	def rent(self, isbn):
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
		for b in self.books:
			if b.isbn == isbn:
				if b.rented:
					b.book_return()
					b.rent_count += 1
					self.update_books()
				else:
					print("이미 반납되어있습니다.")
				return

	def book_search(self, type, keyword):
		for b in self.books:
			if(str(b.title if type=="1" else b.author).find(keyword) != -1):
				print(f"{b.title} / {b.author}")
			

				

               
             
               
		