import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

df = pd.read_csv('PredictData.csv')
df.head()

df.describe()

null_counts = df.isnull().sum()
print(null_counts)

df['time'] = pd.to_datetime(df['time'])

bins = [0, 6, 12, 18, 24]
labels = ['Night', 'Morning', 'Noon', 'Evening']

df['time_category'] = pd.cut(df['time'].dt.hour, bins=bins, labels=labels, include_lowest=True)

Q1 = df['pm2_5'].quantile(0.25)
Q3 = df['pm2_5'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

cleaned_data = df[(df['pm2_5'] >= lower_bound) & (df['pm2_5'] <= upper_bound)]
cleaned_data

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
cleaned_data['place_type'] = le.fit_transform(cleaned_data['place_type'])
cleaned_data['time_category'] = le.fit_transform(cleaned_data['time_category'])

cleaned_data

correlation_matrix = cleaned_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

X = cleaned_data[['time_category', 'outdoor_temp', 'outdoor_humidity', 'outdoor_pm2_5', 'temp']]
y = cleaned_data['pm2_5']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Fitting Simple Linear Regression to the Training set
model = LinearRegression()
model.fit(x_train_scaled, y_train)

score = model.score(x_test_scaled, y_test)
print('R-Squared:', '{:.2f}'.format(score))

print(model.coef_)
print(model.intercept_)

print("Feature: ", x_train.columns.tolist())
print("Coefficient: ", model.coef_)
print("Intercept: ", model.intercept_)

y_pred = model.predict(x_test_scaled)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print('RMSE(Root_Mean_Squared_Error):', '{:.2f}'.format(rmse))

ic = '{:.2f}'.format(model.intercept_)
time_category = '{:.4f}'.format(model.coef_[0])
outdoor_temp = '{:.4f}'.format(model.coef_[1])
outdoor_humidity = '{:.4f}'.format(model.coef_[2])
outdoor_pm2_5 = '{:.4f}'.format(model.coef_[3])
temp = '{:.4f}'.format(model.coef_[4])
print(f'The prediction equation is indoor_pm2_5 = {ic} + ({time_category})x1 + ({outdoor_temp})x2 + ({outdoor_humidity})x3 + ({outdoor_pm2_5})x4 + ({temp})x5')

joblib.dump(model, 'ezdust/dust/static/dust/model/indoorair_model.joblib')
joblib.dump(scaler, 'ezdust/dust/static/dust/model/scaler.joblib')