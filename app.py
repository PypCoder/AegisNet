import streamlit as st
import numpy as np
from models.predictor import predict_sample
from input_handler import get_user_input
from display import display_predictions
from visuals import plot_feature_importance, show_feature_info

# -----------------------------
# Page Config & Columns
# -----------------------------
st.set_page_config(page_title="Aegis Net", layout="centered")
st.title("🛡️ Aegis Net – AI Cyber Threat Detector")

cols = [
    "Flow Duration", "Total Fwd Packets", "Total Backward Packets",
    "Total Length of Fwd Packets", "Total Length of Bwd Packets",
    "Flow Bytes/s", "Flow Packets/s", "Packet Length Mean",
    "Packet Length Variance", "Init_Win_bytes_forward",
    "Init_Win_bytes_backward"
]

feature_descriptions = {
    "Flow Duration": "Total time taken by a network flow from its first packet to the last packet, measured in microseconds. Longer durations might indicate slow transfers, inefficient routing, or potential abnormal activity such as data exfiltration. Extremely short durations with many packets may indicate scanning or DoS activity.",
    "Total Fwd Packets": "Total number of packets sent in the forward direction (from source to destination). A sudden spike in forward packets may indicate scanning, flooding, or brute-force attempts. Consistently low numbers might indicate a dormant or incomplete flow.",
    "Total Backward Packets": "Total number of packets sent in the reverse direction (from destination to source). This helps to analyze traffic balance and response behavior. Very low backward packets compared to forward packets may indicate unresponsive servers or one-way attacks.",
    "Total Length of Fwd Packets": "Sum of the sizes (in bytes) of all forward packets. Large total size might indicate file transfers, streaming, or data exfiltration. Comparing forward and backward sizes can help detect asymmetric or suspicious flows.",
    "Total Length of Bwd Packets": "Sum of sizes (in bytes) of all backward packets. Unusually large backward data could indicate large server responses, potential exploitation, or anomalous traffic patterns.",
    "Flow Bytes/s": "Average number of bytes transmitted per second for this flow. Extremely high rates may indicate Denial-of-Service (DoS) attacks, while very low rates could indicate idle or stalled connections.",
    "Flow Packets/s": "Average number of packets transmitted per second in the flow. High packet rates might be indicative of flooding attacks, network scanning, or botnet activity, whereas low rates might represent normal or background traffic.",
    "Packet Length Mean": "The average size of packets in the flow. Atypical mean packet size might suggest abnormal behavior, such as malicious payloads, tunneling, or unusually large or small packets.",
    "Packet Length Variance": "Variance in packet sizes across the flow. Large variance may indicate mixed traffic types or anomalous activity like a combination of normal traffic and attack traffic, whereas low variance may suggest uniform or predictable traffic.",
    "Init_Win_bytes_forward": "Initial TCP window size advertised by the source. This defines how much data the sender can send before needing an acknowledgment. Unusually large or small window sizes may indicate unusual configurations or attempts to exploit TCP flow control behavior.",
    "Init_Win_bytes_backward": "Initial TCP window size advertised by the destination. Abnormal values could suggest misconfigured servers, potential attacks targeting TCP flow control, or unusual network conditions."
}


# -----------------------------
# User Input
# -----------------------------
user_inputs = get_user_input(cols)

# -----------------------------
# Make Predictions
# -----------------------------
if st.button("Predict"):
    if len(user_inputs) == 0:
        st.warning("Please provide input first!")
    else:
        with st.spinner("🕵️‍♂️ Detecting potential threats..."):
            pred, prob, importances = predict_sample(user_inputs)

        # Display results and feature explanations
        display_predictions(pred, prob, importances, cols)
        show_feature_info(cols, feature_descriptions)
        plot_feature_importance(importances, cols)
