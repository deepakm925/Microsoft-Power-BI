<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/heading-python.png"/>

 # INTEGRATING A PYTHON SCRIPT, THEN LOADING, CLEANING, AND VISUALIZING DATA IN THE POWER BI DESKTOP

## DESCRIPTION
Here we will see how interactive and dynamic the Power BI application is by importing, cleaning, and visualizing data all by using Python and its respective libraries. 

### Overview of the dataset
The CarMax dataset is a CSV file, with at least one (1) million rows. The dataset is a web scrape of the CarMax website and details the daily inventory of cars between September 27, 2015, and June 14, 2017.

## WHAT TO EXPECT...
1. First, create a Python environment using Anaconda Navigator and install all the necessary Python libraries.
2. Update the Python's Environment directory to work within Power BI Desktop then import and load the data from the Python script using Python commands.  
3. Cleaning and Transforming the data in Power BI Desktop using the *Power QUery Editor* tool. (Implementation done in two parts for clarity)
4. Using Python code in Power BI Desktop to generate the following visualizations:
    - One Dimensional (1D) Bar chart
    - Line chart
    - Scatter plot
    - Two Dimensional (2D) Bar chart

## IMPLEMENTATION OF THE STEPS 

### <ins> **STEP ONE: SETTING UP THE PYTHON ENVIRONMENT IN ANACONDA**</ins>

Here we will set up the Python Environment within Anaconda. Anaconda is very quick and efficient in creating and managing environments. The environment created will be called `power-bi`. We will then import the necessary libraries that will be used. For this project, we will stick with `pandas`, `matplotlib`, and `seaborn`. 

**Visual Implementation:**
![Setting-up-env](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/setting-up-python%20environment.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

    pip install pandas
    pip install -U matplotlib
    pip install seaborn

### <ins> STEP TWO: IMPORTING THE ENVIRONMENT AND DATASET INTO POWER BI </ins>

Now that we have a specialized Python Environment created, it is required to set up the environment's directory within Power BI Desktop. This will use the designated environment and its libraries imported. We will then Get data using the Python Scripting feature by importing the Carmax CSV file using `Pandas` to read the CSV file. 

**Visual Implementation:**
![setting-up-python-with-bi](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/getting-data-with%20python-in-Power%20BI.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

      # import all packages 
      import pandas as pd
      import matplotlib.pyplot as plt
      import seaborn as sb

      # Reading into the CSV file
      data = "D:\Python-intergrated-with-BI\carmaxdata.csv"
      carmax_data = pd.read_csv(data)
    

### <ins> **STEP THREE: CLEANING AND TRANSFORMING**</ins>
In this step, we will get our hands dirty to clean up the dataset. *Power BI Query Editor* will clean and transform the dataset. The Data Wrangling/Cleaning step was broken into two parts for simplicity and clarity. 

##### Part 1
- first, we will select the columns wanted for the analysis by selecting `Choose Columns`
- second, we will view the `column quality` for missing, error, and null values.
- thirdly, we will select all columns and drop the null and empty values in each


![cleaning-py-bi-1](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/py-bi-cleaning-1.gif)

##### Part 2
- Here, we notice the region column has state and city together, we want to maintain the region column but split the city and state. Therefore we duplicate the region column and then split it by delimiter
- then, once the columns are split we need to rename them `state` and `city` respectively
- the final step for the cleaning and transforming step is to check and drop null and empty values to maintain a consistent size of the dataset


![cleaning-py-bi-2](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/py-bi-cleaning-2.gif)

**Cleaning and Transforming Applied Steps:**

![PowerBI-cleaning-steps](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/filtered-steps-cleaning.png)


### <ins> **STEP FOUR: PLOTTING PYTHON VISUALIZATIONS IN POWER BI DESKTOP**</ins>
Here in this step, we will plot visualizations using Python with the assistance of two most popular plotting libraries such as `Matplotlib` and `Seaborn`. All visualizations will be plotted in Power BI Desktop using the *PY-Visual* visualization. The visualizations that will be plotted are as follows:

#### Visualization 1- One-Dimensional (1D) Bar Chart
Here we will use one one variable to plot the Top 30 Cities with CarMax Dealerships. We will use the `city` variable. Then we will create a new variable to give us the counts of the `city`.

**Visual Implementation:**
![1d-barchart](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/viz-page-1.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

     """ FIRST PAGE IN REPORT: Code for visualization Top Cities of CarMax Distribution.
         Plots a Barchart!""" 

    sb.set(style="whitegrid")

    # Setting indices for the variable 'region' counts
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
       
    # Callling the plot method to display the visualization
    plt.show()

#### Visualization 2- Scatter plot
Here a scatterplot from the Seaborn library will be used. But we will add a condition the price range of cars is vast so we will add a threshold of 49,000. How did we derive this figure we found the average prices of cars. The objective is to see which is the most expensive `make` of cars with the highest `price` over the years. 
**Visual Implementation:**
![scatterplot](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/viz-page-2.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

     """ SECOND PAGE IN REPORT: Code for Most Expensive Car Prices over the Years. 
        Plots a Scatterplot!""" 

    # Finding the prices greater or equal to 48999
    #Remember we do not use Magic Numbers the logic is applied to take half of the max price and use the data from there!
    top_car_makes_overall = dataset[dataset["price"] >= 48999]
  
    # filtering to apply it to all the features we need in relation to price creating a new data frame 
    dataset_filtered = top_car_makes_overall[['price', 'year', 'model', 'make' ]]
    
    sb.scatterplot(data=dataset_filtered, x="year", y="price", hue="make", palette="deep")
    plt.title(' Comparing Most Expensive Car Make prices over the years)

    plt.show()

#### Visualization 3- Line Chart
Here a Line plot will be used from the Seaborn Library. In this visualization, we will plot the prices of cars over the years and see how the prices have changed significantly over time. 

**Visual Implementation:**
![linechart](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/viz-page-3.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

     """ THIRD PAGE IN REPORT: Code for Revenue of Cars over the Years. 
    Plots a Line Chart""" 

    # Using a seaborn line plot
    sb.lineplot(data=dataset, x="year", y="price", orient="x", 
            size=30)

    plt.title('Revenue of Cars over the years')
    plt.show()

#### Visualization 4- Two-Dimensional (2D) Barplot 
For our last visualization we will plot a bar chart but with two Dimensions. What's the difference, here we use two different vairables and compare them to each other. For this visualization we will look at the average of the different `make` of car `prices`. Finally, the bar chart will also be color-coded to distinguish each `make`. 
**Visual Implementation:**
![barchart-2d](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/viz-page-4.gif)
**Code used:** ([*Source-Code-here*](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/carmax_analysis_code.py))

    """ FOURTH PAGE IN REPORT: Code for Average Price Make 
    Plots a bar chart""" 

    fig, ax = plt.subplots(figsize=(16,11))
    g = sb.barplot(x='make', y='price', data=dataset, ci=None, ax=ax)
    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    plt.title("Average Price of Car Make")
    g.plot()
    plt.show()
