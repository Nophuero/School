# -*- coding: utf-8 -*-
"""Data_Visualization_Python_Stock_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BhBTlM5DMC_p2OPslXS5_dPvsFgxqpQy
"""

# Install the yFinance Python library
!pip install yfinance

import yfinance

# Set the start and end date
start_date = '2008-01-05'
end_date = '2023-8-30'

# Set the ticker (stock quote)
ticker = 'AMZN'

# Get the data
data = yfinance.download(ticker, start_date, end_date)

# Print last 5 rows of data set
data.tail()

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot adjusted close price data
plt.plot(data['Open'])
plt.show()

"""# Adding Special Effects to the Chart"""

#Color can be green (g),
#Dashed line can be drawn using '__' and a square can be drawn using "s",
#Circle is drawn using "o" , Traingle is drawn using ^
# Plot the adjusted close price

plt.figure()
plt.plot(data['Adj Close'], 'g^')
#plt.plot(data['Adj Close'], 'b*')
#plt.plot(data['Adj Close'], 'y_')
#plt.plot(data['Adj Close'], 'yo')

# Define the label for the title of the figure
plt.title("Adjusted Close Price " )

# Define the labels for x-axis and y-axis
plt.ylabel('Price of Amazon')
plt.xlabel('Date')

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-', linewidth=0.5)

# Show the plot
plt.show()

#Also possible to have two things together as demonstrated below
plt.figure(1,figsize=(10,10))
plt.plot(data['Adj Close'], 'bs',data['Adj Close'], 'm')

# Define the label for the title of the figure
plt.title("Adjusted Close Price")

# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Month', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()

"""# Creating Group of charts on One chart"""

#Creating a group of charts
plt.figure(1,figsize=(12, 12))

#Entering information of title of the main image
plt.suptitle("Information")

#First Cell
plt.subplot(221)
# Plot the high price
plt.plot(data['High'], color="purple")
# Define the label for the title of the figure
plt.title("High Price ")
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Month', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='orange', linestyle=':', linewidth=0.5)

#Second Cell
plt.subplot(222)
# Plot the low price
plt.plot(data['Low'],color="violet")
# Define the label for the title of the figure
plt.title("Low Price")
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Month', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='green', linestyle='dotted', linewidth=0.5)

#Third Cell
plt.subplot(223)
# Plot the close price
plt.plot(data['Close'], color="brown")
# Define the label for the title of the figure
plt.title("Close Price")
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Month', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='red', linestyle='dashed', linewidth=0.5)

#Fourth Cell
plt.subplot(224)
# Plot the adjusted close price
plt.plot(data['Adj Close'], color="pink")
# Define the label for the title of the figure
plt.title("Adjusted Close Price")
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Month', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

# Show the plot
plt.show()

