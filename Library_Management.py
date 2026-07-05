book = []
while True:
    print("====== Library Management ======")
    print("1. Add Books")
    print("2. View Books")
    print("3. Search Books")
    print("4. Remove Books")
    print("5. Total Books")
    print("6. Exit")
    Choice = int(input("Enter your Choice:"))
    if Choice == 1:
        def add_books():
            books = input("Enter book name:")
            book.append(books)
            print("book added succesfully!!")
        add_books()   
        print(book)
    elif Choice == 2:   
        def view_books(): 
            if not book:
                print("No Books Available!!")
            else:
                print("====== Library ======")
        view_books() 
        for books in book:
            print(books)
    elif Choice == 3:
        def search_books():
            search = input("Enter book name:")
            if search in book:
                print("✅ Book Found") 
            else:
                print("❌ Book not Found!!")
        search_books()            
    elif Choice == 4:
        def remove_books():
            search = input("Enter Book name:")
            if search in book:
                book.remove(search)
                print("Book removed Succesfully👍")
            else:
                print("❌ Book not found")    
        remove_books()
    elif Choice == 5:
        print("📚 Total Books =", len(book))
    elif Choice == 6:
         print("🙏 Thank you for using Library Management System!")
         print("👋 Have a Nice Day!")
         break
 
        
            