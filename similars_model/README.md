
# Technical Overview

The AIgent uses a pretrained BERT Transformer model to project pitch submissions into a high-dimensional embedding space. The pitch embedding can then be leveraged in two ways: (1) to query against a large database of other book embeddings, retrieving similar titles, and (2) as input to a trained text classifier, to identify the submission's genre.

## Similar Titles
In its design, the AIgent is similar to a content-based filtering recommender system. It runs over an embeddings database trained on GoodReads synopses, and linked to title metadata. At inference, a new submission can be queried, returning similar titles, genres, and sales proxies. This data can help literary agents rapidly evaluate pitches, identifying whether a pitch falls into the group of genres or economic metrics that they prefer. 

Notably, because the recommender system is content-based, rather than collaborative, it does not suffer from popularity bias; it is therefore an appropriate prediction tool for similar titles, irrespective of their popularity. If popularity is an important dimension, post hoc filters could be implemented to surface the most popular titles first.

## Genre Prediction
Pitch submissions are also run through a text classifier, that outputs their predicted genre. For this task, the AIgent leverages logistic regression models trained on >100k books synopses (vectorized with BERT) as input, and weighted genre labels as output. Genre labels were sourced from Goodreads and were weighted by label incidence (i.e., for a given book, the proportion of user-generated labels belonging to that class).
