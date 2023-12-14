import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import statsmodels.api as sm
from statsmodels.miscmodels.ordinal_model import OrderedModel

path = "winequality-red.csv"
wine_data_set = pd.read_csv(path, sep=";")

wine_data_set.hist(bins=50, figsize=(10, 10))
plt.show()


f, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(
    wine_data_set.corr(), annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", ax=ax
)
plt.title(f"Confusion Matrix")
plt.show()

sns.scatterplot(data=wine_data_set, x="sulphates", y="alcohol", hue="quality")
plt.show()

sns.countplot(x="quality", data=wine_data_set, palette="Set1")
plt.title(f"Distribution of quality variable")
plt.show()


def new_quality_rating(rating):
    if rating == 3 or rating == 4 or rating == 5:
        return 0

    else:
        return 1


# # this rating model was removed because it is over fitting
# def new_quality_rating(rating):
#     if (rating == 3 or rating == 4):
#         return 1
#     elif (rating == 5 or rating == 6):
#         return 2
#     else:
#         return 3


wine_data_set["quality"] = wine_data_set["quality"].apply(new_quality_rating)
wine_data_set["quality"] = pd.Categorical(
    wine_data_set["quality"], categories=[0, 1], ordered=True
)
print(wine_data_set["quality"].dtype.ordered)

sns.countplot(x="quality", data=wine_data_set, palette="Set1")
plt.title(f"Distribution of new quality variable")
plt.show()


X = wine_data_set.drop("quality", axis=1)
y = wine_data_set["quality"]

# # this rating model was removed because it is over fitting
# oversample = SMOTE()
# x_resample, y_resample  = oversample.fit_resample(X, y.values.ravel())
# print("Shape of x_resample :",x_resample.shape)
# print("Shape of y_resample :",y_resample.shape)

X_main, X_custom_test, y_main, y_custom_test = train_test_split(
    X, y, test_size=5, random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X_main, y_main, test_size=0.25, random_state=42
)


standard_scaler = StandardScaler()
X_train_scaled = standard_scaler.fit_transform(X_train)
X_test_scaled = standard_scaler.transform(X_test)
X_custom_test_scaled = standard_scaler.transform(X_custom_test)


penalties = ["l1", "l2", "elasticnet"]
accuracy_list = []
for penalty in penalties:
    log_reg = LogisticRegression(
        solver="saga",
        penalty=penalty,
        l1_ratio=0.5,
        multi_class="auto",
        max_iter=10000,
        random_state=42,
    )

    log_reg.fit(X_train_scaled, y_train)

    y_pred = log_reg.predict(X_test_scaled)
    print(f"Logistic regression with {penalty}")
    print("Test set classification report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print(" ")
    y_custom_pred = log_reg.predict(X_custom_test_scaled)
    print("Custom test set classification report:")
    print(classification_report(y_custom_test, y_custom_pred, zero_division=0))
    print(
        "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
    )

distributions = ["probit", "logit"]
for distr in distributions:
    model = OrderedModel(y_train, X_train_scaled, distr=distr)
    results = model.fit(method="bfgs")
    print(results.summary())
    y_pred_eval = results.predict(X_test_scaled)
    y_pred_class_eval = np.argmax(y_pred_eval, axis=1) + np.min(y_train)
    print(f" Ordinal '{distr}' regression classification report:")
    print(classification_report(y_test, y_pred_class_eval, zero_division=0))
    print(
        "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/"
    )
