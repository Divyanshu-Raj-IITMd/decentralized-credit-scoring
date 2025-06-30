import sys
import os
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from joblib import load
from datetime import datetime
from googletrans import Translator

# Fix import path for submodules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.utils import save_user_input, load_user_history, generate_html_report

# Load trained model
model = load("models/credit_model.pkl")

# Streamlit setup
st.set_page_config(page_title="Decentralized Credit Scoring", layout="centered")
st.title("📊 Decentralized Credit Scoring")
st.markdown("Enter your data to check if you're creditworthy.")

# Define tabs
tab1, tab2 = st.tabs(["🏠 Check Score", "📈 SHAP & Reports"])

with tab1:
    with st.form("credit_form"):
        income = st.slider("Monthly Income (₹)", 10000, 100000, 40000)
        phone_paid = st.radio("Phone Bill Paid On Time?", ["Yes", "No"]) == "Yes"
        electricity = st.slider("Electricity Usage (kWh)", 100, 1000, 300)
        apps = st.slider("Number of Apps Installed", 10, 200, 100)
        social_hours = st.slider("Social Media Hours per Day", 0.0, 10.0, 3.5)
        upi = st.slider("UPI Transaction Count", 0, 50, 10)
        sms = st.slider("SMS Notifications", 0, 20, 5)
        loc = st.selectbox("Location Cluster", [0, 1, 2])
        submitted = st.form_submit_button("Check Creditworthiness")

    if submitted:
        input_data = pd.DataFrame([{
            "monthly_income": income,
            "phone_bill_paid_on_time": int(phone_paid),
            "electricity_usage": electricity,
            "num_apps_installed": apps,
            "social_media_hours": social_hours,
            "upi_txn_count": upi,
            "sms_notifs": sms,
            "location_cluster": loc,
        }])

        prediction = model.predict(input_data)[0]
        save_user_input(input_data, int(prediction))

        st.markdown("### 💬 Prediction Result")
        if prediction == 1:
            st.success("✅ Creditworthy!")
        else:
            st.error("❌ Not Creditworthy.")

        # Trust badge
        if income < 30000:
            st.markdown("🏅 **Trust Level:** 🥉 Bronze")
        elif income < 70000:
            st.markdown("🏅 **Trust Level:** 🥈 Silver")
        else:
            st.markdown("🏅 **Trust Level:** 🥇 Gold")

        # Credit points (gamification)
        score_points = 0
        if phone_paid: score_points += 20
        if upi > 10: score_points += 20
        if sms > 5: score_points += 10
        if social_hours < 4: score_points += 10
        if income > 50000: score_points += 20
        st.progress(score_points / 100)
        st.markdown(f"🌟 **Credit Points:** {score_points}/100")

        # Tips for improvement
        st.subheader("💡 Tips to Improve Creditworthiness")
        if prediction == 0:
            if income < 30000: st.info("Try increasing your monthly income or getting a stable income source.")
            if upi < 5: st.info("Increase your UPI transaction count to show financial activity.")
            if phone_paid == 0: st.info("Ensure bills like phone/electricity are paid on time.")
            if social_hours > 5: st.info("Reduce social media time to boost productive app usage.")

        # Translate (bonus)
        with st.sidebar.expander("🌍 Translate to Hindi"):
            translator = Translator()
            text = "You are Creditworthy!" if prediction == 1 else "You are Not Creditworthy"
            translation = translator.translate(text, src='en', dest='hi')
            st.write("🗣️ " + translation.text)

        # Save prediction to CSV
        input_data["prediction"] = prediction
        input_data["timestamp"] = datetime.now()
        input_data.to_csv("data/user_predictions.csv", mode='a', header=not os.path.exists("data/user_predictions.csv"), index=False)

with tab2:
    # SHAP Explanation
    st.subheader("🔍 SHAP Explanation")
    try:
        # Get the last input
        last_data = pd.read_csv("data/user_predictions.csv").iloc[-1]
        sample = pd.DataFrame([{
            "monthly_income": last_data["monthly_income"],
            "phone_bill_paid_on_time": last_data["phone_bill_paid_on_time"],
            "electricity_usage": last_data["electricity_usage"],
            "num_apps_installed": last_data["num_apps_installed"],
            "social_media_hours": last_data["social_media_hours"],
            "upi_txn_count": last_data["upi_txn_count"],
            "sms_notifs": last_data["sms_notifs"],
            "location_cluster": last_data["location_cluster"],
        }])
        explainer = shap.Explainer(model)
        shap_values = explainer(sample)
        shap.plots.waterfall(shap_values[0], show=False)
        st.pyplot(plt.gcf())
        plt.clf()
    except Exception as e:
        st.warning(f"SHAP explanation failed: {e}")

    # Global SHAP (optional)
    if st.checkbox("📊 Show Global SHAP Summary"):
        try:
            bg_data = pd.read_csv("data/synthetic_credit_data.csv").drop("creditworthy", axis=1)
            explainer = shap.Explainer(model)
            shap_vals = explainer(bg_data)
            shap.summary_plot(shap_vals, bg_data, show=False)
            st.pyplot(plt.gcf())
            plt.clf()
        except:
            st.warning("Failed to show global SHAP summary.")

    # Report
    st.subheader("📥 Download Credit Report")
    report_data = sample.to_dict(orient="records")[0]
    report_data["creditworthy"] = int(last_data["prediction"])
    path = generate_html_report(report_data)
    with open(path, "r", encoding="utf-8") as f:
        st.download_button("⬇️ Download Credit Report (HTML)", f.read(), file_name="credit_report.html", mime="text/html")

# History
st.markdown("---")
with st.expander("📂 View My History"):
    history = load_user_history()
    if history:
        for i, (entry, pred) in enumerate(history[::-1], 1):
            st.write(f"🔹 Entry {i}: {entry}, Prediction: {'✅' if pred else '❌'}")
    else:
        st.info("No history found this session.")

# Chatbot
with st.sidebar.expander("🤖 Credit Assistant"):
    q = st.text_input("Ask me anything:")
    if q:
        if "score" in q.lower():
            st.write("Your credit score is determined using your income, utility payments, app usage, etc.")
        elif "improve" in q.lower():
            st.write("Pay bills on time, increase UPI usage, and reduce social media time to improve credit score.")
        elif "badge" in q.lower():
            st.write("Badges are awarded based on income and credit status.")
        elif "report" in q.lower():
            st.write("You can download your credit report after checking your creditworthiness.")
        else:
            st.write("I'm still learning! Try asking about score, badges, or reports.")
