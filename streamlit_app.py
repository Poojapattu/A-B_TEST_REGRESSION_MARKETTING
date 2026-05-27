import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(page_title="Marketing Analytics Dashboard", layout="wide")

st.title("📊 Marketing A/B Testing + Prediction Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    # -------------------------
    # VALIDATION
    # -------------------------
    required_cols = ["clicks", "impressions", "conversions", "platform", "cost"]

    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        st.error(f"Missing columns: {missing}")
        st.stop()

    # -------------------------
    # FEATURE ENGINEERING
    # -------------------------
    df["ctr"] = df["clicks"].div(df["impressions"].replace(0, pd.NA))
    df["cr"] = df["conversions"].div(df["clicks"].replace(0, pd.NA))
    df = df.dropna()

    # -------------------------
    # KPIs
    # -------------------------
    st.subheader("📊 KPIs")

    col1, col2, col3 = st.columns(3)

    col1.metric("Avg CTR", f"{df['ctr'].mean():.2%}")
    col2.metric("Avg CR", f"{df['cr'].mean():.2%}")
    col3.metric("Total Conversions", int(df["conversions"].sum()))

    # -------------------------
    # BUSINESS INSIGHTS (REAL ACTIONABLE)
    # -------------------------
    st.subheader("💡 Business Insights")

    platform_ctr = df.groupby("platform")["ctr"].mean().sort_values()

    best_platform = platform_ctr.idxmax()
    worst_platform = platform_ctr.idxmin()

    st.success(f"✔ Best Platform: {best_platform} (highest CTR)")
    st.error(f"⚠ Worst Platform: {worst_platform} (needs improvement)")

    st.write("### Platform CTR Ranking")
    st.dataframe(platform_ctr)

    st.write("### Action Recommendation")

    if platform_ctr.iloc[-1] < platform_ctr.mean():
        st.warning("👉 Shift more budget to top-performing platforms")
    else:
        st.info("👉 Platform performance is balanced, optimize creatives next")

    # -------------------------
    # PLATFORM PERFORMANCE
    # -------------------------
    st.subheader("📊 Platform Performance")

    platform_perf = df.groupby("platform")[["clicks", "conversions", "cost"]].sum()
    st.bar_chart(platform_perf)

    # -------------------------
    # A/B TESTING
    # -------------------------
    st.subheader("🧪 A/B Testing Insight")

    if "group" in df.columns:
        ab_result = df.groupby("group")[["ctr", "cr"]].mean()
        st.dataframe(ab_result)
        st.bar_chart(ab_result)
    else:
        st.info("No 'group' column found")

    # -------------------------
    # CORRELATION HEATMAP
    # -------------------------
    st.subheader("🔥 Correlation Heatmap")

    corr_cols = ["impressions", "clicks", "cost", "conversions", "ctr"]
    corr = df[corr_cols].corr()

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

    st.pyplot(fig)

    # -------------------------
    # PREDICTION MODEL (IMPROVED)
    # -------------------------
    st.subheader("🤖 CTR Prediction Model")

    features = ["impressions", "clicks", "cost", "conversions"]

    X = df[features]
    y = df["ctr"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # -------------------------
    # MODEL PERFORMANCE
    # -------------------------
    st.subheader("📈 Model Performance")

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    col1, col2 = st.columns(2)
    col1.metric("R² Score", f"{r2:.3f}")
    col2.metric("MAE", f"{mae:.5f}")

    # -------------------------
    # PREDICTIONS
    # -------------------------
    df["predicted_ctr"] = model.predict(X)

    st.subheader("🔮 Actual vs Predicted CTR")

    st.dataframe(df[["ctr", "predicted_ctr"]].head(10))

    # -------------------------
    # FEATURE IMPORTANCE
    # -------------------------
    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    st.subheader("📌 Feature Importance")
    st.bar_chart(importance.set_index("Feature"))

else:
    st.warning("⬆️ Upload CSV to generate insights")