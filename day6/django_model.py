import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Fetch data from the revenues API
revenues_url = "https://uccbwaise.org/api/v1/revenues-list"
revenues_response = requests.get(revenues_url)

if revenues_response.status_code == 200:
    revenue_data = revenues_response.json()
else:
    print("Error retrieving data from the revenues API")

# Fetch data from the expenditures API
expenditures_url = "https://uccbwaise.org/api/v1/expenditures-list"
expenditures_response = requests.get(expenditures_url)

if expenditures_response.status_code == 200:
    expenditure_data = expenditures_response.json()
else:
    print("Error retrieving data from the expenditures API")

# Convert the data to Pandas DataFrames
revenue_df = pd.DataFrame(revenue_data)
expenditure_df = pd.DataFrame(expenditure_data)

# Select relevant features and target variable for the revenue data
revenue_features = revenue_df[['Date','Service', 'Member_Id', 'Building_Amount', 'Love_Offering_Amount', 'Thanks_Giving_Amount', 'Bills_Amount', 'Seed_Amount', 'Envag_Or_Missions_Amount', 'Tithe_Amount', 'General_Offering_Amount']]
revenue_target = revenue_df['Amount']

# Select relevant features for the expenditure data
expenditure_features = expenditure_df[['Date', 'Payment_Made_To', 'Amount']]

# Merge the revenue and expenditure data based on common columns, e.g., 'Date' or 'Member_Id'
merged_data = pd.merge(revenue_features, expenditure_features, on='Date', how='inner')

# Split the merged data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(merged_data, revenue_target, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)
