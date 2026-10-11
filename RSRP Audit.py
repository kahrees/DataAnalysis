# ntwkaudit.py

import streamlit as st
import pandas as pd


# Receives the clean CSV file


st.title("Network Audit")

st.header("Upload Documents")

uploaded_file = st.file_uploader(
   "Upload CSV file",
        type=["csv"],
        help="Upload the cleaned CSV file for audit",
    )

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Success message
    st.success("File successfully uploaded!")
    
    st.subheader("Confirm Data is Accurate")
    # Show the dataframe 
    st.dataframe(df.head())

    # Change type to string
    df = df.astype(str)

    # Clear whitespace
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df_filtered = df[df['rsrpCritical'] != '{timeToTrigger=160, threshold=-119, hysteresis=10}']

    st.header("5G Cells to be Audited")
    st.write(f"{len(df_filtered)} cells need to be audited.")
    st.dataframe(df_filtered[['McpcPSCellProfileId', 'rsrpCritical']])

    

else:
    st.info("Please upload a CSV file to get started.")



