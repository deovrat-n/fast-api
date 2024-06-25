from fastapi import FastAPI
app= FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")  
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_book():
    return {'book_title':'My fav book'}

@app.get("/books/{book_title}")#dynamic params 
async def read_book(book_title: str):
    return {'book_tit':book_title}


# @app.get("/books/mybook")
# async def read_book():
#     return {'book_title':'My fav book'}
'''if this function get called it will behave 
like the upper one to avoid this we can initialize it
above the "/books/{book_title}" decorator  '''