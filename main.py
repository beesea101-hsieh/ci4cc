import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Export Data to Excel", layout="centered")

st.title("📊 Export Data to Excel (.xlsx)")

st.write("You can upload your own CSV file or use sample data below.")

# Option to upload a file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
else:
    # Sample Data
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Paris', 'Tokyo']
    })

st.subheader("📋 Data Preview")
st.dataframe(df, use_container_width=True)

# Function to convert DataFrame to Excel in memory
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

xlsx_data = to_excel(df)

st.subheader("⬇️ Download Excel File")
st.download_button(
    label="Download as XLSX",
    data=xlsx_data,
    file_name='exported_data.xlsx',
    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Pandas.")
