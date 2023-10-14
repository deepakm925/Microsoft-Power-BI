# import all packages 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Reading into the CSV file
data = ("D:/Python-intergrated-with-BI/carmaxdata.csv")
dataset = pd.read_csv(data)


""" Below is the code used to plot the visualizations in Power BI. All the code
was tested and debugged here first before copied over to Power BI """ 


""" THe Dataset code used in Power BI Python script to visualize. """

# dataset = pandas.DataFrame(year, price, model, mileage, make, region, city, state)


""" FIRST PAGE IN REPORT: Code for visualization Top Cities of CarMax Distribution.
Plots a Barchart!""" 

sb.set(style="whitegrid")

# Setting indicies for the variable 'region' counts
popular_regions = dataset["city"].value_counts()
popular_regions_30_counts = popular_regions[:30]
indices = popular_regions_30_counts.index
top_30_regions = indices

# Setting up bar plot settings 
f, ax = plt.subplots(figsize=(8,9))
sb.set_color_codes("dark")
sb.barplot(x=popular_regions_30_counts, y=top_30_regions,
            color="blue", orient='h')

ax.set(title='TOP 30 Cities of CarMax distributors',
       ylabel="Cities Carmax Dealers ",
       xlabel="Count of Cars sold by CarMax")

plt.show()


""" SECOND PAGE IN REPORT: Code for Most Expensive Car prices over the Years. 
Plots a Scatterplot!""" 

# Finding the prices greater or equal to 48999
#Remember we do not use Magic Numbers the logic is applied to take half of the max price and use the data from there!
top_car_makes_overall = dataset[dataset["price"] >= 48999]

# filtering to apply it to all the features we need in relation to price creating a new dataframe 
dataset_filtered = top_car_makes_overall[['price', 'year', 'model', 'make' ]]


sb.scatterplot(data=dataset_filtered, x="year", y="price", hue="make", palette="deep")
plt.title(' Comparing Most Expensive Car Make prices over the years')

plt.show()


""" THIRD PAGE IN REPORT: Code for Revenue of Cars over the Years. 
Plots a Line Chart""" 

# Using a seaborn line plot
sb.lineplot(data=dataset, x="year", y="price", orient="x", 
            size=30)

plt.title('Revenue of Cars over the years')
plt.show()


""" FOURTH PAGE IN REPORT: Code for Average Price Make 
Plots a bar chart""" 

fig, ax = plt.subplots(figsize=(16,11))
g = sb.barplot(x='make', y='price', data=dataset, ci=None, ax=ax)
g.set_xticklabels(g.get_xticklabels(), rotation=90)
plt.title("Average Price of Car Make")
g.plot()
plt.show()

