import string
def preprocessText(text,punctuationList,stopwordsSet):
 text=text.lower()
 text=''.join([c for c in text if c not in punctuationList])
 text=' '.join([w for w in text.split() if w not in stopwordsSet])
 return text
def analyzePosts(postsList,punctuationList,stopwordsSet,positive,negative):
 processed=[]
 for p in postsList:
  clean_text=preprocessText(p['text'],punctuationList,stopwordsSet)
  s=0
  for w in clean_text.split():
   if w in positive:s+=1
   elif w in negative:s-=1
  processed.append({'id':p['id'],'text':p['text'],'score':s})
 return processed
def getFlaggedPosts(scoredPosts,sentimentThreshold=-1):
 return [p for p in scoredPosts if p['score']<=sentimentThreshold]
def findNegativeTopics(flaggedPosts):
 negTopics={}
 for p in flaggedPosts:
  for w in p['text'].split():
   if w.startswith('#') or w.startswith('@'):
    tag=''.join([c for c in w if c.isalnum() or c in ['#','@']])
    if tag not in negTopics:negTopics[tag]=1
    else:negTopics[tag]+=1
 return negTopics
allPosts=[
 {'id':1,'text':'I LOVE the new #GuLPhone! Battery life is amazing.'},
 {'id':2,'text':'My #GuLPhone is a total disaster. The screen is already broken!'},
 {'id':3,'text':'Worst customer service ever from @GuLPhoneSupport. Avoid this.'},
 {'id':4,'text':'The @GuLPhoneSupport team was helpful and resolved my issue. Great service!'}
]
PUNCTUATION_CHARS='''!"#$%%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
STOPWORDS_SET={'i','me','my','a','an','the','is','am','was','and','but','if','of','to','at','by','for','with','this','that'}
POSITIVE_WORDS_SET={'love','amazing','great','helpful','resolved'}
NEGATIVE_WORDS_SET={'disaster','broken','worst','avoid','bad'}
processed=analyzePosts(allPosts,PUNCTUATION_CHARS,STOPWORDS_SET,POSITIVE_WORDS_SET,NEGATIVE_WORDS_SET)
flagged=getFlaggedPosts(processed,sentimentThreshold=-1)
topics=findNegativeTopics(flagged)
print("Flagged Posts:",flagged)
print("Negative Topics:",topics)
