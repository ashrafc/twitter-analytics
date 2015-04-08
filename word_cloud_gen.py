from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv

# Read the whole text.
with open('tweet_data.csv', 'rb') as f:
	mycsv = csv.reader(f)
	for row in mycsv:
		text = row[0]
		joined_text = ''.join(text)


no_urls_no_tags = " ".join([word for word in joined_text.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and word != 'RT'
                            ])
print no_urls_no_tags


wordcloud = WordCloud().generate(no_urls_no_tags)
# Open a plot of the generated image.
plt.imshow(wordcloud)
plt.axis("off")
plt.show()