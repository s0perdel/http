from bs4 import BeautifulSoup
import requests

URL = 'https://habr.com/ru/news/'

def main():
	api = requests.get(URL)
	parser = BeautifulSoup(api.text, 'html.parser')
	blocks = parser.find_all('article','tm-articles-list__item')
	for article in blocks:
		title = article.find('h2', 'tm-article-snippet__title tm-article-snippet__title_h2')
		title = title.find('span')
		time = article.find('span','tm-article-snippet__datetime-published')
		time = time.find('time')
		time = time['title']
		views = article.find('span','tm-icon-counter__value')
		print(time+' | ', views.text+' views | ', title.string)


if __name__ == '__main__':
	main()