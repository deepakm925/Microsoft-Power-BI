<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/heading-python.png"/>

  # INTEGRATING A PYTHON SCRIPT TO LOAD, CLEAN, VISUALIZE DATA IN POWER BI DESKTOP

  ## DESCRIPTION
Here we will see how interactive and dynamic the Power BI application is by importing, cleaning, and visualizing data all by using Python and its respective libraries. 

## WHAT TO EXPECT...
1. First, create a Python environment using Anaconda Navigator and install all the necessary Python libraries.
2. Update the Python's Environment directory to work within Power BI Desktop then import and load the data from the Python script using Python commands.  


## VISUAL IMPLEMENTATION OF THE STEPS WITH GIFS

### <ins> **STEP ONE**</ins>

Here we will set up the Python Environment within Anaconda. Anaconda is very quick and efficient in creating and managing environments. The environment created will be called `power-bi`. We will then import the necessary libraries that will be used. For this project we will stick with `pandas`, `matplotlib`, and `seaborn`. 
![Setting-up-env](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/setting-up-python%20environment.gif)


### <ins> **STEP TWO**</ins>

Now that we have a specialized Python Environment created, it is required to set up the environment's directory within Power BI Desktop. This will use the designated environment and its libraries imported. We will then Get data using the Python Scripting feature by importing the Carmax CSV file using `Pandas` to read the CSV file. 
![setting-up-python-with-bi](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/getting-data-with%20python-in-Power%20BI.gif)


### <ins> **STEP THREE**</ins>
In this step, we will get our hands dirty to clean up the dataset. *Power BI Query Editor* will clean and transform the dataset. The Data Wrangling/Cleaning step was broken into two parts for simplicity and clarity. 

##### Cleaning Part 1
- first, we will select the columns wanted for the analysis by selecting `Choose Columns`
- second, we will view the `column quality` for missing, error, and null values. 
![cleaning-py-bi-1](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/py-bi-cleaning-1.gif)

##### Cleaning Part 2

![cleaning-py-bi-2](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Integrating-a-Python-Script-to-create-a-report-in-BI/resources/py-bi-cleaning-2.gif)
