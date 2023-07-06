phone_book = {}
def contacts():
    global phone_book
    while True:
        q = input("Continiue added contact Yes/No ? ")
        if q == 'Yes' or q == 'Y' or q == 'y':
            pass
        else: 
            break   
        n = input("name: ")
        p = input("phone_number ")
        print('Contact added successfully!')
        phone_book['name'] = n
        phone_book['phone_number'] = p
    return phone_book
contacts()
print(phone_book)