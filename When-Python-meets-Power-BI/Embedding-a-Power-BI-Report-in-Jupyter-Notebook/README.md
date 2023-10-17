<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/banner-3.png"/>


# IMPORTING A POWER BI REPORT USING PYTHON, INTO A JUPYTER-NOTEBOOK

## DESCRIPTION
In this Project, we will continue to experiment with the dynamic data presentation capabilities of Python by embedding a Power BI report in a **Jupyter Notebook**. 

### Overview of the dataset
The CarMax dataset is a CSV file, with at least one (1) million rows. The dataset is a web scrape of the CarMax website and details the daily inventory of cars between September 27, 2015, and June 14, 2017.

## WHAT TO EXPECT...
1. First we will install the necessary Python library required which is  `powerbiclient`. We will then open Jupyter-Notebook
2.  We will then open Jupyter-Notebook and import the necessary library installed
3. Here we will import the authentication method from `powerbiclient` to grant access to our online PowerBI workspace
4. Here, we will then setup the workspace and report id to identify the Power BI report located in our online Power BI workspace

## IMPLEMENTATION OF THE STEPS 
Here we will display the implementation phase in Steps with the use of GIFs and the help of code snippets. Let's begin!

### <ins> STEP ONE: INSTALLING THE POWER BI CLIENT PACKAGE LIBRARY </ins>
First, we will first source the `powerbiclient` package which can be found [here](https://pypi.org/project/powerbiclient/). We then need to install it in our designated environment for *Power BI*. I already have a Power BI environment set up with Anaconda from a previous project called `python-bi-env` so I will just continue to work there. If you need a moment to install your environment I recommend to do it first. Finally as a Python Developer, I recommend setting up environments for easier management. 

**Visual Implementation:**
![powerbiclient](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Embedding-a-Power-BI-Report-in-Jupyter-Notebook/resources/installing-powerbi-client.gif)

Code Used:

     pip install powerbiclient

### <ins> STEP TWO: OPENING JUPYTER-NOTEBOOK </ins>
In this second step, we will open Jupyter-Notebook from the Anaconda Navigator. There are two ways to do this:
- Install Jupyter Notebook from the Home screen of the Navigator
- Install and open using the Anaconda Prompt or Shell 
