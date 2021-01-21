from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
	source=requests.get('https://www.livefpl.net/leagues/935876').text

	soup=BeautifulSoup(source,"html.parser")

	Shiva=['Suraj Kulkarni','josson thoppil', 'Tarun Hegde','Bharadwaj M']
	diff=0

	for player_info in soup.find_all('tr',class_="clickable"):

		data= player_info.find_all('td')
		points=int(data[5].text)+int(data[6].text)
		if data[2].text in Shiva:
			diff+=points
		else:
			diff-=points

	return render_template('index.html', diff=diff)

if __name__=="__main__":
	app.run(debug=True)