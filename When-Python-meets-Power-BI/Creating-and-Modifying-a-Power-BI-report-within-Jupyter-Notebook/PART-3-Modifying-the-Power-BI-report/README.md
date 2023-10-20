<p align="center">
  <img src="https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/resources/banner-3.png"/>

# CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK
# PART 3:  MODIFYING THE POWER BI REPORT USING BI TOOLS

## DESCRIPTION
This is **PART 3** of the Project **CREATING AND MODIFYING A POWER BI REPORT USING PYTHON AND POWER BI TOOLS, IN JUPYTER-NOTEBOOK**. In PART-2 we created the Power BI report instance. 
In this part of the project, we will add personal modifications to the Power BI report such as edit and changing the characteristics of the types and characteristics of the visualizations to our analysis objectives. 

## WHAT TO EXPECT...
1. Duplicate the report instance to create a new variable that will be modified
2. Modifying and personalizing visualizations 
3. Modifying and personalizing visualizations Continued
4. testing the modified report 

## IMPLEMENTATION OF THE STEPS 
Here we will display the implementation phase in Steps with the use of GIFs and the help of code snippets. Let's begin!

### <ins> STEP ONE: DUPLICATING THE POWER BI REPORT INSTANCE TO CREATE A NEW VARIABLE FOR MODIFICATION </ins>
In PART 2 we already created a power bi report and assigned it to the variable `create_bi_report` . Now we want to keep the default report to show we created one but we want to create a new one to modify. 
Here we will create a new report instance and assign it to the variable `modified_report`. 

**Visual Implementation**
![duplicating-report](https://github.com/deepakm925/Power-BI/blob/main/When-Python-meets-Power-BI/Creating-and-Modifying-a-Power-BI-report-within-Jupyter-Notebook/PART-3-Modifying-the-Power-BI-report/resources/duplicating-report.gif)

Code Used

      # assigning the original report to a new one to create a duplicate
      modified_report = create_bi_report

      # Display the report
      modified_report

### <ins> STEP TWO: MODIFYING AND EDITING THE POWER BI REPORT WITH BI TOOLS  </ins>
Here we notice the firt Power BI report instance we created already produced default visualizations. However, we have our own agenda for the analysis and we wish to edit modify and change the report to personalize our analysis. This step and the next step after this STEP 3 will deal with modifications and editing the Power BI report using Power BI tools and BI visualizations!
The visualizations that will be edited and modified here are:
- First visualization we will change it and use a *Slicer-list* using the `genres`. WE are making the `genres` the main list and if any visualization with the `genres` will automatically sync the slicer settings
- Second visualization we will use a *Clustered Bar Chart* to plot
- Third visualization, we will use a Tree Map

**Visual Implementation**

