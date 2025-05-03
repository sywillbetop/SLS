import json

class Book:
    def get_books():
        with open('./files/books.json', 'r', encoding="utf-8") as f:
            books = json.load(f)
        
        for book in books:
            print(str(book['isbn']).replace("-",""))
            if(str(book['isbn']).replace("-","").__eq__("1111111111111")) :
                book['rented'] = True
        
        with open('./files/books.json', 'w', encoding="utf-8") as fw:
            json.dump(books, fw, indent=2, ensure_ascii=False)
    
    get_books()
    
    def book_rent():
        pass
    
    def book_return():
        pass
    

   

    