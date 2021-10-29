# tpatja, nkrause323, alpen0, lixiang, user4431345, bin liu, Olas, JL20119, yalisovetskyAS, Arycoo (plus 10 more warriors)
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
