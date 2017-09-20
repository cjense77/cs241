class Person:
    def __init__(self, name='anonymous', bday='unknown'):
        self.name = name
        self.bday = bday
        
    def display(self):
        print('{} (b. {})'.format(self.name, 
                                  self.bday))
        
class Book:
    def __init__(self, title='untitled', 
                 author=Person(), 
                 publisher='unpublished'):
        self.title = title
        self.author = author
        self.publisher = publisher
    
    def display(self):
        print('{}\nPublisher:\n{}\nAuthor:'.format(self.title,
                                                   self.publisher))
        self.author.display()
        
def main():
    book = Book()
    book.display()
    
    print('\nPlease enter the following:')
    book.author.name = input('Name: ')
    book.author.bday = input('Year: ')
    book.title = input('Title: ')
    book.publisher = input('Publisher: ')
    print('')
    
    book.display()
    
if __name__ == '__main__':
    main()