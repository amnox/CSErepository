from nltk.book import *

"""def custom_tags(prompt_type):
	if prompt_type=='search':
		return 'search using concordance()'+'\n'
	elif prompt_type=='c_cntxt'
		return 'Shared context of words'+'\n'
	else: 
		return 'error'
print custom_tags('search')
print text1.concordance("monstrous")
print custom_tags('c_cntxt')
print text2.common_contexts(["monstrous","very"])
print "length of a string"
print len(text3)
v=set(text1)
long_words=[w for w in v if len(w)>15]
print "List of all long words"
print sorted(long_words)"""
fdist5=FreqDist(text5)
#w=[word for word in set(text5) if len(word)>7 and fdist5[word]>7]
for w1 in fdist5: print fdist5[w1]

