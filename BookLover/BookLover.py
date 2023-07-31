import pandas as pd
import numpy as np
class BookLover():
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre 
        self.num_books = num_books
        self.book_list = book_list
        self.book_list['book_rating'] = self.book_list['book_rating'].astype(int) 
    
    def add_book(self, book_name, rating):
        if not self.has_read(book_name):
            if (1 <= rating <= 5):
                self.book_list = pd.concat([self.book_list, pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [rating]
                })], ignore_index=True)
            else:
                print('Rating not valid')
        else:
            print('Book already exists')
        self.num_books = self.book_list.shape[0]
  
    def has_read(self, book_name):
        return (self.book_list['book_name'] == book_name).any() 
    
    def num_books_read(self):
        return self.num_books
    
    def fav_book(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
    

