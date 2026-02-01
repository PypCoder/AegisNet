import streamlit as st
import pandas as pd
from utils.formatter import format_top_features

def display_predictions(pred, prob, importances, cols):
    """Display predictions in a clean table or single row output."""
    n_samples = len(pred)
    results = []

    for i in range(n_samples):
        label = "Attack" if pred[i] == 1 else "Safe"
        probability = prob[i]
        top_features = format_top_features(cols, importances, k=5)

        results.append({
            "Sample": i+1,
            "Predicted Status": label,
            "Attack Probability": f"{probability:.2%}",
            "Top Features": ", ".join([f"{f}: {imp:.2f}" for f, imp in top_features])
        })

    df_results = pd.DataFrame(results)
    st.subheader("🖥️ Prediction Results")
    st.dataframe(df_results, use_container_width=True)

    # Download option
    csv = df_results.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Predictions",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv"
    )

    return df_results
