#!/usr/bin/env python
#-*-coding: utf-8 -*-
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

def bar_plot_option(label_count, top=None, color_option=None, value_option=False):
    """ Deal with label count
    deal with the label_count, so that can be used to plot 
    Parameters:
        label_count: dict
            the data is parse from the specific column. Key is label, value is 
            ammount number
        top: int default None
            Specify the top level value, which check the option amount. If it is
            None, return labels that is a index
        color_option: list default None
            A color list will be used to convert the label amount. Caution last
            element is default color
        value_option: boolean default False
            If True, concate the value formated to labels
    
    Result:
        labels: ndarray or list
            It is used to plot that is a argument labels
        colors: list optional value
            It is used to plot that is a argument colors
    """
    series = pd.Series(label_count).sort_values()
    labels = []
    colors = []
    choose_option = 0

    if not top:
        labels = series.index
        return labels
    # top is not None
    for label, condition in \
        zip(
            series.index, 
            series.apply(lambda x: True if x in series.nlargest(top).values else False)
        ):

        if condition:
            colors.append(color_option[choose_option])
            choose_option += 1
            # update the label with format value
            if value_option:
                value = "\n{:0.2f}%".format(series.loc[label] / series.sum() * 100)
                labels.append(label + value)
            else:
                labels.append(label)
        else:
            labels.append("")
            colors.append(color_option[-1])
            
    return labels, colors