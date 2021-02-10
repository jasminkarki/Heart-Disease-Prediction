import os
import pickle

from sklearn import metrics
from sklearn.metrics import f1_score, make_scorer
from sklearn.svm import SVC

from .config import config


def base_model(X_train, X_test, y_train, y_test, classifier):

    svc = classifier()
    svc.fit(X_train, y_train)
    pickle.dump(
        svc,
        open(
            os.path.join(
                config.BASE_DIR, "heart_disease", "checkpoints", "model_svc.pkl"
            ),
            "wb",
        ),
    )
    model = pickle.load(
        open(
            os.path.join(
                config.BASE_DIR, "heart_disease", "checkpoints", "model_svc.pkl"
            ),
            "rb",
        )
    )
    predictions = model.predict(X_test)
    f1_sc = metrics.f1_score(y_test, predictions, average="macro")
    accuracy_sc = metrics.accuracy_score(y_test, predictions)
    return f1_sc, accuracy_sc


def inference(arr):
    transf = pickle.load(
        open(
            os.path.join(
                config.BASE_DIR, "heart_disease", "checkpoints", "transf.pkl"
            ),
            "rb",
        )
    )
    transformed = transf.transform([arr])
    model = pickle.load(
        open(
            os.path.join(
                config.BASE_DIR, "heart_disease", "checkpoints", "model_svc.pkl"
            ),
            "rb",
        )
    )
    label = model.predict(transformed)
    return 'No' if label==0 else 'Yes'
    # label_inv_encoder = pickle.load(
    #     open(
    #         os.path.join(
    #             config.BASE_DIR, "heart_disease", "checkpoints", "label_encoder.pkl"
    #         ),
    #         "rb",
    #     )
    # )
    # output = label_inv_encoder.inverse_transform(label)
    # return label
