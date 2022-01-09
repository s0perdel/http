import requests
import time
from datetime import datetime
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdat

TOKEN = '89e9615e6a43fda9660bc664146a3b9cf1bb83f0dafd67e1632e958a8a899177'
URL = 'https://min-api.cryptocompare.com/data/v2/histoday'
params = {'fsym': 'BTC', 'tsym': 'USD', 'limit': 2000, 'api_key': TOKEN}

def main():
	api = requests.get(URL, params=params)
	print(api)
	response = api.json()

	print("Has warning: {}".format(response['HasWarning']))
	if response['Response'] != "Success":
		print(response['Response'])
		print(response['Message'])

	else:
		response = response['Data']
		print("Data from {} to {}".format(time.ctime(response['TimeFrom']),time.ctime(response['TimeTo'])))
		date, start, close, high, low, raw_date = [], [], [], [], [], []

		for part in response['Data']:
			raw_date.append(part['time'])
			date.append(time.ctime(part['time']))
			start.append(part['open'])
			close.append(part['close'])
			high.append(part['high'])
			low.append(part['low'])

		result = pandas.DataFrame({
			'DATE': date,
			'START': start,
			'CLOSE': close,
			'HIGH': high,
			'LOW': low
			})

		result.index.name = '№'
		print(result)

		days = mdat.DayLocator()
		months = mdat.MonthLocator()
		years = mdat.YearLocator()
		d_format = mdat.DateFormatter('%d-%m-%y')
		dates = []
		for a in raw_date:
			dates.append(datetime.fromtimestamp(a))

		fig, ax = plt.subplots()
		plt.plot(dates,result['HIGH'],dates,result['LOW'])
		ax.xaxis.set_major_locator(months)
		ax.xaxis.set_minor_locator(days)
		ax.xaxis.set_minor_locator(years)
		ax.xaxis.set_major_formatter(d_format)
		plt.title('BITCOIN DYNAMICS')
		plt.ylabel('USD')
		plt.grid(True)
		plt.legend(['the highest price', 'the lowest price'])
		plt.show()
			



if __name__ == '__main__':
	main()