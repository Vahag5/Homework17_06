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
            p = input("phone_number ")
            print('Contact added successfully!')
            phone_book['name'] = n
            phone_book['phone_number'] = p
        elif q == '2':
        elif q == '3':   
        else: 
             break  
        
    return phone_book
contacts()
print(phone_book)
