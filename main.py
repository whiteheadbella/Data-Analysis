import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io  # Needed for capturing data.info()

# Streamlit App Title
st.title("❤️ Heart Disease Analysis")
st.title(" Heart Disease Insights & Prevention Report❤️")
#  1.Methodology
st.markdown("### 🧪 Methodology")
st.markdown("""
This analysis follows a structured data workflow to explore and interpret the heart disease dataset.
#### A. Data Understanding
- Reviewed dataset structure using `.head()`, `.info()`, and `.describe()`.
- Identified key features such as `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, and `target`.
#### B. Data Preprocessing
- Handled categorical values (e.g., mapped `sex`, `cp`, `fbs`, `target` to human-readable labels).
#### C. Exploratory Data Analysis 
- Used visualizations (bar plots, histograms, KDE plots) to identify distributions.
- Compared chest pain types, fasting blood sugar, cholesterol, and blood pressure by gender and heart disease status.
- Highlighted strong correlations between features like chest pain type and target (heart disease).
#### D. Insights
- Ranked features based on their relationship to heart disease.
- Summarized findings into digestible insights.
- Suggested prevention strategies based on observed risk patterns.
#### E. Communication
- Used Streamlit to create an interactive app combining data, visualizations, and narrative.
- Organized content for clarity: analysis section, insights section, and recommendations.

> **Tools used**: Python, Pandas, Seaborn, Matplotlib, Plotly, Streamlit.
""")

#  Introduction
st.markdown("### 🧩 Introduction: Why This Matters")
st.write(
    "Heart disease is the leading cause of death globally. "
    "Using real patient data, we explore the key risk factors that contribute to heart disease, "
    "and how proactive prevention can save lives."
)

# Load the dataset
file_path = 'input/heart-disease-dataset/heart.csv'

