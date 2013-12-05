import sys
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict, Counter
import networkx as nx
import re


stopwords = set(stopwords.words('english'))

def textrank_sentences(article):

  G = nx.Graph()
  # Add all sentences to the graph, index is node name
  G.add_nodes_from([index for index,sent in enumerate(article)])

  bag_of_words = defaultdict(list)
  # Build a bag of words where a word
  # is associated to the sentence indexes it belongs to
  # word => [(sentence index, wordfreq)]
  for index, sentence in enumerate(article):
    words = Counter([word for (word,_) in sentence])
    for word, freq in words.items():
      if word in stopwords: continue # don't count stopwords
      bag_of_words[word].append((index, freq))

  # Loop through sentences and add the edges
  for index, sentence in enumerate(article):
    for word, pos in sentence:
      for sent_index, weight in bag_of_words[word]:
        if sent_index == index: continue # no edges to self
        G.add_edge(index, sent_index, weight=weight)

  pageranked_sents = nx.pagerank(G)
  sentence_ranks = [index for index in sorted(pageranked_sents, key=pageranked_sents.get, reverse=True)]

  return sentence_ranks


def gen_summary_from_ranks(ranks, article, num_sentences=3):
  sents = ranks[:num_sentences]
  # order by appearance in text
  sents.sort()
  summary = ' '.join([word for index in sents for (word,_) in article[index]])
  return summary


# Fix some tokens that have spaces after rejoining:
def clean_summary(summary):
  summary = summary.replace(' ,', ',')
  summary = summary.replace(' .', '.')
  summary = summary.replace(' !', '!')
  summary = summary.replace(' ?', '?')
  summary = summary.replace('( ', '(')
  summary = summary.replace(' )', ')')
  return summary


def summarize(article, raw=False, rank_sentences=textrank_sentences, length=3):
  if raw:
    article = preprocess_raw_article(article)
  ranks = rank_sentences(article)
  summary = gen_summary_from_ranks(ranks, article, length)
  return clean_summary(summary)

def preprocess_raw_article(article):
  return [[(word, None) for word in word_tokenize(sentence)] for sentence in  sent_tokenize(article)]


if __name__ == "__main__":
  with open(sys.argv[1]) as f:
    length = 3
    if len(sys.argv) > 2: length = int(sys.argv[2])
    print summarize(f.read(), raw=True, length = length)





