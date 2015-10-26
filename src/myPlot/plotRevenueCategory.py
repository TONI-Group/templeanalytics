#!/usr/bin/env python
import logging

# Pandas DataManagement
import pandas as pd

# Plotly Graphing
import plotly.plotly as py
import plotly.graph_objs as go

def plot(rawData):
    logging.info("Creating product Revenue vs Product Category Plot")

    # ----------------
    # - LOAD IN DATA - 
    # ----------------
    logging.info("Loading in data...")
 
    # For this plot we need customer, order, and product category data
    #
    rawData.loadCustomer()
    rawData.loadOrder()
    rawData.loadProduct()

    # Finish Loading in data
    #
    logging.info("Done loading data")

    # -------------------
    # - REORGANIZE DATA - 
    # -------------------
    logging.info("Reorganizing data...")
    
    # Combine Order Number and Customer Number
    #
    customerOrder = pd.merge(rawData.orderList, rawData.customerList, 
            left_on='CUSTOMER_NBR', right_index=True, sort=False)
    
    logging.debug(customerOrder)
    
    # Combine Orders and Product Categories
    #
    customerOrderDescr = pd.merge(customerOrder, rawData.productDescr,
             on='PRODUCT_NBR', sort=False)
    
    logging.debug(customerOrderDescr)

    # Finish Organizing in data
    #
    logging.info("Done reorganizing data")
    
    # --------------
    # - QUERY DATA - 
    # --------------
    logging.info("Querying data...")
    
    # Create a sub-set of the data
    #
    customSub = customerOrderDescr.loc[:,
            ['PRODUCT_CATEGORY', 'TOTAL_LINE_AMT']]

    # Create Multi-Index Dataset
    #
    customSub = customSub.groupby('PRODUCT_CATEGORY').sum()

    # Remove non-aplicable columns
    #
    customSub = customSub.drop(['Returns', 'PUBLIC RELATION'])
    
    logging.debug(customSub)
    
    # Finish Organizing in data
    #        
    logging.info("Done querying data")
    
    # -------------
    # - PLOT DATA - 
    # -------------
    logging.info("Plotting...")
     
    # Plot Layout
    #
    layout = go.Layout(
            title='Revenue per Product Category',
            yaxis=dict(
                title='Revenue (USD $)'
            )
    )
    
    # Define the figure using playout and data. Plot After
    #
    data = [
            go.Bar(
                x=customSub.index,
                y=customSub['TOTAL_LINE_AMT']
            )
    ]
    
    fig = go.Figure(data=data,layout=layout)
    url = py.plot(fig, 
            filename='templeAnalytics2015/Revenue_vs_Product_Category')    
                
    # Finish Plotting in data
    #   
    logging.info("Done plotting product Revenue vs Product Category Plot")
