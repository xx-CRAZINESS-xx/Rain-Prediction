
# Rain Prediction

A project on predicting whether it will rain tomorrow or not in Australia by using the rainfall dataset



### Dataset
https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

## Screenshots

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Rain-Prediction/blob/main/static/image/Screenshot.png?raw=True)

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Rain-Prediction/blob/main/static/image/rainy.png)

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Rain-Prediction/blob/main/static/image/sunny.png)


## Preprocessing

- Data has 145460 rows and 23 columns out of which, except Date and Location every column had null values

- Seperated year,month and date from date column

- Created a new feature seasons from month 

- Removed outliers using IQR 

- Encoded Location based on value counts

- Used IterativeImputer to impute null values

- Dropped few features using correlation
## Model Building

- As the target variable is imbalanced, used SMOTE to oversample the minority class

- Used logistic regression as baseline model which resulted in an accuracy of 80%, roc auc of 80% 

- Used FLAML automl to find the best model and ended up selecting LightGBMClassifier as the best model 

### Results

![App Screenshot](https://github.com/xx-CRAZINESS-xx/Rain-Prediction/blob/main/static/image/result.png?raw=True)


![App Screenshot](https://github.com/xx-CRAZINESS-xx/Rain-Prediction/blob/main/static/image/roc.png?raw=True)
## Deployment

- Used flask to create an app

- Deployed the app on heroku

https://rain--prediction.herokuapp.com/
## Run Locally

Clone the project

```
  git clone https://github.com/xx-CRAZINESS-xx/Rain-Prediction.git
```

Go to the project directory

```
  cd Rain-Prediction
```

Install dependencies

```
  pip install -r requirements.txt
```

Start the server

```
  python app.py
```

