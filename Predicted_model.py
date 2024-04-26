from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib  # Import joblib


df = pd.read_csv("PredictData.csv")
x = df[['outdoor_pm2_5', 'temp']]
y = df['pm2_5']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)
model = LinearRegression()
model.fit(x_train_scaled, y_train)
score = model.score(x_test_scaled, y_test)
print('R-Squared:', '{:.2f}'.format(score))

# joblib.dump(model, 'ezdust/dust/views/indoorair_model.joblib')
joblib.dump(scaler, 'ezdust/dust/static/dust/modle/scaler.joblib')