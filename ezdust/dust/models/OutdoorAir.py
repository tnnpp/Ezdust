from django.db import models
from django.utils import timezone

class OutdoorAir(models.Model):
    time = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=200)
    pm2_5 = models.IntegerField()
    temp = models.FloatField()
    humidity = models.FloatField()

    # def predict_model(self):
    #     df = pd.read_csv("media/PredictData.csv")
    #     x = df['pm2_5']
    #     y = df['outdoor_pm2_5']
    #     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    #     scaler = StandardScaler().fit(x_train)
    #     x_train_scaled = scaler.fit_transform(x_train)
    #     x_test_scaled = scaler.transform(x_test)
    #     model = LinearRegression()
    #     model.fit(x_train_scaled, y_train)
    #     score = model.score(x_test, y_test)
    #     print('R-Squared:', '{:.2f}'.format(score))
    #     # print(df)
    #
