# ============================================================
# PyCaret Regression Demo
# Problem: House Price Prediction
# ============================================================

import pandas as pd

from pycaret.regression import (
    setup,
    models,
    compare_models,
    create_model,
    tune_model,
    predict_model,
    evaluate_model,
    plot_model,
    save_model,
    load_model,
    pull
)


# ------------------------------------------------------------
# 1. Create sample dataset
# ------------------------------------------------------------

data = {
    "area": [900, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2800,
             3000, 3200, 3500, 1100, 1400, 1700, 1900, 2100, 2400, 2600],
    "bedrooms": [2, 2, 2, 3, 3, 3, 4, 4, 4, 5,
                 5, 5, 5, 2, 3, 3, 3, 4, 4, 4],
    "age": [10, 8, 6, 5, 4, 7, 3, 2, 5, 1,
            2, 1, 1, 9, 6, 4, 5, 3, 2, 4],
    "distance": [12, 10, 9, 7, 6, 8, 5, 4, 6, 3,
                 3, 2, 2, 11, 8, 6, 7, 5, 4, 5],
    "price": [45, 52, 58, 72, 78, 85, 105, 120, 135, 160,
              175, 190, 210, 55, 68, 82, 92, 115, 132, 145]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nDataset shape:", df.shape)


# ------------------------------------------------------------
# 2. Start PyCaret regression setup
# ------------------------------------------------------------
# target = the column we want to predict
# session_id = fixed randomness for repeatable result

regression_setup = setup(
    data=df,
    target="price",
    session_id=42,
    train_size=0.8,
    verbose=True
)

# After setup(), PyCaret internally prepares the experiment.
# It identifies features, target, train/test split, and preprocessing pipeline.


# ------------------------------------------------------------
# 3. See available regression models
# ------------------------------------------------------------

available_models = models()

print("\nAvailable PyCaret regression models:")
print(available_models)


# ------------------------------------------------------------
# 4. Compare many regression models automatically
# ------------------------------------------------------------
# compare_models() tries many supported regression algorithms
# and ranks them based on metrics.
# For regression, default sorting is usually R2 unless changed.

best_model = compare_models()

print("\nBest model selected by PyCaret:")
print(best_model)

# pull() captures the latest PyCaret output table.
comparison_table = pull()

print("\nModel comparison leaderboard:")
print(comparison_table)


# ------------------------------------------------------------
# 5. Compare selected models only
# ------------------------------------------------------------
# Useful for teaching: compare only algorithms we already learned.

selected_best_model = compare_models(
    include=["lr", "dt", "rf"],
    sort="RMSE"
)

print("\nBest model among Linear Regression, Decision Tree, Random Forest:")
print(selected_best_model)

selected_comparison_table = pull()

print("\nSelected model comparison table:")
print(selected_comparison_table)


# ------------------------------------------------------------
# 6. Create a specific model manually
# ------------------------------------------------------------
# lr = Linear Regression
# dt = Decision Tree Regressor
# rf = Random Forest Regressor

lr_model = create_model("lr")
print("\nLinear Regression model:")
print(lr_model)

lr_results = pull()
print("\nLinear Regression cross-validation results:")
print(lr_results)


rf_model = create_model("rf")
print("\nRandom Forest model:")
print(rf_model)

rf_results = pull()
print("\nRandom Forest cross-validation results:")
print(rf_results)


# ------------------------------------------------------------
# 7. Tune the Random Forest model
# ------------------------------------------------------------
# Tuning tries better hyperparameters.

tuned_rf_model = tune_model(
    rf_model,
    optimize="RMSE"
)

print("\nTuned Random Forest model:")
print(tuned_rf_model)

tuned_results = pull()
print("\nTuned Random Forest results:")
print(tuned_results)


# ------------------------------------------------------------
# 8. Predict on PyCaret holdout/test data
# ------------------------------------------------------------
# If data is not provided, predict_model() uses the holdout set.

holdout_predictions = predict_model(tuned_rf_model)

print("\nHoldout predictions:")
print(holdout_predictions)

holdout_results = pull()
print("\nHoldout evaluation metrics:")
print(holdout_results)


# ------------------------------------------------------------
# 9. Predict price for new house data
# ------------------------------------------------------------

new_houses = pd.DataFrame({
    "area": [1700, 2300, 3100],
    "bedrooms": [3, 4, 5],
    "age": [4, 3, 2],
    "distance": [6, 4, 3]
})

new_predictions = predict_model(
    tuned_rf_model,
    data=new_houses
)

print("\nNew house predictions:")
print(new_predictions)


# ------------------------------------------------------------
# 10. Save the trained model
# ------------------------------------------------------------

save_model(
    tuned_rf_model,
    "house_price_pycaret_model"
)

print("\nModel saved as house_price_pycaret_model.pkl")


# ------------------------------------------------------------
# 11. Load the saved model
# ------------------------------------------------------------

loaded_model = load_model("house_price_pycaret_model")

print("\nLoaded model:")
print(loaded_model)


# ------------------------------------------------------------
# 12. Use loaded model for prediction
# ------------------------------------------------------------

loaded_model_predictions = predict_model(
    loaded_model,
    data=new_houses
)

print("\nPredictions using loaded model:")
print(loaded_model_predictions)


# ------------------------------------------------------------
# 13. Optional plots
# ------------------------------------------------------------
# These work best in Jupyter Notebook.
# In script mode, some plots may open in a browser/window depending on setup.

# plot_model(tuned_rf_model, plot="residuals")
# plot_model(tuned_rf_model, plot="error")
# plot_model(tuned_rf_model, plot="feature")
# evaluate_model(tuned_rf_model)