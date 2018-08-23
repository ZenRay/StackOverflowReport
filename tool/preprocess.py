"""Data preprocessing
  purpose: handling the data, like dealing with the fields, add the missing 
           fields
"""
# load the essential packages
import pandas as pd
import numpy as np
import itertools

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
	
	Result:
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

def add_single(data, new_values:dict):
	""" Add information to the data contained columns
	add new values that stores in new columns, which can be used to
	analysis data in the next step

  	Parameters:
		data : pandas DataFrame
			An Original data is readed from pandas that is a raw information

		new_values : dict
			column lables stores in the keys, which contains single value
	
	Result:
		result : pandas DataFrame
			An information data contains the new fields

	Examples
	--------
	>>> df = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
	...                    columns=['a', 'b', 'c', 'd', 'e'])
	>>> add_single(df, {'c':5})
	    a   b	c
	0   2   8	5 
	1   4   2 	5
	2   1   0 	5
	3   5   1 	5
	4   6   0  	5
	"""
	result = data.copy()
	result[new_values.keys()[0]] = new_values.values()[0]

	return result

def convert_single_func(x, validate_values, value=np.nan, reg_option=False,
		missing_option=True):
	"""Convert function
	The function is used in the apply method, which can be converted the
	invalidate value into the value

	Parameters:
		x : 
			element in the Series data or in the DataFrame data
		validate_values : list or regex pattern
			store the validate values that don't need to be converted. If x is 
			in the sequece, x will be same.
			If the validate_values is a regex pattern, search the x by using the
			pattern
		value : int, string, boolean, default nan
			target value.If value is False, regex match value will be returned
		reg_option : boolean defalt False
			If True, validation_values must be a regex pattern.In order to 
			search the x by using the pattern
		missing_option : boolean default True
			If True, the missing value will be added in the validate values
	Result:
		value or x
	"""

	# whether add the original missing value into the validate_value
	if missing_option and not reg_option:
		validate_values.append(np.nan)

	# if x is missing value, return itself
	if pd.isnull(x):
		return x
	# whether the element x will be converted
	# regex pattern, if the value is boolean false, return the match value by regex
	if reg_option:
		if validate_values.search(x):
			if value:
				return value
			else:
				return validate_values.search(x).group()
		else:
			return x

	if x in validate_values:
		return x
	else:
		return value


def convert_list_funct(x):
	"""Convert function
	The function is used in the apply method, which can be get the first index 
	value about the element

	Parameters:
		x : 
			element in the Series data or in the DataFrame data. If it's list,
			return the first index value, or return the x itself
	"""
	if not isinstance(x, list):
		if pd.isnull(x):
			return x
	else:
		return x[0]