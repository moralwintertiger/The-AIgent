
# Data Overview

* Each dataset has 9338 records (not 9668). 
* Datasets were generated 01/25/2020. 
* Datasets are not currently hosted as of 03/05/2020. Please reach out for more information.

## full-ids-genretags-OHE-synopses-df-m9668-n20.csv

This dataset was scraped from Goodreads. Following scraping, only records with >1000 genre tags and only records from 2014-2019 were kept. Each row contains 20 columns corresponding to one-hot-encodings of the 20 most common genre tags, with certain tags like ‘fiction’ and ‘audiobook’ removed. There is also a ‘synopsis’ column. To pre-process for BERT, any synopsis with more than 240 tokens was removed, culling this dataset to 9338 records from an initial size of ~17500. 

Note that a token length of 240 had the best accuracy and F1 scores (against genre tags in a logistic regression test) for m=1000 instances. Longer records require higher compute resources. Also some metric will need to be developed to handle token length >512, in order to expand this to the full Goodreads portfolio.

## full-features-array-m9668-n20.npy

This dataset was produced by tokenizing each synopsis from the pandas df above, using distilBERT. Dataset is a numpy array of size = 9338x768. Each column relates to the output from the final hidden layer of the distilBERT pre-trained model (uncased). Only CLS tokens were Kept for this dataset, i.e. each column is a full sentence (or paragraph)-level embedding. Note that these data do not include item IDs. But the indices are shared between this dataset and the other datasets. 

## full-ids-genretags-WE-synopses-df-m9668-n20.csv

This dataset is the same as the full-ids-genretags-OHE-synopses-df-m9668-n20.csv dataset, except that for each column of genre tags, values are not one-hot-encoded. Rather, each value represents the proportion of the total number of tags for the title that occurred in each genre. Ie if there were 1000 user tags total and 800 were in the ‘suspense’ category, then the suspense value = 0.8.

## full-ids-synopses-df-m9668-n20.csv

This dataset is a reduction from (1) and (3): it only contains title IDs and synopses. 
