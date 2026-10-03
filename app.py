import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_performance_model.pkl")
preprocessor = joblib.load("student_preprocessor.pkl")

st.title("🎓 Student Performance Prediction System")

st.write("Enter the student's details to predict their final performance.")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=15,
        max_value=25,
        value=17,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["F", "M"]
    )

    famsize = st.selectbox(
        "Family Size",
        ["LE3", "GT3"]
    )

with col2:
    school = st.selectbox(
        "School",
        ["GP", "MS"]
    )

    address = st.selectbox(
        "Address",
        ["U", "R"]
    )

    Pstatus = st.selectbox(
        "Parent Status",
        ["T", "A"]
    )
# Family & education
st.header("👨‍👩‍👧 Family & Education")

col1, col2 = st.columns(2)

with col1:
    Medu = st.number_input(
        "Mother's Education Level",
        min_value=0,
        max_value=4,
        value=2,
        step=1
    )

    Mjob = st.selectbox(
        "Mother's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

    reason = st.selectbox(
        "Reason for Choosing School",
        ["home", "reputation", "course", "other"]
    )

with col2:
    Fedu = st.number_input(
        "Father's Education Level",
        min_value=0,
        max_value=4,
        value=2,
        step=1
    )

    Fjob = st.selectbox(
        "Father's Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

    guardian = st.selectbox(
        "Guardian",
        ["mother", "father", "other"]
    )

# Academic Information
st.header("📚 Academic Information")

col1, col2 = st.columns(2)

with col1:
    traveltime = st.number_input(
        "Travel Time",
        min_value=1,
        max_value=4,
        value=2,
        step=1
    )

    studytime = st.number_input(
        "Weekly Study Time",
        min_value=1,
        max_value=4,
        value=2,
        step=1
    )

    failures = st.number_input(
        "Number of Past Failures",
        min_value=0,
        max_value=3,
        value=0,
        step=1
    )

with col2:
    schoolsup = st.selectbox(
        "Extra Educational Support",
        ["yes", "no"]
    )

    famsup = st.selectbox(
        "Family Educational Support",
        ["yes", "no"]
    )

    paid = st.selectbox(
        "Extra Paid Classes",
        ["yes", "no"]
    )





# Activities and Internet
st.header("🌐 Activities & Internet")

col1, col2 = st.columns(2)

with col1:
    activities = st.selectbox(
        "Extra-curricular Activities",
        ["yes", "no"]
    )

    nursery = st.selectbox(
        "Attended Nursery School",
        ["yes", "no"]
    )

    higher = st.selectbox(
        "Wants Higher Education",
        ["yes", "no"]
    )

with col2:
    internet = st.selectbox(
        "Internet Access",
        ["yes", "no"]
    )

    romantic = st.selectbox(
        "Romantic Relationship",
        ["yes", "no"]
    )
# Social and Health Information
st.header("🧠 Social & Health Information")

col1, col2 = st.columns(2)

with col1:
    famrel = st.number_input(
        "Family Relationship Quality",
        min_value=1,
        max_value=5,
        value=4,
        step=1
    )

    freetime = st.number_input(
        "Free Time",
        min_value=1,
        max_value=5,
        value=3,
        step=1
    )

    health = st.number_input(
        "Health Status",
        min_value=1,
        max_value=5,
        value=3,
        step=1
    )

with col2:
    goout = st.number_input(
        "Going Out Frequency",
        min_value=1,
        max_value=5,
        value=3,
        step=1
    )

    absences = st.number_input(
        "Number of Absences",
        min_value=0,
        max_value=100,
        value=5,
        step=1
    )

with st.expander("🍹 Optional Lifestyle Information"):
    st.caption(
        "These fields are included because they were part of the original dataset."
    )

    Dalc = st.number_input(
        "Workday Alcohol Consumption",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        help="1 = very low, 5 = very high"
    )

    Walc = st.number_input(
        "Weekend Alcohol Consumption",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        help="1 = very low, 5 = very high"
    )
# Previous Grades
st.header("📊 Previous Grades")

col1, col2 = st.columns(2)

with col1:
    G1 = st.number_input(
        "First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10,
        step=1
    )

with col2:
    G2 = st.number_input(
        "Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10,
        step=1
    )



# Prediction button

if st.button("🔮 Predict Student Performance"):

    input_data = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],
        "famsize": [famsize],
        "Pstatus": [Pstatus],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "Mjob": [Mjob],
        "Fjob": [Fjob],
        "reason": [reason],
        "guardian": [guardian],
        "traveltime": [traveltime],
        "studytime": [studytime],
        "failures": [failures],
        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "nursery": [nursery],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "Dalc": [Dalc],
        "Walc": [Walc],
        "health": [health],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    input_processed = preprocessor.transform(input_data)

    prediction = model.predict(input_processed)[0]
    st.subheader("🎯 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted Final Score",
            value=f"{prediction:.2f} / 20"
    )

    with col2:
        if prediction < 10:
            performance = "Needs Improvement"
        elif prediction < 15:
            performance = "Good"
        else:
            performance = "Excellent"

        st.metric(
            label="Performance Level",
            value=performance
    )
    

    

    st.subheader("📈 Performance Level")
    st.info(performance)


    # Recommendations

    st.subheader("💡 Recommendations")

    recommendations = []

    if studytime <= 2:
        recommendations.append(
            "Consider increasing your regular study time."
        )

    if failures > 0:
        recommendations.append(
            "Focus on subjects where you previously faced difficulties."
        )

    if absences > 10:
        recommendations.append(
            "Try to reduce unnecessary absences and attend classes regularly."
        )

    if G2 < G1:
        recommendations.append(
            "Review recent topics and focus on improving your recent performance."
        )

    if not recommendations:
        recommendations.append(
            "Keep following your current study routine and maintain your progress."
        )
    for recommendation in recommendations:
        st.info("💡 " + recommendation)
    