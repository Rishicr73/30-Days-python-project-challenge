#Library managment system using python 
import datetime
import os
#os.getcwd()

class LMS:
    ''' This class is used to keep record of books library .
    It has total four module : "Display Books" , "Issue Books" , "Return Book" , "Add Books" '''
    def __init__(self, list_of_books , library_name) -> None:
        
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id) : {"books_title":line.replace('\n' , ''),\
                "lender_name" : "","issue_date" : '' , "status" : "Available"}})
            Id += 1
        #print(self.books_dict)    
    def display_books(self):
        print("---------List of Books---------")        
        print("Books ID" ,"\t" , "Title")
        print("-------------------------------")
        for key,value in self.books_dict.items():
            print(key , "\t\t" , value.get("books_title") ,'- [' , value.get('status') ,']')
#using the 'get' we can get keys value

    def Issue_books(self):
        books_id = input("Enter books Id :")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"] == "Available":
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['issue_date']}")
                return self.issue_books()
            elif self.books_dict[books_id]['status'] == "Available":
                your_name = input("Enter your name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['status'] = "Already issued"
                print("Book Issued successfully !!! \n")
            else:
                print("Book ID not found")
                
    def add_books(self):
        new_books = input("Enter book title :")
        if new_books == '':
            return self.add_books()
        elif len(new_books) > 25:
            print("Book title length should be less than 20. ")
        else:
            with open(self.list_of_books , "a") as bk:
                bk.writelines(f'{new_books}\n')
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,\
                    'lender_name':'','issue_date':'', 'status':'Available'}})
                print(f"This books '{new_books}' has been added successfully !!!")

    def return_book(self):
        books_id = input("Enter books ID :")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == "Available" :
                print("This book is already available in library . please check your book id .")
                return(return_book)
            elif not self.books_dict[books_id]["status"] == "Available":
                self.books_dict[books_id]["lender_name"] = ""
                self.books_dict[books_id]["issuse_date"] = ""
                self.books_dict[books_id]["status"] = "Available"
                print("Successfully update !!")
        else:
            print("Book Id not find !")

if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.txt", "VS")
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_book()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check. !!!")
