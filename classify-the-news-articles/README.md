### Project Overview

 We are given references to news pages collected from a web aggregator in the period from 10-March-2014 to 10-August-2014. The resources are grouped into categories that represent pages discussing the same story. News categories included in this dataset include business(b); science and technology(t); entertainment(e); and health(h).
The goal is to predict which class a particular resource belongs to given the title of the resource.


### Learnings from the project

 Solving it will reinforce the following concepts of text analytics:

Preprocess text data with tokenization, stopword removal etc
Vectorize data using Bag-of-words and TF-IDF approaches
Apply classifiers (Logistic and Multinomial Naive Bayes) to perform multi-class classification


### Approach taken to solve the problem

 In this project, we are using various techniques of NLP. We are classifying the news articles into various kinds like business, health, etc. we are using various functions like label encoder to convert it into numerical form.


### Challenges faced

 The data provided for this project is all in text form so first of all, we have to convert it into machine recognizable form. Another thing is that we have to take of synonymy, ambiguity, anaphora resolution, etc. kind of issues. 


