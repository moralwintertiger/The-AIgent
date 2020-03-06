import requests
from bs4 import BeautifulSoup
from typing import Tuple

def clean_text(input):
    return input.text.rstrip().lstrip()


class RetrieveData(object):
    '''Takes a book url as input and outputs book metadata'''

    def __init__(self, input_url: str):
        r = requests.get(input_url).text
        self.soup = BeautifulSoup(r, "html.parser")

    def get_title_name(self):
        self.title_name = clean_text(self.soup.find(id="bookTitle"))

    def get_author_name(self):
        self.author_name = clean_text(
            self.soup.find(id="bookAuthors")).replace('\n',
                                                      '').replace('by', '')

    def get_description(self):
        self.description = clean_text(self.soup.find(id="description"))

    def get_review(self):
        self.review = clean_text(self.soup.find(id="description"))
    
    def record_builder(self) -> Tuple[str, str, str, str]:
        self.get_title_name()
        self.get_author_name()
        self.get_description()
        self.get_review()
        return self.author_name, self.title_name, self.description, self.review
