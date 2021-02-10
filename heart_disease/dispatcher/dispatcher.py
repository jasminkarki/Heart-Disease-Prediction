from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier



MODELS = {
    "knn": KNeighborsClassifier,
    "naive_bayes": MultinomialNB,
    "xgboost": XGBClassifier,
    "logistic": LogisticRegression,
    "svm_svc": SVC,
}