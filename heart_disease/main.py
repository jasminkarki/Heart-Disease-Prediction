import os
import pickle
import sys

# import mlflow
import numpy as np
import pandas as pd
# from mlflow import log_artifacts, log_metric, log_param
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

from baselinemodel import base_model
from heart_disease.config import config  # insert . to run from outside
from preprocessing import train_test_split_normalize, load_dataset

# Load dataset from its path
dataset = load_dataset(config.PROCESSED_DATAPATH, config.DATASET_NAME)
# Train test split the loaded dataset and normalize it
X_train, X_test, y_train, y_test = train_test_split_normalize(dataset)
