from Books_in_library_collections import science_books, fantasy_books ,encyclopedias, horror_books ,self_help_books , money_books , fiction_books

books_dict= {
    "Science": science_books,
    "Fantasy": fantasy_books,
    "Encyclopedia": encyclopedias,
    "Horror": horror_books,
    "Self_help": self_help_books,
    "Money": money_books,
    "Fiction" : fiction_books
} 
genre_tuple = ('Science', 'Fantasy', 'Encyclopdeia', 'Horror', 'Money', 'Self_Help', 'Fiction')

#print(genre_names)
# fantasy_book_names = list(fantasy_books.keys())
proper_books_dict = books_dict.values()
merged_proper_dict = {}   ##
for any in proper_books_dict:
    merged_proper_dict.update(any)

# print(merged_proper_dict)

class Fine:
    def __init__(self,daysofissue, usersubmitted):
        fine = 0
        self.daysofissue = daysofissue
        self.user_submitted = usersubmitted
        if usersubmitted > daysofissue:
            fine+= (usersubmitted- daysofissue)*2     #double fine for late return
            
            print("Thanks for returning the book.")
            print(f"*** Your total fine of late submission: ${fine} ***")
        else:
            print("\t***Thankyou for returning the book on time...***\t")
        

       
class Books:
    '''
    checks if that book is in the library
    '''
    def __init__(self):
        
        
        pass
             
    def find_book(self,user_wants):
        found = False
        
        self.user_wants = user_wants
        # print(book_name

        while not found:
            for  key, value in books_dict.items():
                
                    for title, details in value.items():
                
                        if title.title() == user_wants.title():
                        
                            
                            print(f"~Your book is in '{key}' genre.\n~Author's name: '{value[title]['author']}'\n~Publishing year : {value[title]['publishing_year']}.")
                            found = True
                    
                    if found:
                        break
            if found:
                break
                            
                        
                        # returns genre and book details
            if not found:
                print("Sorry but currently it's not available.")
                break
                
    
    # def daysofissue(days):

                



    
