import heapq
from nltk.corpus import brown

news_fileids = brown.fileids(categories='news')

articles = [brown.tagged_sents(fileids=id, simplify_tags=True) for id in news_fileids]

def rank_sentences(article):
  ranks = []
  for index, sentence in enumerate(article):
    score = -len([word for (word, pos) in sentence if pos == 'NP'])
    heapq.heappush(ranks, (score, index, sentence))

  return ranks

def gen_summary_from_ranks(ranks, n=3):
  sents = []
  for i in range(n):
    sents.append(heapq.heappop(ranks))
  sents.sort(key=lambda x: x[1]) # order by appearance in text
  summary = ' '.join([word for sent in sents for (word, pos) in sent[2]])
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



def gen_summary(article):
  ranks = rank_sentences(article)
  summary = gen_summary_from_ranks(ranks)
  return clean_summary(summary)







