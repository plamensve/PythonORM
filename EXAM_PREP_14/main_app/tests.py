import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Генериране на синтетични данни
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Разделяне на данните на обучителен и тестов набор
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Създаване и обучение на модел на линейна регресия
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказания върху тестовия набор
y_pred = model.predict(X_test)

# Оценка на модела
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Пример за предсказание
new_data = np.array([[1.5]])
prediction = model.predict(new_data)
print(f"Prediction for {new_data[0][0]}: {prediction[0][0]}")
