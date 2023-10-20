<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/banner-3.png"/>

  # CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK
  # PART 1 :  IMPORTING AND WRANGLING DATA WITH PYTHON 

## DESCRIPTION
This is **PART 1** of the Project **CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK**. In this first part, we will import and wrangle the data using Python. 


## WHAT TO EXPECT...
1. First, import the necessary libraries and load the dataset
2. Then begin our data cleaning step by analyzing the missing/null values and dropping them
3. Dropping unwanted columns that are not adequate for the analysis
4. Editing columns such as transforming, splitting, and changing data type
5. Load a clean version of the dataset


## IMPLEMENTATION OF THE STEPS 
Here we will display the implementation phase in Steps with the use of GIFs and the help of code snippets. Let's begin!

### <ins> STEP ONE: INSTALLING LIBRARIES AND LOADING THE DATASET</ins>
In this first step, we will open Jupyter-Notebook and install the necessary libraries. The libaries that will be used are:
- `pandas`
- `powerbiclient`
  
Then, we will use the `pandas` method `pd.read_csv()` to read into and load the TMDB movies dataset file `movie_data`.

**Visual Implementation:**
![import-and-load](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/importing-and-loading-dataset.gif)

Code Used

     """ First Code Cell """ 
     # import necessary libraries
     from powerbiclient import QuickVisualize, get_dataset_config
     import pandas as pd
     
     """ Second Code cell """ 
     # import dataset using Pandas
     movie_data = pd.read_csv('tmdb-movies.csv')
     # display
     movie_data.head()

### <ins> STEP TWO: IDENTIFYING AND DROPPING MISSING VALUES </ins>
Here in this step, we will identify the missing values and null values in the dataset. We can use this by using a `pandas` method called `isnull().sum()`. Then, we can remove the missing/null values using the `drop.na()` method which is also from the `pandas` library. 

**Visual Implementation:**
![identifying-missing-valyes](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/identifying-dropping-missing-values.gif)

Code Used

     """ This code cell checks missing values""" 
     # Identifying missing values
     movie_data.isnull().sum()

     """ This code cell removes the missing values """
     # Apply dropna from Pandas to drop the values from existing columns
     movie_data_cleaner_1 = movie_data.dropna()

     # Checking if process worked
     movie_data_cleaner_1.isnull().sum()

### <ins> STEP THREE: DROPPING UNWANTED COLUMNS </ins>
Here, in this step we will remove any unnecessary columns that will not be used for our analysis. To do this the `pandas` library has a method `df.drop()` that drops columns. 

**Visual Implementation:**
![unwanted-columns](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/deleted-unwanted-columns.gif)

Code Used

     # Dropping unwanted columns
     movie_data_cleaner_2 = movie_data_cleaner_1.drop(['homepage', 'tagline', 'keywords', 'overview'], axis=1)

### <ins> STEP FOUR:  EDITING COLUMNS BY SPLITTING AND CHANGING DATA TYPES</ins>
Here, in this step we will do two things:
1. If we didnt notice earlier when viewing the data, we should look again now, if you notice the `cast`, `genres` and `production_companies` have many data values in one row like so:

   ![categorical](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/sample-categorical.png)
   
     To fix this we use the `|` delimator method along with `lambda` which splits worded data. This will split and take the first word in the series. WE will aplly it on the three worded columns mentioned above. 

2. Secondly, we notice we have a `release_year` column. However, it is in `int64`. We want the data to remain periodically, so we will use the `pandas` method `PeriodIndex` which will always keep the years in periodical format.

**Visual Implementation:**
![edit-columns](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/editing-columns.gif)

Code Used

     """ IN this cell we use lambda with the delimator method to split the worded columns 
     # Cleaning cast
     movie_data_cleaner_2.loc[:,'cast'] = movie_data_cleaner_2.loc[:,'cast'].apply(lambda x: x.split('|')[0])

     # Cleaning genres
     movie_data_cleaner_2.loc[:,'genres'] = movie_data_cleaner_2.loc[:,'genres'].apply(lambda x: x.split('|')[0])

     # Cleaning production companies
     movie_data_cleaner_2.loc[:,'production_companies'] = movie_data_cleaner_2.loc[:,'production_companies'].apply(lambda x: x.split('|')[0])

     """ In this code cell pandas PeriodIndex will be applied to the relase_year column to maintain the year format indexing 
     # Using PeriodIndex
     movie_data_cleaner_2['release_year'] = pd.PeriodIndex(movie_data_cleaner_2['release_year'], freq='A')


### <ins> STEP FIVE:  FINAL CLEANED DATASET</ins>
Here we will run tests and output our cleaned dataset and assign it a new variable. 

**Visual Implementation:**
![final-cleaned-dataset](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-1-Importing-and-Wrangling-data-with-Python/resources/final-cleaned-dataset.gif)

Code Used

      # Our cleaned version of the dataset 
      
      movie_df_final = movie_data_cleaner_2
      movie_df_final.head()
     
