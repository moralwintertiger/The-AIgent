# Modeling Notebooks

## The AIgent: Text Classifiers
The purpose of this notebook is to build regressors to predict genre tags from BERT embeddings of synopses. Several classifier models are explored. Each uses as its features a set of BERT embeddings; labels are genre tags. Note that these genre tags are user-generated from Goodreads members. Because of this they have weights attached that can be used to set thresholds of class (i.e., genre) membership.

Several classification strategies are common for text, including support vector machines, naive Bayes, and logistic regression. Each of these models is tested for accuracy and F1 scores across genres. Datasets are balanced prior to training for a particular genre tag, and only synopses with >1000 user tags are used in model building. In order to maintain the extensibility of the AIgent (i.e., to allow for new genre incorporation and to fine-tune genre classifiers), I have used a one-versus-all approach and have built an independent classifier for each genre.

Not all feature experimentation is included in this notebook. In other notebooks, I have tested the effect of synopsis length on classifier strength, seeking to set a balance between the speed of the model (which slows with longer synopses) and the robustness of the model (which slowly increases with longer synopses).


