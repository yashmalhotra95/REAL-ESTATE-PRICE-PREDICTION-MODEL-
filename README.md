# REAL-ESTATE-PRICE-PREDICTION-MODEL-
The model utilizes advanced regression techniques, such as Linear Regression, Feature Engineering, Random Forest and Gradient Boosting, to establish the relationship between independent variables & features. By leveraging predictive analytics, the model contributes to greater transparency and efficiency in the property market. 
### Problem Specification and Scope

<br>__Deliverable:__ Trained model file
<br>__Machine learning task:__ Regression
<br>__Target variable:__ Transaction Price
<br>__Win condition:__ Avg. prediction error  __*< $70,000*__ , using Mean Absolute Error (MAE)
<br>__Timeline:__ 1 months
### Stages
Stage 1: Exploratory Data Analysis (EDA)
<br>Stage 2: Data Cleaning
<br>Stage 3: Feature Engineering
<br>Stage 4: Modeling and Evaluation

### Features/Columns Explanation:
#### Target variable:
**'tx_price'** - Transaction price in USD

#### Property Public records:
**'tx_year'** - Year the transaction took place
<br>**'property_tax'** - Monthly property tax
<br>**'insurance'** - Cost of monthly home owner's insurance

#### Property characteristics:
**'beds'** - Number of bedrooms
<br>**'baths'** - Number of bathrooms
<br>**'sqft'** - Total floor area in squared feet
<br>**'lot_size'** - Total outside area in squared feet
<br>**'year_built'** - Year property was built
<br>**'basement'** - Does the property have a basement?
#### Location convenience scores
**'restaurants'** - Number of restaurants within 1 mile
<br>**'groceries'** - Number of grocery stores within 1 mile
<br>**'nightlife'** - Number of nightlife venues within 1 mile
<br>**'cafes'** - Number of cafes within 1 mile
<br>**'shopping'** - Number of stores within 1 mile
<br>**'arts_entertainment'** - Number of arts and entertainment venues within 1 mile
<br>**'beauty_spas'** - Number of beauty and spa locations within 1 mile
<br>**'active_life'** - Number of gyms, yoga studios, and sports venues within 1 mile

#### Neighborhood demographics
**'median_age'** - Median age of the neighborhood
<br>**'married'** - Percent of neighborhood who are married
<br>**'college_grad'** - Percent of neighborhood who graduated college

#### Schools
**'num_schools'** - Number of public schools within district
<br>**'median_school'** - Median score of the public schools within district, on the range 1 - 10

## Summary
From section 4.2, the gradient boosting regressor model could predict the transaction price with an mean absolute error of $45k. After trying out training with different combination of features, the model predicts most accurately with only 7 features: sqft, lot size, property tax , insurance, beds, baths and tx year.
