#Creating a module to have the data of books for the library management system
class Book:

    '''attributes of the book'''
    def __init__(self,title,author,genre,year,availability):
        self.title=title
        self.author=author
        self.genre=genre
        self.year=year
        self.availability=availability

    '''methods of book'''
    def save_to_file(self):
        with open("books.txt","a") as file:
            file.write(f"{self.title},{self.author},{self.genre},{self.year},{self.availability}\n")

    def display_books(self):
        
        with open("books.txt", "r") as file:
            for line in file:
                data=line.split(",")
                print("\nTitle of the book :",data[0])
                print("Name of the Author :",data[1])
                print("Genre of the book :",data[2])
                print("Year of Publication :",data[3])
                print("Availability :",data[4])
                print("-"*40)
                

    def search_book(self,search):
        with open("books.txt","r") as file:
            found=False
            for line in file:
                data=line.split(",")
                if data[0] == search:
                    print("\nTitle of the book :",data[0])
                    print("Name of the Author :",data[1])
                    print("Genre of the book :",data[2])
                    print("Year of Publication :",data[3])
                    print("Availability :",data[4])
                    print("-"*40)
                    found=True
            if found == False:
                print("No Book Found")

    def delete_book(self,delete):
        with open("books.txt","r") as file:
            lines=file.readlines()
            found=False
            new_line=[]
            for line in lines:
                data=line.split(",")
                if delete.lower().strip() == data[0].lower().strip():
                    found=True
                else:
                    new_line.append(line)
                
        if found == False:
            print("No Book Found")
            return
        with open("books.txt","w") as file:
            for line in new_line:
                file.write(line)
       

    def update_book(self):
        with open("books.txt","r") as file:
           new_lines=[]
           found=False
           update=input("Enter the title of the book to be updated :")
           for line in file: 
                data=line.split(",")
                
                if update == data[0]:
                        new_title=input("Enter the new title :")
                        new_author=input("Enter the name of the author :")
                        new_genre=input("Enter the genre of the book :")
                        new_year=input("Enter the year of publication :")
                        new_availablity=input("Enter the availablity :")
                        new_lines.append(f"{new_title},{new_author},{new_genre},{new_year},{new_availablity}\n")
                        found=True
                        print(f"Updated the details of book {update}\n")
                    
                else:
                    new_lines.append(line)
           if found == False:
               print("No Book Found")

        with open("books.txt","w") as file:
            for lines in new_lines:
              file.write(lines)


    def issue_book(self):
        with open("books.txt","r") as file:
            issue=input("Enter the title of the book whose availablity has to be changed :")
            lines=file.readlines()
            new_lines=[]
            found=False
            for line in lines:
                data=line.split(",")
                if issue == data[0]:
                    if data[4].strip() == "issued":
                        print("The book is already issued")
                    elif data[4].strip() == "available":
                        data[4]="issued"
                    found=True
                    new_lines.append(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n")
                    print(f"The book {issue} is successfully isssed")
                else:
                    new_lines.append(line)
            if found == False:
                print("No Book Found")
        with open("books.txt","w") as file:
            for line in new_lines:
                file.write(line)


    def return_books(self):
        with open("books.txt","r") as file:
            return_book=input("Enter the title of the book that you want to return :")
            new_lines=[]
            found=False
            for line in file:
                data=line.split(",")
                data[4]=data[4].strip()
                if data[0].lower() == return_book.lower():
                    if data[4].lower() == "issued":
                        data[4]="available"
                        new_lines.append(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n")
                        found=True
                        
                    elif data[4].lower() == "available":
                        print("The Book is already returned")
                        new_lines.append(line)
                        found=True
                    print(f"The book {return_book} is returned successfully\n")
                else:
                    new_lines.append(line)
            if found == False:
                print("No Book Found")
            
        with open("books.txt","w") as file:
            for line in new_lines:
                file.write(line)

