import shap
import xgboost
import pandas as pd
from joblib import load
import matplotlib.pyplot as plt
from shap.plots import force
import shap


model = load("models/credit_model.pkl")
data = pd.read_csv("data/synthetic_credit_data.csv")
X = data.drop("creditworthy", axis=1)

explainer = shap.Explainer(model)
shap_values = explainer(X)

# Save global summary
plt.title("SHAP Summary")
shap.plots.beeswarm(shap_values, show=False)
plt.savefig("models/global_shap_summary.png")

# Generate force plot for one sample
sample = X.iloc[[0]]
shap.initjs()
force_plot_html = shap.plots.force(shap_values[0], matplotlib=False)

with open("models/force_plot.html", "w", encoding="utf-8") as f:
    f.write(str(force_plot_html)) 