import nltk
from nltk.classify import apply_features

def get_classifier(train_set, test_set, features):
  train_set = apply_features(features, train_set)
  test_set = apply_features(features, test_set)
  classifier = nltk.NaiveBayesClassifier.train(train_set)
  print "Accuracy is ", (nltk.classify.accuracy(classifier, test_set) * 100), '%'
  return classifier


