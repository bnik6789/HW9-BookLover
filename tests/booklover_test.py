import unittest
from BookLover import BookLover 
import pandas as pd
import numpy as np

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_name = 'Intro to python'
        new_book_rating = 4
        
        new_lover.add_book(new_book_name, new_book_rating)
        
        expected = pd.DataFrame({
            'book_name': [new_book_name], 
            'book_rating': [new_book_rating]
        })
        self.assertEqual(True, expected.equals(new_lover.book_list))
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_name = 'Intro to python'
        new_book_rating = 4
        
        new_lover.add_book(new_book_name, new_book_rating)
        new_lover.add_book(new_book_name, new_book_rating)
        expected = pd.DataFrame({
            'book_name': [new_book_name], 
            'book_rating': [new_book_rating]
        })
        self.assertEqual(True, expected.equals(new_lover.book_list))
    
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_name = 'Intro to python'
        new_book_rating = 4
        
        new_lover.add_book(new_book_name, new_book_rating)
        self.assertTrue(new_lover.has_read(new_book_name))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_name = 'Intro to python'
        new_book_rating = 4
        
        new_lover.add_book(new_book_name, new_book_rating)
        new_book_not = 'Intro to C'
        self.assertFalse(new_lover.has_read(new_book_not))
    
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_names = ['Intro to python', 'Intro to C', 'Intro to Java', 'Intro to Ruby', 'Intro to SQL']
        new_book_ratings = [1, 2, 3, 4, 5]
        
        for new_name, new_rating in zip(new_book_names, new_book_ratings):
            new_lover.add_book(new_name, new_rating)
            
        self.assertEqual(len(new_book_names), new_lover.num_books_read())
        
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        new_lover = BookLover('Test 1', 'Test 1@example.com', 'Example')
        new_book_names = ['Intro to python', 'Intro to C', 'Intro to Java', 'Intro to Ruby', 'Intro to SQL']
        new_book_ratings = [1, 2, 3, 4, 5]
        
        for new_name, new_rating in zip(new_book_names, new_book_ratings):
            new_lover.add_book(new_name, new_rating)
        
        for book_name, book_rating in new_lover.fav_book().values:
            self.assertTrue(book_rating > 3)
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)