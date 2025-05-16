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

# Library 인스턴스 생성
lib = Library()

# 종료 메시지 출력 함수
def printStopMsg():
    print("\033[91m\n>>>>>>>> 프로그램을 종료합니다 <<<<<<<<<<\033\n[0m")

# 각 동작 후 결과에 따라 종료할지 여부 판단
def ctrl_after_action(res):
	if res:
		return True
	else:
		printStopMsg()
		return False

# 메인 메뉴를 보여주고 사용자 입력을 처리하는 함수
def show_menu():
	while True:
		print(f"\033[92m\n┌"+"─"*31+"┐")
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

		choice = input("\n\033[93m메뉴 번호를 입력하세요 ▷▷ ")
		
		if choice == "1":
			if not ctrl_after_action(lib.show_books_available()):
				break	
		elif choice == "2":
			if not ctrl_after_action(lib.book_search()):
				break
		elif choice == "3":
			if not ctrl_after_action(lib.rent()):
				break
		elif choice == "4":
			if not ctrl_after_action(lib.book_return()):
				break
		elif choice == "5":
			if not ctrl_after_action(lib.add_books()):
				break
		elif choice == "6":
			if not ctrl_after_action(lib.remove_books()):
				break
		elif choice == "7":
			if not ctrl_after_action(lib.show_books_most_rented()):
				break
		elif choice == "8":
			if not ctrl_after_action(not lib.doContinue('종료')):
				break
		else:
			print("\033[92m\n잘못된 입력입니다. 다시 선택하세요.")
			continue
	
# 프로그램 진입점 (이 파일 직접 실행 시 동작)
if __name__ == "__main__":
    show_menu()


	