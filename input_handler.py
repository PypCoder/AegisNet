import streamlit as st
import pandas as pd
import numpy as np
from utils.generate_random_data import generate_random_data

SAFE_SAMPLE = {
    "Flow Duration": 12000,
    "Total Fwd Packets": 12,
    "Total Backward Packets": 10,
    "Total Length of Fwd Packets": 1500,
    "Total Length of Bwd Packets": 1400,
    "Flow Bytes/s": 300,
    "Flow Packets/s": 5,
    "Packet Length Mean": 120,
    "Packet Length Variance": 50,
    "Init_Win_bytes_forward": 8192,
    "Init_Win_bytes_backward": 8192,
}

ATTACK_SAMPLE = {
    "Flow Duration": 5715405,
    "Total Fwd Packets": 3,
    "Total Backward Packets": 1,
    "Total Length of Fwd Packets": 0,
    "Total Length of Bwd Packets": 0,
    "Flow Bytes/s": 0,
    "Flow Packets/s": 0.699862914,
    "Packet Length Mean": 0,
    "Packet Length Variance": 0,
    "Init_Win_bytes_forward": 29200,
    "Init_Win_bytes_backward": 28960,
}

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
        st.subheader("Enter Network Flow Features")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🟢 Load Safe Example"):
                st.session_state["preset"] = "safe"
        with col2:
            if st.button("🔴 Load Attack Example"):
                st.session_state["preset"] = "attack"
        manual_data = {}
        for feature in cols:
            if "preset" in st.session_state:
                if st.session_state["preset"] == "safe":
                    default_value = SAFE_SAMPLE.get(feature, 0.0)
                elif st.session_state["preset"] == "attack":
                    default_value = ATTACK_SAMPLE.get(feature, 0.0)
                else:
                    default_value = 0.0
            else:
                default_value = 0.0
            manual_data[feature] = st.number_input(
                feature,
                value=float(default_value),
                step=1.0,
                format="%.2f"
            )
        user_inputs = np.array([list(manual_data.values())])


    elif input_method == "Generate Random Data":
        n_samples = st.number_input("Number of flows to generate", value=5)
        user_inputs = generate_random_data(n_samples)
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
