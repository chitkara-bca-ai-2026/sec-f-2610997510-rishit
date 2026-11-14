books=[("python crash course","by Eric Matthes","(2019)","|Genre: programming"),
       ("Automate the boring stuff","by Ai Sweigart","(2020)","|Genre: programming"),
       ("Artificial Intelligence:","A morden approach by Stuart Russell","(2021)","|Genre: Ai"),
       ("Clean code","by Robert C. Martin","(2008)","|Genre: Software Engineering")]

library_categories={"Programming","programming","Ai","Software Engineering"}
student_wishlist={"Ai","Cloud Computing","Robotics","Cybersecurity"}
print("==========================================================================")
print("              LIBRARY BOOK & CATEGORY MANAGER                             ")
print("==========================================================================")
while True:
    print("Select an option:")
    print("1. View Cataloged Books")
    print("2. Add new book record")
    print("3. View unique library categories")
    print("4. Add category ro student wish list")
    print("5. Run category gap analysis")
    print("6. Exit")
    choice=int(input("Enter your choice(1-6): "))
    
    if choice==1:
        print("----Current Library Catalog (Fixed Records)---")
        for index,i in enumerate(books):
            print(index+1,*i)
            print(len(books))

    elif choice==2:
        print("---Add New Book Record---")     
        book_title=input("Enter book title: ") 
        auther_name=input("Enter Author name: ")  
        publication_year=input("Enter Publication year: ")
        category=input("Enter category/genre: ")
        new_book=(book_title,auther_name,publication_year,category)
        books.append(new_book)
        print("[SUCCESS] ""Data structure and Algorithms"" added as an immutable catalog record.")
        print("[INFO] Category set updated with: ""Data Science""")


    elif choice==3:
        print("---Unique Categories available in Library (Set)---")
        for index,i in enumerate(books):
            print(index+1,i[-1])
            #print(len(i[-1]))            FINDING THE LENGTH OF UNIQUE GENRES


    elif choice==4:
        print("---Add to Student Wishlist---")
        requested_category=input("Enter requested category: ") 
        student_wishlist.add(requested_category)
        print("[SUCCESS] ""Machine Learning"" is added to student wishlist.")


    elif choice==5:
        print("===========================================CATEGORY GAP ANALYSIS========================================")
        print(f"Library Holdings (Set): {library_categories}")
        print(f"Student Wishlist (Set): {student_wishlist}")
        print(f"Already in Stock (Intersection &): {library_categories & student_wishlist}")
        print(f"Purchase Order Needed (Difference -): {library_categories-student_wishlist}")
        print(f"Full combined Genre Coverage (Union |): {library_categories|student_wishlist}")
        print("========================================================================================================")


    elif choice==6:
        print("Thank you for using the library manager. Goodbye!!")  
        break             






