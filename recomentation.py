# Importando bibilotecas
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

books = pd.read_csv('SistemaRecomendacão\BX-Books.csv', sep=';', encoding='latin-1',
                    on_bad_lines='warn', low_memory=False)
users = pd.read_csv('SistemaRecomendacão\BX-Books.csv', sep=';',
                    encoding='latin-1', on_bad_lines='skip')
ratings = pd.read_csv('SistemaRecomendacão\BX-Book-Ratings.csv', sep=';',
                      encoding='latin-1', on_bad_lines='skip')
books = books[['ISBN', 'Book-Title', 'Book-Author',
               'Year-Of-Publication', 'Publisher']]
books.rename(columns={'Book-Title': 'title', 'Book-Author': 'author',
                      'Year-Of-Publication': 'year', 'Publisher': 'publisher'}, inplace=True)
users.rename(columns={'User-ID': 'user_id',
             'Location': 'location', 'Age': 'age'}, inplace=True)
ratings.rename(columns={'User-ID': 'user_id',
               'Book-Rating': 'rating'}, inplace=True)
ratings['user_id'].value_counts()
