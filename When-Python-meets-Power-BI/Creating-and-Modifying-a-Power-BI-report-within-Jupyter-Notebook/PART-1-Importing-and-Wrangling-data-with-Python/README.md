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

      
