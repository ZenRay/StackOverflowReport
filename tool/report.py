"""Data Analysis
    purpose: module to analysis the data
"""

# load essential package
import pandas as pd
import numpy as np

def count_values(data, column, split_option=";"):
    """ Count the checkbox values being wrapped by sting

    Parameters:
        data: DataFrame
            An original data is dataframe
        column: string
            Column in data, will be parsed
        split_option: string default ";"
            Use to split the value in column

    Results:
        labels: set
            A set contains the checkbox option
        label_count: dict
            A dict contains label as key, amount as value
        colors: list optional
            Convert the label amount to a matplotlib color value
    """
    labels = set()
    label_count = dict()

    for i in data[column]:
        if pd.notna(i):
            # update labels
            tem = set(i.split(split_option))
            labels |= tem

        for label in tem:
            if label_count.get(label, 0) == 0:
                label_count[label] = 1
            else:
                label_count[label] +=1

    return labels, label_count

