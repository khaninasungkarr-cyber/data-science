kamus = []

def show_data(kamus):
    if not kamus:
        print("add ur data")
    else:
        print("ur data is")
        for i, kata in enumerate(kamus):
            print(kata, [i])
            
def insert_data(kamus):
    kata_baru = input("judul kamus: ")
    kamus.append(kata_baru)
    print("ur data is add")
    
def edit_data(kamus):
    show_data(kamus)
    if kamus:
        i = int(input("choose ur number u want change: "))
        if 0 <= i < len(kamus):
            kata_baru = input("add ur new word:")
            kamus[i] = kata_baru
            print("ur data has been saved")
    else:
        print("ur data not valid")
        
def delete_data(kamus):
    show_data(kamus)
    if kamus:
        i = int(input("choose ur number u want delete: "))
        if 0 <= i < len(kamus):
            kamus.pop(i)
            print("ur data has been remove")
    else:
        print("ur data not valid")
        
def main():
    while True:
        print("menu")
        print("1. show data")
        print("2. insert data")
        print("3. edit data")
        print("4. delete data")
        print("5. exit")        
        pilihan = input("masukan pilihan: ")
        if pilihan == "1":
            show_data(kamus)
        elif pilihan == "2":
            insert_data(kamus)
        elif pilihan == "3":
            edit_data(kamus)
        elif pilihan == "4":
            delete_data(kamus)
        elif pilihan == "5":
            exit()
        else:
            print("no no")
                
if __name__ == '__main__':
    main()


    