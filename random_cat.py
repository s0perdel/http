import requests # собственно HTTP запросы
import sys # аргументы файла (при запуске из cmd)
import random # для рандомных котов
from PIL import Image # открытие изображения
from urllib.request import urlopen # сохранение изображения по URL

def get_the_cat(num):
	num = int(num)
	if num < 1 or num > 58: # на сайте всего 58 котов)))
		return None
	else:
		cat = requests.get('https://thatcopy.pw/catapi/restId/{}'.format(num)) # получение json о коте
		return cat.json()

def show_the_cat(cat):
	image = Image.open(urlopen(cat['url'])) # собственно показ кота
	image.show()


if __name__ == "__main__":
	if len(sys.argv) < 2:
		CAT_ID = random.randint(1,58) # если не передали аргументом при запуске файла id, то кот рандомный
	else:
		CAT_ID = sys.argv[1] # если передали, то берем id
	kitty = get_the_cat(CAT_ID) # переменная кота))
	show_the_cat(kitty) # показ кота
	print(kitty['id']) # вывод id кота