if os.path.exists(file_path):
    data = pd.read_csv(file_path)

    # Show basic data info
    st.subheader("Dataset Preview")
    st.write("Top 5 Rows:")
    st.dataframe(data.head())

    st.write("Bottom 5 Rows:")
    st.dataframe(data.tail())

    st.write(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")

    # Display dataset info using StringIO
    st.subheader("Dataset Info")
    buffer = io.StringIO()
    data.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

else:
    st.error("CSV file not found. Please check the path.")

#data information
if os.path.exists(file_path):
    data = pd.read_csv(file_path)

    st.subheader("Overall Statistics About the Dataset")
    st.dataframe(data.describe(include='all'))
    st.write("")

# 2. Who is Most Affected?
st.markdown("### 🔍 1. Who Is Most Affected?")
st.markdown("""
- **Gender**: Males show a significantly higher rate of heart disease than females.
- **Age**: Risk increases with age, especially beyond 60.
> 🎯 **Insight**: Men-aged from 55 to 60 were the high-risk group.
""")
    # Count how many have and don't have heart disease
counts = data['target'].value_counts()
st.write(f"People without heart disease: {counts[0]}")
st.write(f"People with heart disease: {counts[1]}")

    # Create bar chart
fig = px.bar(
        x=['People without heart disease', 'People with heart disease'],
        y=[counts[0], counts[1]],
        labels={'x': 'Condition', 'y': 'Number of People'},
        title="People with heart disease vs People without heart disease"
    )
st.plotly_chart(fig)

#Find Count of Male & Female in this Dataset
# Show gender counts
st.subheader("Counts of Male & Female in this Dataset")
gender_counts = data['sex'].value_counts()
st.write(f"Female: {gender_counts[0]}")
st.write(f"Male: {gender_counts[1]}")

# Plot gender distribution
fig, ax = plt.subplots()
sns.countplot(data=data, x='sex', ax=ax)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Female', 'Male'])
ax.set_title("Gender Distribution")
st.pyplot(fig)

st.subheader("Which Gender Has More Heart Disease?")

# Map sex values to labels (0 = female, 1 = male)
data['sex'] = data['sex'].map({0: 'Female', 1: 'Male'})
data['target'] = data['target'].map({0: 'No Disease', 1: 'Disease'})

# Countplot of Heart Disease by Gender
fig, ax = plt.subplots()
sns.countplot(data=data, x='sex', hue='target', ax=ax)
ax.set_title("Heart Disease Count by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
st.pyplot(fig)

# Optional: Display numbers
st.subheader("Heart Disease Counts by Gender")
gender_disease_counts = data[data['target'] == 'Disease']['sex'].value_counts()
st.write(gender_disease_counts)

#age distribution by gender or heart disease status
st.subheader("Age Distribution in the Dataset -Highest By 60years old were likely to have a heart disease")

# Plot age distribution using Seaborn histplot
fig, ax = plt.subplots()
sns.histplot(data['age'], bins=20, kde=True, ax=ax)
ax.set_title("Distribution of Age")
ax.set_xlabel("Age")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Plot the column bar chart
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x='cp', palette='Set2')

# 3. Chest Pain Types
st.markdown("### ❤️ 2. Chest Pain Types: A Silent Warning")
st.markdown("""
- **Non-anginal** individuals (chest pain that is not related to the heart) had the **highest rate** of heart disease.
> 🎯 **Insight**: People without symptoms may still be at serious risk!
""")
# Plot in Streamlit
st.subheader("Chest Pain Type Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=data, x='cp', palette='Set2', ax=ax)
ax.set_title("Chest Pain Type Distribution")
ax.set_xlabel("Chest Pain Type")
ax.set_ylabel("Number of People")
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Typical angina','Atypical angina','Non-anginal pain','Asymptomatic'], rotation=20)
st.pyplot(fig)

# Streamlit heading
st.subheader("Chest Pain Type Distribution by Heart Disease")

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=data, x='cp', hue='target', palette='Set2', ax=ax)

# Format axes
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'], rotation=20)
ax.set_xlabel("Chest Pain Type")
ax.set_ylabel("Number of Patients")
ax.set_title("Chest Pain Type Distribution by Heart Disease")
ax.legend(title="Heart Disease", labels=["No-disease", "Disease"])
st.pyplot(fig)

# 4. Fasting Blood Sugar
st.markdown("### 🩸 3. Fasting Blood Sugar (FBS)")
st.markdown("""
- FBS ≤120 mg/dL **strongly predictive** in this dataset.
> 🎯 **Insight**: Still important for overall cardiovascular health, especially in diabetic patients.
""")

# Map once
if data['fbs'].dtype in [int, float]:
    data['fbs'] = data['fbs'].map({0: '≤ 120 mg/dL', 1: '> 120 mg/dL'})
if data['target'].dtype in [int, float]:
    data['target'] = data['target'].map({0: 'No Disease', 1: 'Disease'})

# Plot
st.subheader("Fasting Blood Sugar vs Heart Disease Status")
fig, ax = plt.subplots()
sns.countplot(data=data, x='fbs', hue='target', ax=ax)
ax.set_title("Heart Disease Count by Fasting Blood Sugar")
ax.set_xlabel("Fasting Blood Sugar Level")
ax.set_ylabel("Patients Count")
st.pyplot(fig)

# 5. Resting Blood Pressure
st.markdown("### 🧘‍♂️ 4. Resting Blood Pressure")
st.markdown("""
- High resting BP (>120 mm Hg) is more common in heart disease patients.
> 🎯 **Insight**: Target **~100 mm Hg** resting BP for prevention.
""")

# Safely map gender only if needed
if data['sex'].dtype in [int, float]:
    data['sex'] = data['sex'].map({0: 'Female', 1: 'Male'})

# Drop NaNs from trestbps and sex
plot_data = data[['trestbps', 'sex']].dropna()

# Plot in Streamlit
st.subheader("🩺 Resting Blood Pressure Distribution by Gender")

fig, ax = plt.subplots(figsize=(10, 5))
sns.kdeplot(data=plot_data, x='trestbps', hue='sex', fill=True, ax=ax)

ax.set_title("Resting Blood Pressure (trestbps) by Gender")
ax.set_xlabel("Resting Blood Pressure (mm Hg)")
ax.set_ylabel("Density")
st.pyplot(fig)

# 6. Top Risk Factor Table
st.markdown("### 📊 Top Risk Factors (Based on Visual Trends)")
st.table({
    "Risk Association": [
        "🚨 Strongest red flag =Age 60",
        "🚨 Higher prevalence",
        "🚨 More affected overall= Men",
        "⚠️ Consistent among patients",
        "⚠️ FBS"
    ]
})

#7. Prevention And Recommendations
st.markdown("### 🛡️ Prevention Recommendations")
st.markdown("""
To reduce the risk of heart disease, these preventive actions are highly recommended:

1. ✅ **Routine Screenings**  
   Even when asymptomatic, regular checkups can detect early warning signs.

2. ✅ **Monitor Blood Pressure**  
   Maintain a target of around **120/80 mm Hg** for optimal cardiovascular health.

3. ✅ **Heart-Healthy Lifestyle**  
   Eat a balanced diet, stay active, avoid smoking, and reduce stress.

4. ✅ **Evaluate Chest Pain Promptly**  
   Even mild or unusual chest discomfort should not be ignored.

5. ✅ **Manage Risk Factors Together**  
   Don’t treat blood pressure, cholesterol, and blood sugar in isolation—address them **together** as part of a lifestyle plan.
""")

# 10. Conclusion
st.markdown("### 🎯 Final Thoughts & Conclusion")
st.success(
    "Heart disease doesn’t always present with loud symptoms. Many patients—especially older males—can appear "
    "asymptomatic yet still be at high risk. This analysis shows the importance of early detection, lifestyle management, "
    "and regular health screenings. Prevention is not just about fixing problems when they appear—"
    "it's about staying one step ahead. ❤️"
)

