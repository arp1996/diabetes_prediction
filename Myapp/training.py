from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

DATA_DIR = Path(__file__).resolve().parent

df = pd.read_csv(DATA_DIR / "heart.csv")

print(df.head())

print(df.info())

print(df.shape)

print(df.describe())

print(df.duplicated().sum())

#Analysis
print(df.isna().sum())

print(df.nunique().sort_values())

sns.countplot(x='Age',data=df)

"""Feature Selection => Manual"""
x = df.drop(['Age','HeartDisease'], axis=1)
##data = data.dropna()
print(type(x))

y = df['HeartDisease']
print(type(y))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1234)

from sklearn.svm import SVC
#from sklearn.ensemble import RandomForestClassifier

svcclassifier = SVC()
svcclassifier.fit(x_train, y_train)

y_pred = svcclassifier.predict(x_test)
print(y_pred)


print("=" * 40)
print("==========")
print("Classification Report : ",(classification_report(y_test, y_pred)))
print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
# ACC = (accuracy_score(y_test, y_pred) * 100)
# repo = (classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("==================")
print("Confusion Matrix :\n",conf_matrix)

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

from joblib import dump
dump(svcclassifier, DATA_DIR / "model.joblib")
print("Model saved as model.joblib")
