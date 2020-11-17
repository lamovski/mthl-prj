# -*- coding: utf8 -*-
import re
import nltk
from nltk.corpus import stopwords
from string import punctuation

txt = 'Не угощай и не потчевай никого, а веди себя лучше так, чтобы тебя угощали, а больше всего береги и копи копейку: эта вещь надежнее всего на свете. Товарищ или приятель тебя надует и в беде первый тебя выдаст, а копейка не выдаст, в какой бы беде ты ни был. Все сделаешь и все прошибешь на свете копейкой.'

sentences = nltk.sent_tokenize(txt, 'russian')
print('Самое длинное предложение:', max(sentences))
print('Самое короткое предложение:', min(sentences))

nptxt = txt.lower()
nptxt = re.sub("[\,\.]", "", nptxt)

words = nltk.word_tokenize(nptxt, 'russian')
print('Самые частые слова со стоп-словами:', nltk.FreqDist(words).most_common(3))

nswords = [word for word in words if word not in stopwords.words('russian')]

print('И без:', nltk.FreqDist(nswords).most_common(3))

print(nltk.pos_tag(nswords, lang = 'rus'))

print(list(nltk.FreqDist(nltk.bigrams(nswords)).most_common(3)))
