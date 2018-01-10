# DSI Capstone Project

## DrivenData Competition: Reboot: Box-Plots for Education 

*Author: Uyen Truong*

For my independent final Capstone Project, I worked on the dataset from the [Reboot: Box-Plot for Education Competition](https://www.drivendata.org/competitions/46/box-plots-for-education-reboot/) hosted by DrivenData.

### Problem Description

"Budgets for schools and school districts are huge, complex, and unwieldy. It's no easy task to digest where and how schools are using their resources. Education Resource Strategies is a non-profit that tackles just this task with the goal of letting districts be smarter, more strategic, and more effective in their spending.

Your task is a multi-class-multi-label classification problem with the goal of attaching canonical labels to the freeform text in budget line items. These labels let ERS understand how schools are spending money and tailor their strategy recommendations to improve outcomes for students, teachers, and administrators."

### Project goals:

- Apply fundamental machine learning classification models to predict the probability that a certain label is attached to each budget line item.
- Enter submissions the competition website.


**Content:**

In the ipynb folder, start with **Capstone_Project_Report.ipynb** - This report describes the process and results of the the technical process and codes I used to build my models and generate predictions. The report includes the following sections:

- EDA and data preprocessing of the datasets which included using NLP library and regex to clean the data,
- Baseline model pipeline'
- Process for experimenting with different types of models to improve scores which includes:
    - Model hyper-parameter tuning with Gridsearch,
    - Boosting method with XGB,
    - Model blending.
    
**Submission Results**
As of January, 2018 my lowest submission score puts me in 13th place of the competition. I'm continuing to explore other methods as well as fine tuning my current models to achieve lower submission scores.

![](/Users/uyen/Desktop/rank.png)

   

