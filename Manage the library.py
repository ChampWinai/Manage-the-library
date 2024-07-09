book_list = []
borrow_list = []
all_book = []
with open("all_book.txt","r") as file:
    data = file.read().split()
    for line in data :
      item = line.split()
      all_book.append(item)

with open("book_list.txt","r") as reader:
  line = reader.readline()
  while line != '':  # The EOF char is an empty string
   print(line, end='')
   line = reader.readline()
   book_list.append(line)

with open("borrow_list.txt","r") as file:
    data = file.read().splitlines()
    for line in data :
      item = line.split()
      borrow_list.append(item[0])
      
def booklist():
  print("■"*32)
  print("■"," "*28,"■")
  print("■■■■■■■ Book List ■■■■■■■")
  print("■"," "*28,"■")
  print("■"*32,"\n")
  serial = 0
  print("❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉\n")
  print("%s %20s %s"%("No.","Name Book","\n"))
  print("❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉❉\n")
  for i in range (len(book_list)):
    serial+=1
    print("%s %5s %-1s\n "%(serial," ",book_list[i]))
  else:
    serial = 0

def borrowbook():
  try:
    borrow_choice = input("Please enter the name of the book you want to borrow. :")
    print(" ")
    if borrow_choice in borrow_list: 
      print("✪"*28+"\n")
      print("This book has been borrowed.\n")
      print("✪"*28)
    elif not borrow_choice in book_list:
      print("✪"*28+"\n")
      print(" {borrow_choice} This book does not exist in the system.\n")
      print("✪"*28)
    elif borrow_choice in book_list:
      borrow_list.append(borrow_choice)
      book_list.remove(borrow_choice)
      print("✪"*28+"\n")
      print("You have successfully borrowed the book.\n")
      print("✪"*28)
      with open("borrow_list.txt","w+") as file:
        for x in range (len(borrow_list)):
          file.write("%s\n"%(borrow_list[x]))
      with open("book_list.txt","w+") as file:
        for x in range (len(book_list)):
          file.write("%s\n"%(book_list[x]))
  except:
    print("✪"*28+"\n")
    print("Please enter the title of the book in the system.\n")
    print("✪"*28)


def list_borrowbook():
 if not  borrow_list in book_list:
    for i in range(len(borrow_list)):
      print("✪"*28+"\n")
      print("list of borrowed books \n")
      print(" ",borrow_list[i],"\n")
      print("✪"*28)
 
 if not borrow_list:
    print("✪"*28+"\n")
    print("No books were borrowed. \n")
    print("✪"*28)
  
def returnbook():
  try:
    return_input = input("Please enter the name of the book you wish to return. :")
    print(" ")
    if return_input in borrow_list:
      if not return_input in book_list:
        book_list.append(return_input)
        borrow_list.remove(return_input)
        print("✪"*28+"\n")
        print("The book was returned successfully.\n")
        print("✪"*28)
        with open("book_list.txt","w+") as file:
         for x in range (len(book_list)):
           file.write("%s\n"%(book_list[x]))
        with open("borrow_list.txt","w+") as file:
         for x in range (len(borrow_list)):
           file.write("%s\n"%(borrow_list[x]))
      else:
        print("✪"*28+"\n")
        print("This book already exists in the system.\n")
        print("✪"*28)
    else:
      print("✪"*28+"\n")
      print("This book does not exist in the system.\n")
      print("✪"*28)
  except Exception as e:
    print(e)

def donatebook():
  x = input("Please enter the name of the book you want to add. :")
  print(" ")
  book_list.append(x)
  all_book.append(x)
  print("✪"*28+"\n")
  print("Successful book addition"+"\n")
  print("✪"*28)
  with open("book_list.txt","w+") as file:
    for x in range (len(book_list)):
      file.write("%s\n"%(book_list[x]))
  with open("all_book.txt","w+") as file:
    for x in range (len(all_book)):
      file.write("%s\n"%(all_book[x]))


while True:
  print("╔══════════════════════════════════╗")
  print("*"*9,"Library Program","*"*10)
  print("╚══════════════════════════════════╝")
  print("   Please select the desired topic.  \n")
  print(" 1. View all books list ")
  print(" 2. Borrow books ")
  print(" 3. View a list of borrowed books. ")
  print(" 4. Return the book ")
  print(" 5. Add new book ")
  print(" 6. Exit the program ")
  print("*"*32)
  choice = input("Please select the desired topic. : ")
  print(" ")
  if choice == "1":
   booklist()
  elif choice == "2":
    borrowbook()
  elif choice == "3":
    list_borrowbook()
  elif choice == "4":
    returnbook()
  elif choice == "5":
    donatebook()
  elif choice == "6":
    break
  else:
    print("Try again, please select items 1-5.")

print("❉❉❉❉❉❉❉ Good luck ❉❉❉❉❉❉❉")