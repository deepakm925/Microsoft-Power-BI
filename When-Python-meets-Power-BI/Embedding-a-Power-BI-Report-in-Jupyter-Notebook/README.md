<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/banner-3.png"/>


# EMBEDDING A POWER BI REPORT IN JUPYPTER NOTEBOOK, USING PYTHON. 

## DESCRIPTION
In this Project, we will continue to experiment with the dynamic data presentation capabilities of Python by embedding a Power BI report in a **Jupyter Notebook**. 

### Overview of the dataset
The CarMax dataset is a CSV file, with at least one (1) million rows. The dataset is a web scrape of the CarMax website and details the daily inventory of cars between September 27, 2015, and June 14, 2017.

## WHAT TO EXPECT...
1. First we will install the necessary Python library which is  `powerbiclient`. We will then open Jupyter-Notebook
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
1. Method 1: *Install Jupyter Notebook from the Home screen of the Navigator*
2. Method 2: *Install and open using the Anaconda Prompt or Shell* 

I will be *using Method 2* for this project. 

**Visual Implementation:**
![opening-jupyter](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Embedding-a-Power-BI-Report-in-Jupyter-Notebook/resources/opening-jupyter.gif)

Code Used:

     # IF YOU NEED TO INSTALL JUPYTER-NOTEBOOK RUN THIS COMMAND FIRST IN ANACONDA COMMAND PROMPT
     conda install -c anaconda jupyter

     # IF YOU HAVE JUPYTER NOTEBOOK ALREADY INSTALLED JUST USE THE FOLLOWING COMMAND TO OPEN IT
     jupyter-notebook

  **NOTE**: In newer versions of Anaconda Notebook the Jupyter-Notebook can be installed from the home screen from the Anaconda Naviagtor!

### <ins> STEP THREE: IMPORTING THE LIBRARY POWERBICLIENT AND AUTHENTICATING POWER BI ON LINE SERVICE </ins>
Here we will first import the necessary library `powerbiclient` along with the methods we will be using which are `Report`, `models`. 
Then we will call a `authentication` class containing the method `DeviceLoginAuthentication`. What this does is make Python request authentication to access the Power BI Online service workspaces. 
To do this optimally:
- Open Power BI online and log in to Power BI online with the email and password. Keep the tab open. 
- Run the code cell with the Authentication step in the Notebook. A security code will then be provided in the Notebook that must be inputted into the Microsoft security page provided in order to complete the security procedure.
- Once the security code is entered correctly. Microsoft itself will notify you that the device has been authenticated and that the page can be closed. This confirms that the Power BI online service can now be accessed successfully.

(NOTE: If you refresh the kernel of the Notebook this will need to be redone. Everytime this is done a new code will be provided for authentication for security purposes by Micrsoft)

  **Visual Implementation:**
  ![authenticating-bi](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Embedding-a-Power-BI-Report-in-Jupyter-Notebook/resources/authentication-bi-python.gif)

  Code Used:

    """FIRST CODE CELL""" 
    # import powerbiclient library and necessary BI components
    from powerbiclient import Report, models

    # Import the DeviceCodeLoginAuthentication class to authenticate against Power BI
    from powerbiclient.authentication import DeviceCodeLoginAuthentication

     """ SECOND CODE CELL""" 
     # Initiate device authentication
     device_auth = DeviceCodeLoginAuthentication()

### <ins> STEP FOUR: IDENTIFYING THE POWER BI REPORT BY REPORT ID AND WORKSPACE ID </ins>
In this step, we will choose a report on the online Power BI platform that we wish to use to embed into our JUpyter-Notebook file. To do this we need to:
1. First identify the report we want to open in a new tab in the browser.
2. WE look at the URL tab and notice `groups` and then `reports` we notice both titles have a series of characters in between their `/` Here is a visual example from my personal workspace:
![ids](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Embedding-a-Power-BI-Report-in-Jupyter-Notebook/resources/report_id-workspace_id-report.png)
3. We then copy the underlined  pieces which are the `groups` and `reports` along with their characters. (In my example above the text underlined in red is the workspace ID and blue is the report ID)
4. We then create two new variables in our Python code called `workspace_id` and `report_id` and copy and paste the characters respectively to their variables.

(FOR CLARIFICATION: `groups` is the workspace directory, however, in my example, I used `workspace_id`. )

**Visual Implementation:**
![report_id-work_id](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Embedding-a-Power-BI-Report-in-Jupyter-Notebook/resources/report-id.gif)

### <ins> STEP FIVE: SETTING UP THE REPORT  </ins>
In this final step, we can go ahead and load the Power BI report into our notebook. 
- First, we will call the `REPORT` method from the `powerbiclient` library. We then assign this to a variable called `load_bi_report`
- In the `REPORT` method we have to pass the `workspace_id`, `report_id`, and `device_auth`. Here, locate the report in the designated workspace and give Jupyter-Notebook access to open it.
- Finally, we can run the variable `load_bi_report` with our method and its parameters. 


 
