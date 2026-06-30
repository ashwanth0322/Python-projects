#importing the modules to get the final output of the library management system 
import book
while True:
    print("\nThese are the menus available")
    print("1. Add Books")
    print("2. Display Books")
    print("3. Search Books")
    print("4. Delete Books")
    print("5. Update Book")
    print("6. Exit")

    try:

        menu=int(input("Enter the menu :"))
        if menu == 1:
            title=input("Enter the title of book :")
            author=input("Enter the name of the author :")
            genre=input("Enter the genre of the book :")
            year=int(input("Enter the year of publication :"))

            b1=book.Book(title,author,genre,year)
            b1.save_to_file()
            print("Books Added successfully")

        elif menu == 2:
            b=book.Book("","","",0)
            b.display_books()

        elif  menu == 3:
            search=input("Enter the name of the Book to be Searched :")
            b=book.Book("","","",0)
            b.search_book(search)

        elif menu == 4:
            delete=input("Enter the Title of the book to be deleted :")
            b=book.Book("","","",0)
            b.delete_book(delete)

        elif menu == 5:
            b=book.Book("","","",0)
            b.update_book()

        elif menu == 6:
            print("Thank you For visiting")
            break

           

        else:
            print("Please choose an valid menu")

    except ValueError:
        print("Please enter an integer menu")
