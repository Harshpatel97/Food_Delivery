# End to end Food-Delivery-Prediction-Time-Project
The Food Delivery Time Prediction project is a machine learning-based solution aimed at estimating the delivery time for food orders placed through various delivery platforms. This project leverages historical data, machine learning algorithms, and predictive modeling to provide accurate estimates of when customers can expect their food to arrive.

## Fearures

1. Data Collection: Data is Downloaded from kaggle https://www.kaggle.com/datasets/bhanupratapbiswas/food-delivery-time-prediction-case-study
2. Feature Engineering: We performed feature engineering to extract many useful informations, like using longitude and latitude to distance between restaurant and delivery location.
3. Model Evaluation: We used RandomForestClassifier which got 83% accuracy when fine tuned with different hyperparameters.
4. User Interface: Build Custom interface on Flask.
5. Deployed: Deployed on AWS beanstalk and Azure. 

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Harshpatel97/Food_Delivery.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create --name food python=3.9 -y
```

```bash
conda activate food
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Harsh Patel
Email: harshp4106@gmail.com
```

