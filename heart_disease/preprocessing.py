import os
import numpy as np
import pandas as pd

import re
import pickle

import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from config import config


def load_dataset(dataset_path, dataset_name):

    df = pd.read_csv(
        os.path.join(dataset_path, dataset_name),
        header=None,
    )
    df.drop(columns=["target"], inplace=True)
    return df

def train_test_split_normalize(df):

    X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['target']), df['target'], test_size = 0.2, random_state = 0)
    norm = MinMaxScaler().fit(X_train)
    X_train = norm.transform(X_train)
    pickle.dump(
        norm,
        open(
            os.path.join(
                config.BASE_DIR, "heart_disease", "checkpoints", "norm.pkl"
            ),
            "wb",
        ),
    )
    X_test = norm.transform(X_test)

    return X_train, X_test, y_train, y_test

