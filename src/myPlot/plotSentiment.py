#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import cufflinks as cf

# Plotting template file
#

# Please give the filename of this plotting fuction a descriptive name
# Also when you have created a plotting function add it to the __init__
# list so it is included in the package.
# More info here:
# https://docs.python.org/2/tutorial/modules.html#importing-from-a-package
#

def plot(rawData):
    logging.info("Creating product Revenue vs Product Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # Use rawData to load in data required.
    # example: rawData.loadOrder
    rawData.loadSocial()
    # Finish Loading in data
    #
    logging.info("Done loading data")

    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
   
    #grab column Sentiment
    #
    #SentimentCol = rawData.socialList[['SENTIMENT']]
    #logging.debug(SentimentCol)
   
    #group by unique entries in column 'SENTIMENT'
    #add total count
    #
    sentimentCol = rawData.socialList.groupby('SENTIMENT').size()
    logging.debug(sentimentCol)
    
    # Combine Necessary Tables 
    # Use logging.debug(obj.DataFrame) to print contents of the resulting table
    #
    
    # Finish Organizing in data
    #
    logging.info("Done reorganizing data")
    
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
    
    # From the Table presumable created above, remove excess columns. Also
    # re-index a table to new column
    #
    
    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
    
    sentimentCol.iplot(kind='bar',yTitle="Number of Sentiment Type", title="Total number of Sentiment Feedback", filename='templeAnalytics2015/plotSentiment')
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue vs Product Category Plot")
