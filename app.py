import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="AIPro Data Insights",
    layout="wide"
)

# Title and Intro
st.title("📊 AIPro Data Insights App")
st.markdown("Explore and analyze your AIPro dataset visually and interactively.")

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("AIPro.csv")
    return df

# Load the data
df = load_data()

# Sidebar Options
st.sidebar.header("Navigation")
view = st.sidebar.radio("Choose a section:", ["📄 Raw Data", "📈 Summary", "📊 Visualizations"])

# 1. Raw Data View
if view == "📄 Raw Data":
    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df)

# 2. Summary Statistics
elif view == "📈 Summary":
    st.subheader("📌 Dataset Summary")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.write("**Column Names:**", df.columns.tolist())
    st.markdown("### 🔢 Descriptive Statistics")
    st.dataframe(df.describe())

# 3. Visualizations
elif view == "📊 Visualizations":
    st.subheader("📊 Visual Analytics")

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if not numeric_cols:
        st.warning("No numeric columns available for plotting.")
    else:
        # Histogram
        st.markdown("#### 📌 Histogram")
        selected_col = st.selectbox("Select a numeric column", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        ax.set_title(f"Distribution of {selected_col}")
        st.pyplot(fig)

        # Correlation Heatmap
        if len(numeric_cols) > 1:
            st.markdown("#### 🔥 Correlation Heatmap")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax2)
            st.pyplot(fig2)
