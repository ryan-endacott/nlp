import heapq
from nltk.corpus import brown

news_fileids = brown.fileids(categories='news')

news_article = brown.tagged_sents(fileids = news_fileids[0], simplify_tags=True)

def rank_sentences(article):
  ranks = []
  for index, sentence in enumerate(article):
    score = 0
    for word in sentence:
      if word[1] == 'NP': score -= 1 # proper noun, lower is better
    heapq.heappush(ranks, (score, index, sentence))

  return ranks

def gen_summary_from_ranks(ranks, n=3):
  sents = []
  for i in range(n):
    sents.append(heapq.heappop(ranks))
  sents.sort(key=lambda x: x[1]) # order by appearance in text
  return ' '.join([word[0] for sent in sents for word in sent[2]])

def gen_summary(article):
  ranks = rank_sentences(article)
  return gen_summary_from_ranks(ranks)







