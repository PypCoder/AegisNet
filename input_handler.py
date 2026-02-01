import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

def get_user_input(cols):
    """Get user input via CSV, manual input, or random data."""
    input_method = st.radio("Select Input Method", ["Upload CSV", "Manual Input", "Generate Random Data"])
    user_inputs = []

    if input_method == "Upload CSV":
        st.info(" Please upload a CSV file with the following format. " \
        "Sample CSV: ")
        download_sample_csv(cols)
        uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)[cols]
            st.subheader("Preview of Uploaded Data")
            st.dataframe(df.head())
            user_inputs = df.values

    elif input_method == "Manual Input":
        st.subheader("Enter Flow Features Manually")
        manual_data = {}
        for feature in cols:
            manual_data[feature] = st.number_input(feature, value=0.0, step=1.0, format="%.2f")
        user_inputs = np.array([list(manual_data.values())])

    elif input_method == "Generate Random Data":
        n_samples = st.number_input("Number of flows to generate", min_value=1, max_value=20, value=5)
        np.random.seed(42)
        random_data = np.random.rand(n_samples, len(cols)) * 1000
        user_inputs = random_data
        st.subheader("Generated Random Data Preview")
        st.dataframe(pd.DataFrame(user_inputs, columns=cols))

    return user_inputs

def download_sample_csv(cols):
    """Provide a downloadable sample CSV file."""
    sample_data = pd.DataFrame(np.random.rand(5, len(cols))*1000, columns=cols)
    csv = sample_data.to_csv(index=False).encode('utf-8')
    st.dataframe(sample_data)
    st.download_button(
        label="📥 Download Sample CSV",
        data=csv,
        file_name="sample_flows.csv",
        mime="text/csv"
    )
