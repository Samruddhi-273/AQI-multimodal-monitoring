import joblib
import pandas as pd
import numpy as np

# Load trained Random Forest model
model = joblib.load("models/random_forest_model.pkl")


def predict_with_uncertainty(input_df):
    """
    Predict AQI with uncertainty estimation
    using predictions from all trees.
    """

    # Prediction from every decision tree
    tree_predictions = np.array([
        tree.predict(input_df)[0]
        for tree in model.estimators_
    ])

    mean_prediction = np.mean(tree_predictions)

    std_prediction = np.std(tree_predictions)

    lower = mean_prediction - 1.96 * std_prediction
    upper = mean_prediction + 1.96 * std_prediction

    return {
        "prediction": mean_prediction,
        "std": std_prediction,
        "lower": lower,
        "upper": upper
    }