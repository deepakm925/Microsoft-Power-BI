<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/banner-3.png"/>

  # CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK
  # PART 2 :  USING PYTHON TO CREATE A POWER BI REPORT

## DESCRIPTION
This is **PART 2** of the Project **CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK**. In PART-1 we used Python to Import and Wrangle the dataset. 
In this step, we will create a Power BI report using the `powerbiclient` library

## WHAT TO EXPECT...
1. First we will authenticate Power BI credentials in the JUpyter Notebook so that we can create a link to the Power BI online Service
2. We will use the `powerbiclient` library to create a new instance of a report from the cleaned dataset from PART 1

## IMPLEMENTATION OF THE STEPS 
Here we will display the implementation phase in Steps with the use of GIFs and the help of code snippets. Let's begin!

### <ins> STEP ONE: AUTHENTICATING POWER BI CREDENTIALS WITH JUPYTER-NOTEBOOK</ins>
In this step, we will use the `Authenticate` method from the `powerbiclient` library to authenticate Jupyter Notebook to have access to the Power BI online workspace. Microsoft will provide a URL link and a security code, open the link and add the security code plus the Power BI online account details.

**Visual Implementation**
![authenticating-powerbi](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-2-Using-Python-to-Create-a-Power-BI-Report/resources/powerbi-authentication.gif)

Code Used:

      """ In this code cell we will use the Authenticate method from powerbiclient """
      # Import the DeviceCodeLoginAuthentication class to authenticate against Power BI
      from powerbiclient.authentication import DeviceCodeLoginAuthentication

      # Initiate device authentication
      device_auth = DeviceCodeLoginAuthentication()

### <ins> STEP TWO: CREATE THE REPORT /ins>
In this step will use another method from the `powerbiclient` library called `QuickVisualize`. Within this method, we will pass our cleaned dataset variable called `movie_df_final` created from STEP ONE. When run, this creates a new instance of a report with default visualizations created from `QUICK VISUALIZE`.
