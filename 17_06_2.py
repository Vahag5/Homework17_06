phone_book = {}
def contacts():
    global phone_book
    while True:
        q = input("if You want added new contact press '1'\n"
"if you want search contact press:  '2'\n"
"if you want see all contacts press: '3'\n"
"if you want exit the program press: '4'\n")
        if q == '1':
            n = input("name: ")
            p = input("phone_number: ")
            print('Contact added successfully!')
            phone_book[n] = n
            phone_book[n] = p
        elif q == '2':
            c = input("Enter name: ")
            print("Phone number:",phone_book.get(c,"false name"))
        elif q == '3':  
            print("Contacts:")
            for i in phone_book:
                print(f"{i} :{phone_book[i]}")
        elif q == '4':
            print("Goodbye!")
            break  
        else:
            continue
        
    return phone_book
contacts()
