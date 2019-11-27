import spacy

print("Hi")

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple is looking at buying U.K. startup for $1billion on 25/11/2018' )
doc1=nlp(u'dog cat banana')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

"""
for token1 in doc1:
    for token2 in doc1:
        print(token1.text, token2.text, token1.similarity(token2))
"""

# Process whole documents
text = (u"When Sebastian Thrun started working on self-driving cars at "
        u"Google in 2007, few people outside of the company took him "
        u"seriously. “I can tell you very senior CEOs of major American "
        u"car companies would shake my hand and turn away because I wasn’t "
        u"worth talking to,” said Thrun, now the co-founder and CEO of "
        u"online higher education startup Udacity, in an interview with "
        u"Recode earlier this week.")
doc2 = nlp(text)

# Find named entities phrases and concepts
for entity in doc2.ents:
    print(entity.text, entity.label_)

# Determine semantic similarities
doc3 = nlp(u"my fries were super gross")
doc4 = nlp(u"such disgusting fries")
similarity = doc3.similarity(doc4)
print(doc3.text, doc4.text, similarity)

f1 = open("testfile.txt","rt")
text1 = f1.read()
print(text1)

doc5 = nlp(text1)

# for ent1 in doc5.ents:
#     print('doc5 :', ent1.text, ent1.lemma_, ent1.label_)

for word in doc5:
    print('doc5 :', word.text, word.lemma_, word.shape_, word.tag_)
    # print('doc5 :', word, word.lemma_, word.shape_)

# for ent1 in doc5.ents:
#     print(ent1.text, ent1.lemma_, ent.tag_, ent.dep_, ent.shape_,
#     ent.alpha_, ent1.label_)
