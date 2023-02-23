from urllib.request import urlretrieve
import pandas as pd
import os


FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download = False):
	"""Download and cache Fremont bridge bike data 

	Args:
		filename (str, optional): _description_. Defaults to 'Fremont.csv'.
		url (str, optional): _description_. Defaults to FREMONT_URL.
		force_download (bool, optional): _description_. Defaults to False. If True, force redownload of data

	Returns:
		data : pandas.DataFrame
			The fremont bridge data
	"""	

	if force_download or not os.path.exists(filename):
		urlretrieve(URL, filename)
	data = pd.read_csv('Fremont.csv', index_col ='Date', parse_dates=True)
	data.columns = ('Total', 'East', 'West')
	#data['Kok'] = data['West'] + data['East']
	return data
	


