import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from .config import data_path, top_books


class BookData(object):
    '''Given a book ID, retrieves relevant metadata'''
    def __init__(self, book_id: int):
        '''Load information about a given book'''
        self.book_id = book_id
        metadata_csv = pd.read_csv(os.path.join(data_path, top_books))
        self.record = metadata_csv[metadata_csv['source_book_id'] == book_id]
        self.pull_record = lambda field: self.record[field].iloc[0]
        self.retrieve_metadata()
        self.retrieve_cover()

    def retrieve_metadata(self):
        '''Pull the book's metadata records'''
        self.title = self.pull_record('source_title_desc')
        self.year = self.pull_record('published_year')
        self.author = self.pull_record('source_person_desc')
        self.publisher = self.pull_record('publisher_names')
        self.rating = self.pull_record('user_rating_avg')
        self.rating_count = self.pull_record('person_user_rating_cnt')
        self.book_url = self.pull_record('source_book_url')
        self.record_rating = 100 - int(
            self.pull_record('user_ratings_rank') * 100)
        self.synopsis = self.pull_record('description')

    def retrieve_cover(self):
        '''Pulls the book's cover art'''
        record_url = self.pull_record('source_book_url')
        r = requests.get(record_url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find("img", id="coverImage")
        self.image_url = links["src"]