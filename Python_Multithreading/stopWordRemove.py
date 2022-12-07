from nltk.corpus import stopwords

def stopWordRemove_bulma(satir):
		text = satir.split()
		swRemovedText = []
		stop_words=list(stopwords.words('english'))
		kelimeList1 = []
		for k in text:
			kelimeList1 = k.split()
			for a in kelimeList1:
				if a not in stop_words:
					swRemovedText.append(a)
		swRemovedText = ' '.join(swRemovedText)
		return swRemovedText