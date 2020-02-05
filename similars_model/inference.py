import os
import torch
import numpy as np
import pandas as pd
from joblib import load
import transformers as ppb
from collections import namedtuple
from typing import List, Dict, Tuple
from sklearn.metrics.pairwise import cosine_similarity

from .config import data_path, lr_path, book_ids, features, genre_list, bert_model


class SimilarBooks(object):
    def __init__(self,
                 input_synopsis: str,
                 num_sim_titles: int = 5,
                 num_genres: int = 5):
        '''Load features, BERT tokenizer & model, logistic regression models, and data sets'''
        self.input_synopsis: str = input_synopsis
        self.num_sim_titles: int = num_sim_titles
        self.num_genres: int = num_genres
        self._feature_set: np.ndarray = np.load(
            os.path.join(data_path, features))
        self._ids_df: pd.DataFrame = pd.read_csv(
            os.path.join(data_path, book_ids))
        self._tokenizer = ppb.DistilBertTokenizer.from_pretrained(bert_model)
        self._model = ppb.DistilBertModel.from_pretrained(bert_model)
        self._lr_models: Dict = {
            genre: load(f'{lr_path}lr_clf{genre}.joblib')
            for genre in genre_list
        }
        self.tokenize_synopsis()
        self.matching_titles()
        self.matching_strengths()
        self.get_genre_tags()

    def tokenize_synopsis(self):
        '''Leverages the BERT model to tokenize the input title synopsis'''
        input_ids = torch.tensor(self._tokenizer.encode(
            self.input_synopsis)).unsqueeze(0)
        outputs = self._model(input_ids)
        self._featurized_text: np.ndarray = outputs[0][:, 0, :].detach().numpy(
        )

    def matching_titles(self):
        '''Queries synopsis against feature set and returns the ids of the n most similar titles'''
        self._cosine_map = [
            cosine_similarity([feat], self._featurized_text)
            for feat in self._feature_set
        ]
        top_matches = sorted(range(len(self._cosine_map)),
                             key=lambda x: self._cosine_map[x],
                             reverse=True)[:self.num_sim_titles]
        self.sim_title_ids: List[int] = list(
            self._ids_df.iloc[top_matches].id.values)

    def matching_strengths(self):
        '''Returns the association strength of the n most similar titles to the input title'''
        top_strengths = [k[0][0] for k in self._cosine_map]
        top_strengths.sort(reverse=True)
        top_strengths = top_strengths[:self.num_sim_titles]
        top_strengths = [f'{round(t*100,2)}%' for t in top_strengths]
        self.sim_strengths: Dict[int, float] = dict(
            zip(self.sim_title_ids, top_strengths))

    def get_genre_tags(self):
        '''Generates a list of the top 10 predicted genre tags and their corresponding likelihood'''
        Tag = namedtuple('Tag', 'genre strength')
        pred = lambda lr_model: lr_model.predict_proba(self._featurized_text
                                                       )[:, 1][0]
        lr_predictions_list = [
            pred(lr_model) for lr_model in self._lr_models.values()
        ]
        tag_predictions = dict(zip(genre_list, lr_predictions_list))
        self.top_tags = sorted(tag_predictions.items(),
                               key=lambda x: -x[1])[:self.num_genres]
        self.top_tags: List[Tuple] = [
            Tag(genre, f'{round(strength*100,2)}%')
            for genre, strength in self.top_tags
        ]
