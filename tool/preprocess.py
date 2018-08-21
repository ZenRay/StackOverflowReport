"""Data preprocessing
  purpose: handling the data, like dealing with the fields, add the missing 
           fields
"""
# load the essential packages
import pandas as pd
import numpy as np

def extract_data(data, columns):
	""" Extract the data contained columns
	Extract the data that is contained with columns, which can be used to
	analysis data in the next step

  	Parameters:
		data : pandas DataFrame
			An Original data is readed from pandas that is a raw information

		columns : list or tuple
			Column labels to use for extracting the information data from 
			raw data
	
	Results:
		result : pandas DataFrame
			An information data contains the columns

	Examples
	--------
	>>> df = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
	...                    columns=['a', 'b', 'c', 'd', 'e'])
	>>> extract_data(df, ['a', 'b'])
	    a   b
	0   2   8 
	1   4   2 
	2   1   0 
	3   5   1 
	4   6   0  
	"""
	# check the columns datatype
	if not isinstance(columns, (list, tuple)):
		raise "The columns type is %s, plz converte it to list or tuple" % type(columns)

	# filter the data by using columns
	try:
		result = data.filter(items=columns, axis=1).copy()
	except Exception as e:
		print(e)

	return result