import requests
from bs4 import BeautifulSoup

# Get the sites information (the HTML code) and store it in a variable
def getSiteData():

	url = "https://www.nytimes.com/"
	result = requests.get(url)
	return result




def main():

	siteData = getSiteData()
	rawHtml = siteData.text

	# Use BeautifulSoupl to parse html 
	soup = BeautifulSoup(rawHtml, "html.parser")

	# Open file to write to
	f = open("article_titles.txt","w+")
	text = ""

	# find all the story-heading tags (these contain titles for articles)
	for link in soup.find_all(class_="story-heading"):
		
		# for titles that are links extract the text
		# for others get the first child of the parent tag and store in variable
		try:
			if link.a:
				
				text =link.a.text.strip().encode("utf-8")
				# text =link.a.text.replace("\n", " ").strip().encode("utf-8")
				# print(text)
				f.write(text)
			else: 
				
				text = link.contents[0].strip().encode("utf-8")
				# print(text)
				f.write(text + "\n")
		except Exception, e:
			print "There was an issue %s" % e
			print(link)

	f.close()



if __name__ == "__main__":
	main()