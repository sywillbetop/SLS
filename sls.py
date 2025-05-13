'''
4. sls.py : 프로그램을 실행하는 main 프로그램 이다
	4.1 sls.py는 사용자 인터페이스를 통해 book 모듈과 library 모듈을
	이용하여, 책을 대여하고 반납하는 기능을 실행하는 모듈이다.
	4.2 동작 기능은, (1) 대여 가능한 책 목록보여주기, (2) 대여하기, 
	(3) 반납하기, (4) 신간 추가하기, (5) 고서 제거하기, (6) 종료하기 등
	6개의 메뉴로 구성된다. 
	더 추가하고 싶은 기능이 있다면 추가하여 동작시키기 바란다
'''
from library import Library
from book import Book

lib = Library()


def show_menu():
	print(f"┌"+"─"*31+"┐")
	print(f"│{'│':>32}")
	print(f"│{'도서관 메뉴':>16}{'│':>11}")
	print(f"│{'│':>32}")
	print(f"│{'(1) 대여 가능한 책 보기':>19}{'│':>5}")
	print(f"│{'(2) 책 검색':>12}{'│':>17}")
	print(f"│{'(3) 책 대여하기':>14}{'│':>13}")
	print(f"│{'(4) 책 반납하기':>14}{'│':>13}")
	print(f"│{'(5) 신간 추가하기':>15}{'│':>11}")
	print(f"│{'(6) 고서 제거하기':>15}{'│':>11}")
	print(f"│{'(7) 가장 많이 대여된 책5':>20}{'│':>4}")
	print(f"│{'(8) 종료':>10}{'│':>20}")
	print(f"│{'│':>32}")
	print(f"└"+"─"*31+"┘")
    
	print(f"")
	choice = input(" 번호를 입력하세요 ▷▷ ")
	into_menu(choice)

def into_menu(choice):
	if choice == "1":
		lib.show_books_available()
	elif choice == "2":
		print("====도서 검색====")
		type = input("1. 제목 / 2. 저자: ")
		keyword = input("검색어: ")
		lib.book_search(type, keyword)
	elif choice == "3":
		print("====책 대여하기====")
		selected = lib.show_books_for_choose("rent")
		if selected:
			lib.rent(selected.isbn)
	elif choice == "4":
		print("====책 반납하기====")
		selected = lib.show_books_for_choose("return")
		if selected:
			lib.book_return(selected.isbn)
	elif choice == "5":
		print("====신간 추가하기====")
		title = input("책 제목: ")
		author = input("* 저자: ")
		published = input("* 출판일: ")
		isbn = input("*ISBN: ")
		book = Book(title, author, published, isbn)
		lib.add_books(book)
	elif choice == "6":
		pass
	elif choice == "7":
		lib.show_books_most_rented()
	elif choice == "8":
		print("종료합니다.")
		pass
	else:
		print("잘못된 입력입니다. 다시 선택하세요.")


show_menu()


'''
while True:
	print(f"┌"+"─"*31+"┐")
	print(f"│{'│':>32}")
	print(f"│{'도서관 메뉴':>16}{'│':>11}")
	print(f"│{'│':>32}")
	print(f"│{'(1) 대여 가능한 책 보기':>19}{'│':>5}")
	print(f"│{'(2) 책 검색':>12}{'│':>17}")
	print(f"│{'(3) 책 대여하기':>14}{'│':>13}")
	print(f"│{'(4) 책 반납하기':>14}{'│':>13}")
	print(f"│{'(5) 신간 추가하기':>15}{'│':>11}")
	print(f"│{'(6) 고서 제거하기':>15}{'│':>11}")
	print(f"│{'(7) 종료':>10}{'│':>20}")
	print(f"│{'│':>32}")
	print(f"└"+"─"*31+"┘")
    
	print(f"")
	choice = input(" 번호를 입력하세요 ▷▷ ")
'''
    
	