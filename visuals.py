import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_feature_importance(importances, cols):
    """Feature importance horizontal bar plot at the very end."""
    feat_df = pd.DataFrame(sorted(zip(cols, importances), key=lambda x: x[1], reverse=True),
                           columns=["Feature", "Importance"])
    fig, ax = plt.subplots(figsize=(8,5))
    sns.barplot(x="Importance", y="Feature", data=feat_df, palette="viridis", ax=ax)
    ax.set_title("Feature Importance Overview")
    st.pyplot(fig)

def show_feature_info(cols, feature_descriptions):
    """Display expandable feature info for each column."""
    st.subheader("ℹ️ Feature Explanations")
    for feature in cols:
        with st.expander(feature):
            st.write(feature_descriptions.get(feature, "No description available."))
