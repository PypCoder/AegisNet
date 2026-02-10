import streamlit as st
import pandas as pd
from utils.formatter import format_top_features

def display_predictions(pred, prob, importances, cols):
    n_samples = len(pred)

    st.subheader("🖥️ Prediction Results")

    if n_samples <= 3:
        for i in range(n_samples):
            label = "🚨 Attack Detected" if pred[i] == 1 else "✅ Safe Traffic"
            probability = prob[i]
            top_features = format_top_features(cols, importances, k=2)

            with st.container(border=True):
                st.markdown(f"### 🔍 Network Flow {i + 1}")
                st.metric(
                    label="Attack Probability",
                    value=f"{probability:.2%}",
                    delta="High Risk" if pred[i] == 1 else "Low Risk"
                )

                st.success(label) if pred[i] == 0 else st.error(label)

                st.markdown("**Top Contributing Features**")
                for f, imp in top_features:
                    st.progress(
                        min(float(imp), 1.0),
                        text=f"{f} ({imp:.2f})"
                    )

        return None

    results = []
    for i in range(n_samples):
        label = "Attack" if pred[i] == 1 else "Safe"
        results.append({
            "Sample": i + 1,
            "Predicted Status": label,
            "Attack Probability": f"{prob[i]:.2%}"
        })

    df_results = pd.DataFrame(results)
    st.dataframe(df_results, use_container_width=True)

    # Download option
    csv = df_results.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Predictions",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv"
    )

    return df_results
