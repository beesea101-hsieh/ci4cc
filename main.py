
import streamlit as st

st.set_page_config(page_title="CHA₂DS₂-VASc Score Calculator", layout="centered")

st.title("🧮 CHA₂DS₂-VASc Score Calculator")
st.write("Estimate stroke risk in patients with Atrial Fibrillation (AF).")

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=0, max_value=120, value=65)
    sex = st.radio("Sex", ["Male", "Female"])
    hf = st.checkbox("Congestive Heart Failure")
    htn = st.checkbox("Hypertension")
    dm = st.checkbox("Diabetes Mellitus")

with col2:
    stroke = st.checkbox("Prior Stroke/TIA/Thromboembolism")
    vascular = st.checkbox("Vascular Disease (MI, PAD, aortic plaque)")

# Score calculation
score = 0
if hf:
    score += 1
if htn:
    score += 1
if age >= 75:
    score += 2
elif 65 <= age < 75:
    score += 1
if dm:
    score += 1
if stroke:
    score += 2
if vascular:
    score += 1
if sex == "Female":
    score += 1

# Output
st.subheader("Results")
st.write(f"**CHA₂DS₂-VASc Score:** {score}")

# Optional interpretation
if score == 0:
    st.success("Low risk. Consider no anticoagulation.")
elif score == 1:
    if sex == "Female":
        st.info("Score of 1 due to female sex only is generally considered low risk.")
    else:
        st.warning("Moderate risk. Consider anticoagulation based on clinical judgment.")
else:
    st.error("High risk. Oral anticoagulation is recommended.")

st.markdown("---")
st.caption("This tool is for educational purposes only and not a substitute for clinical judgment.")
