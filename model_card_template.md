# GIT link
    https://github.com/kdoerh1/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Karrissa. The data completed was November 6, 2024. 
The model was done as a Udacity Project for Machine Learning DevOps. 
## Intended Use
The intended use for this model was to take information from the census data to see who is making above or below $50,000 anually. 
It takes the following collumns as inputs: workclass, education, marital status, occupation, relationship, race, sex,
and native country. 

## Training Data
The data from the census is then trained. I used the RandomForestRegressor to train my model. 
## Evaluation Data
The data was provided by Udacity. And Udacity took the data from the US Census Bureau Data. 
## Metrics
The metrics that were calculated were precision, recall and F1.
My models metrics are:
    Precision: 0.7976
    Recall: 0.5920
    F1: 0.6796

## Ethical Considerations
This dataset was specific for this project for Udacity.

## Caveats and Recommendations
I recommend to find your own data set and make sure the model will work for that dataset. 
