class Library:
    def __init__(self, list, libraryname):
        self.list = list
        self.libraryname = libraryname
        self.user_leger = {}
        for i in list:
            self.user_leger[i] = None

    def displaybooks(self):
        for i in self.list:
            print(i)

    def addbooks(self):
        book_name = input("enter the book name\n")
        book_author = input("enter the author name\n")
        self.list.append(f'{book_name}-{book_author}')
        self.user_leger[f'{book_name}-{book_author}'] = None
        print('you have successfully added the book')

    def lendbooks(self):
        print("see the book code for book carefully")
        for i in range(len(self.list)):
            print(f'{i} for {self.list[i]}')
        book_code = int(input('enter the book code\n '))
        if self.user_leger[self.list[book_code]] != None:
            print(
                f'{self.user_leger[self.list[book_code]]} has taken your lovely book "{self.list[book_code]}"\n you cannot have it now')
        else:
            print('the book is yours man')
            self.user_leger[self.list[book_code]] = input("enter your real name\n")

    def returnbook(self):
        print('thanks for returning the book')
        print("see the book code for book carefully")
        for i in range(len(self.list)):
            print(f'{i} for {self.list[i]}')

        book_code = int(input('enter the book code\n '))
        name = input('enter your name\n')
        if self.user_leger[self.list[book_code]] == name:
            self.user_leger[self.list[book_code]] = None
            print(f'you have successfully returned the book "{self.list[book_code]} "')
        else:
            print('try again and use your real name used before and dont return without taking book')


book = ['one hundred years of solitude - garcia gabriel marquez', 'the sister keeper - jodi picault',
        'it-stephen king', 'harry potter and the cursed child-j.k rowling', '30 famous short stories-by several authors'
        ]
PrAsHaNtLibrary = Library(book, 'Celestial Library')
while True:
    mode = int(input("enter \n 1 for Book List\n 2 for Donate Book \n 3 for Lend Book \n 4 for Return Book\n 5 for Quit\n"))
    if mode == 1:
        PrAsHaNtLibrary.displaybooks()
    elif mode == 2:
        PrAsHaNtLibrary.addbooks()
    elif mode == 3:
        PrAsHaNtLibrary.lendbooks()
    elif mode == 4:
        PrAsHaNtLibrary.returnbook()
    elif mode == 5:
        break