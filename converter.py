import requests
import sys

TOKEN = '116347f556a56fe44fcba5b8'
URL = 'https://v6.exchangerate-api.com/v6/'

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Type {} [sum] [currency code from] [currency code to]".format(sys.argv[0]))
	else:
		old_sum = float(sys.argv[1])
		cur_old = sys.argv[2].upper()
		cur_new = sys.argv[3].upper()

		currency = requests.get(URL+TOKEN+'/pair/{}/{}'.format(cur_old,cur_new))
		currency = currency.json()
		
		if currency['result'] == 'error':
			print("An error has occured!")
			print("Error type: {}".format(currency['error-type']))
		elif currency['result'] == 'success':
			new_sum = old_sum * currency['conversion_rate']
			print("{} {} = {} {}".format(old_sum,cur_old,new_sum,cur_new))
			print("Last update:")
			print(currency['time_last_update_utc'])
		else:
			print("An unknow error has occured!")
			print(currency)