import csv
import string

from flask import Flask
app = Flask(__name__)

def get_securities():
	content = ''
	url = 'http://business.customer.gatrixx.com/planspiel/192/chartNG.gfn?language=en&style=1&height=250&width=485&chartType=8&languageIsoalpha2=en&time=300&subProperty=2&average=38~linear&average=200~linear&instrumentId='

	with open('securities.csv', 'rb') as data:
		reader = csv.reader(data, delimiter=',')
		for row in reader:
			content += "<div><img src='" + url + row[2]+"'/></div>"
	
	return content

@app.route('/')
def main():
	with open('index.html', 'r') as page:
		page_text = page.read()
		return string.replace(page_text, 'CONTENT', get_securities())

if __name__ == "__main__":
	app.run()
