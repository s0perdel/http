import requests
from bs4 import BeautifulSoup
import time
import os

URL = 'https://qna.habr.com/q/1096502'

def main():
	os.system('color 02')
	answers = 0
	querys = 0
	while answers == 0:
		querys += 1
		api = requests.get(URL)
		parser = BeautifulSoup(api.text, 'html.parser')
		answers = parser.find('div','question__additionals')
		answers = answers.find('meta')
		answers = int(answers['content'])
		views = parser.find('span', 'question__views-count question__views-count_full')
		views = views.text.replace('\n','').strip()
		views = views.split(' ')
		views = int(views[0])
		print('ANSWERS: {}, VIEWS: {}, REQUESTS: {}'.format(answers,views,querys))
		time.sleep(3)
	print('\a')
	print('[OK] ANSWERS: %s' % answers)
	print('\a')
	os.system('pause')



if __name__ == '__main__':
	main()