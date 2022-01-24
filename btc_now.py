import requests
import time
import matplotlib.pyplot as plt

TOKEN = '89e9615e6a43fda9660bc664146a3b9cf1bb83f0dafd67e1632e958a8a899177'
URL = 'https://min-api.cryptocompare.com/data/price'
PARAMS = {'fsym':'BTC', 'tsyms':'USD', 'extraParams':'BTC REAL-TIME MONITOR', 'api_key':TOKEN}

def main():
	plt.ion()
	api = requests.get(URL,params=PARAMS)
	response = api.json()

	get_time = [' '.join(time.ctime(time.time()).split(' ')[1:])]
	server_output = [api]
	usd = [float(response['USD'])]
	old_usd = [response['USD']]
	percent = [(usd[0]-old_usd[0])/usd[0]*100]
	status = ['----']

	print("Initializing....")
	plt.title('BITCOIN CURRENCY')
	plt.xlabel('Counting')
	plt.ylabel('USD')
	plt.grid(True)
	time.sleep(3)

	counter = 0
	number = [0]
	while True:
		print('{} | {} | {} | {} | {}'.format(get_time[counter],server_output[counter],usd[counter],status[counter],percent[counter]))

		number.append(counter+1)

		api = requests.get(URL,params=PARAMS)
		response = api.json()

		get_time.append(' '.join(time.ctime(time.time()).split(' ')[1:]))
		server_output.append(api)
		usd.append(float(response['USD']))
		old_usd.append(usd[counter])
		percent.append((usd[counter+1]-old_usd[counter+1])/usd[counter+1]*100)
		if percent[counter+1] > 0: status.append(' UP ')
		elif percent[counter+1] < 0: status.append('DOWN')
		else: status.append('----')

		plt.plot(number, usd, 'r')
		plt.show()
		plt.pause(1.5)

		counter += 1
		


if __name__ == '__main__':
	main()