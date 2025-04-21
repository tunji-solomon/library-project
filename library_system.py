class library:
    def __init__(self):
        self.shelf = []
        self.borrowed = {}
        self.available = []
        
    def add_book(self, book):
            for books in self.shelf:
                if books["name"] == book["name"]:
                    books["count"] += book["count"]
                    break
            else:
                if book["count"] > 0:
                    book["is_available"] = True
                self.shelf.append(book)
                
    def borrow_book(self, borrow):
        for book in self.shelf:
            amount_available = book["count"]
            amount_to_be_borrowed = borrow["count"]
            book_name = book["name"]
            borrow_name = borrow["name"]
            if book_name == borrow_name:
                if book["is_available"] == True:
                    if amount_available >= amount_to_be_borrowed:
                        amount_available -= amount_to_be_borrowed
                        if amount_available == 0:
                            book["is_available"] = False
                        book["count"] = amount_available
                        borrower = borrow["borrower"]
                        
                        if borrower in self.borrowed:
                            # Get the list of borrowed items
                            books = self.borrowed[borrower]
                            
                            # Check if item already exists
                            for book in books:
                                if book["name"] == borrow_name:
                                    book["count"] += amount_to_be_borrowed
                                    break
                            else:
                                # Item not found, add new entry
                                books.append({
                                    "name": borrow_name,
                                    "count": amount_to_be_borrowed
                                })
                        else:
                            # New borrower, create record
                            self.borrowed[borrower] = [{
                                "name": borrow_name,
                                "count": amount_to_be_borrowed
                            }]

                                            
                        return f"{borrow["borrower"]}, you have been borrowed {amount_to_be_borrowed} {borrow_name} {'book' if amount_to_be_borrowed < 2 else "books"}"
                    else:
                        return f"\n{book_name}: {amount_available}. available is less than amount requested. Please try request less amount"
                else:
                    return f"\n{borrow_name} is not available for borrowing now. Please try some other time"
        else:
            return f"\nWe dont have {borrow_name} yet."
                
    def borrowed_books(self):
        for borrower, books in self.borrowed.items():
            print(f"{borrower} : {books}")
        
                    
    def display_shelf(self):
        print(self.shelf)
        
    def return_book(self, book):
        book_name = book["name"]
        returner = book["returner"]
        count = book["count"]
        
        if returner in self.borrowed: 
            books = self.borrowed[returner]
            
            for book in books:
                count_of_borrowed_book = book["count"]
                if book_name == book["name"]:
                    if  count_of_borrowed_book < count:
                        print(f"{book_name} borrowed : {count_of_borrowed_book} is lesser than amount being returned: {count}. please make adjustments")
                        break
                    else:
                        book["count"] -= count
                        if book["count"] == 0:
                            del self.borrowed[returner]
                            print("Youve successfully returned all the books you borrowed")
                            break
                        else:
                            print(f"Youve returned {count} of the books you borrowed. you have {book["count"]} left")
            else:
                print(f"{book_name} not found in the records of books borrowed")
                
        else:
            print(f"{returner} hasnt borrowed any book from the library")
    



