import pandas as pd

class BookLover:
    
    def __init__(self, nm:str, em:str, fvg:str,
                 nb:int=0,
                 bls:pd.DataFrame=pd.DataFrame({'book_name' : [],
                                                'book_rating' : []})):
        self.name = nm
        self.email = em
        self.fav_genre = fvg
        self.num_books = nb
        self.book_list = bls

    def add_book(self, bn:str, r:int):
        if bn in self.book_list['book_name'].values:
            return

        new_book = pd.DataFrame({
            'book_name' : [bn],
            'book_rating' : [r]
        })

        self.book_list = pd.concat([self.book_list, new_book],
                                   ignore_index=True)
        
        self.num_books += 1

    def has_read(self, bn:str):
        return bn in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list.query("book_rating > 3")


if __name__ == '__main__':
    b = BookLover("Han Solo", "hsolo@strwrs.com",
                  "scifi")
    print(b.num_books_read())
    b.add_book("War of the Worlds", 4)
    print(b.num_books_read())
    print(b.has_read("War and Peace"))
    print(b.has_read("War of the Worlds"))
    b.add_book("Heart of Darkness", 2)
    print(b.fav_books())

