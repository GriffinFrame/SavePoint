

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

# data straight from my ass. CHANGE
# Assuming columns are Voltage, Current, and Battery Charge
data = {
    'Voltage': [29.0, 28.8, 28.5, 28.2, 27.9, 27.5, 27.2, 26.9],
    'Current': [10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5],
    'Battery Charge': [95, 90, 85, 80, 75, 70, 65, 60]  # in %
}


df = pd.DataFrame(data)
X = df[['Voltage', 'Current']].values
y = df['Battery Charge'].values

#Runtime (hours) = Remaining Capacity (Ah) / Current (A)
battery_capacity = 50  # in Ah
df['Remaining Capacity (Ah)'] = (df['Battery Charge'] / 100) * battery_capacity
df['Runtime (hours)'] = df['Remaining Capacity (Ah)'] / df['Current']
y_runtime = df['Runtime (hours)'].values



# Splitind data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_runtime, test_size=0.2, random_state=42)




# Normalizing
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)





# Training model to predict battery runtime
svr_charge = SVR(kernel='rbf')
svr_charge.fit(X_train_scaled, y_train)

# predicting battery life
y_pred_runtime = svr_charge.predict(X_test_scaled)
  
# Evaluating model 
mse_runtime = mean_squared_error(y_test, y_pred_runtime)
print(f"Mean Squared Error (Runtime Prediction): {mse_runtime}")

# Plot predictions 
plt.scatter(y_test, y_pred_runtime)
plt.plot([0, max(y_test)], [0, max(y_test)], color='red', linestyle='--')  # Ideal  
plt.xlabel('Actual Battery Runtime (hours)')
plt.ylabel('Predicted Battery Runtime (hours)')
plt.title('Battery Runtime Prediction')
plt.show()




# doing the same shit but for battery charge 
svr_charge_amount = SVR(kernel='rbf')
svr_charge_amount.fit(X_train_scaled, y_train)

# Predicting battery charge 
y_pred_charge = svr_charge_amount.predict(X_test_scaled)

# Evaluating model
mse_charge = mean_squared_error(y_test, y_pred_charge)
print(f"Mean Squared Error (Charge Prediction): {mse_charge}")

# Plot predictions  
plt.scatter(y_test, y_pred_charge)
plt.plot([0, 100], [0, 100], color='red', linestyle='--')  # Ideal  
plt.xlabel('Actual Battery Charge (%)')
plt.ylabel('Predicted Battery Charge (%)')
plt.title('Battery Charge Prediction')
plt.show()
