# CNNs for Text Classification

## Mentors 👨‍🏫:
- [@Mrinal](https://github.com/themrinaal)
- [@Alice](https://github.com/atol)

## Overview 🕵️:
This project focuses on leveraging Machine Learning, especially Natural Language Processing (NLP), to classify text. Students will implement and train a one-dimensional (1D) convolutional neural network (CNN) that takes a text input and outputs a class label for the text.

## Datasets 📊:
### Toxic Comments
Identify hate speech by classifying comments as `toxic` or `not toxic`.

*Disclaimer: This dataset contains text that may be considered profane, vulgar, or offensive.*

### IMDB Movie Reviews
Classify the sentiment (`negative` or `positive`) of movie reviews.

Students are encouraged to try out other datasets of interest and to extend the task to multi-class text classification.

## Bonus 🏆:
As a bonus task, students can write a script that uses the trained model to classify user input in real-time.

## Requirements 📝:
- Laptop/PC
- Access to stable Internet
- [Google Collaboratory](https://colab.research.google.com)

## Setup ⚙️:
1. Install all the necessary libraries. Type following command in your Jupyter Notebook:
```
!pip install -r requirements.txt
```
2. Install Glove 
```
!wget http://nlp.stanford.edu/data/glove.6B.zip
````
3. Unzip Glove
```
!unzip -q glove.6B.zip
```

## References
* [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
* [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
```
@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = {http://www.aclweb.org/anthology/P11-1015}
}
```
