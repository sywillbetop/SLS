'''
4. sls.py : 프로그램을 실행하는 main 프로그램 이다
	4.1 sls.py는 사용자 인터페이스를 통해 book 모듈과 library 모듈을
	이용하여, 책을 대여하고 반납하는 기능을 실행하는 모듈이다.
	4.2 동작 기능은, (1) 대여 가능한 책 목록보여주기, (2) 대여하기, 
	(3) 반납하기, (4) 신간 추가하기, (5) 고서 제거하기, (6) 종료하기 등
	6개의 메뉴로 구성된다. 
	더 추가하고 싶은 기능이 있다면 추가하여 동작시키기 바란다
'''
from library import Library, menu, select, normal, warn, quest
from book import Book

# Library 인스턴스 생성
lib = Library()

# 종료 메시지 출력 함수
def printStopMsg():
    warn("\n>>>>>>>> 프로그램을 종료합니다 <<<<<<<<<<") 
    normal("\n")

# 각 동작 후 결과에 따라 종료할지 여부 판단
def ctrl_after_action(ac=True):
	while True:
		quest(f"프로그램을 {'계속' if ac else '종료'}하시겠습니까? (y/n) :")
		isKeep = input().upper()
		if isKeep not in ("Y", "N"):
			print("y / n 만 입력가능합니다.")
			continue
		else:
			if isKeep.upper() == "Y": 
				if not ac: printStopMsg() # 종료하시겠습니까?
				return True
			else: 
				if ac: printStopMsg() # 종료하시겠습니까?
				return False

# 메인 메뉴를 보여주고 사용자 입력을 처리하는 함수
def show_menu():
	while True:
		menu("\n┌"+"─"*31+"┐")
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

		select("\n메뉴 번호를 입력하세요 ▷▷")
		choice = input()
		
		if choice == "1":
			lib.show_books_available()
		elif choice == "2":
			lib.book_search()
		elif choice == "3":
			lib.rent()
		elif choice == "4":
			lib.book_return()
		elif choice == "5":
			lib.add_books()
		elif choice == "6":
			lib.remove_books()
		elif choice == "7":
			lib.show_books_most_rented()
		elif choice == "8":
			if ctrl_after_action(False):
				break
		else:
			warn("※ 잘못된 입력입니다. 다시 선택하세요 ※")
			continue


		if choice != "8" and not ctrl_after_action():
			break
	
	
# 프로그램 진입점 (이 파일 직접 실행 시 동작)
if __name__ == "__main__":
    show_menu()


	