from typing import List

# data_path: str = '../production-ready-data/'
# lr_path: str = '../production-ready-data/log-reg-models/'

#data_path = '/home/ubuntu/agent-python3/production-ready-data/'
#lr_path = '/home/ubuntu/agent-python3/production-ready-data/log-reg-models/'

data_path = '/Users/ryan/Projects/Insight/insight/Agent-2/agent-2/streamlit-agent/production-ready-data/'
lr_path = '/Users/ryan/Projects/Insight/insight/Agent-2/agent-2/streamlit-agent/production-ready-data/log-reg-models/'

book_ids: str = "full-ids-genretags-OHE-synopses-df-m9668-n20.csv"

features: str = "full-features-array-m9668-n20.npy"

bert_model: str = "distilbert-base-uncased"

top_books: str = "goodreads_top40k_with_ranks.csv"

genre_list: List = [
    'romance', 'mystery', 'science-fiction', 'erotica', 'historical-fiction',
    'paranormal', 'fantasy', 'adult-fiction', 'chick-lit',
    'contemporary-romance', 'contemporary', 'new-adult', 'suspense',
    'thriller', 'womens-fiction', 'young-adult'
]
