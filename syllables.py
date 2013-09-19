from nltk.corpus import cmudict

d = cmudict.dict()

def max_syl(word):
  if word not in d: return None
  return max([len([y for y in x if y[-1].isdigit()]) for x in d[word]])


