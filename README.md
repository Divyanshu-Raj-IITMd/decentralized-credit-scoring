# 📊 Decentralized Credit Scoring App

A privacy-preserving, AI-powered credit scoring system that predicts a user's creditworthiness using behavioral and financial data. Built using Streamlit, XGBoost, SHAP, and includes optional decentralized storage with IPFS and Ethereum smart contracts.

---

## 🚀 Features

- ✅ Credit prediction with an optimized XGBoost model (via Optuna tuning)
- 📊 Explainability using SHAP Waterfall plots
- 🧠 Behavioral Scoring based on UPI usage, app installs, SMS patterns, etc.
- 📥 Generate & download credit reports (HTML)
- 🏅 Trust badges (🥉 Bronze, 🥈 Silver, 🥇 Gold)
- 🤖 Built-in chatbot assistant
- 📂 Local session history tracking
- 📡 Optional: Upload to IPFS or Ethereum-based smart contracts

---

## 🖥️ Tech Stack

| Component         | Technology       |
|------------------|------------------|
| UI               | Streamlit        |
| ML Model         | XGBoost + Optuna |
| Explainability   | SHAP             |
| Data             | Pandas (Synthetic) |
| Reports          | Jinja2 + HTML    |
| Decentralization | IPFS + Web3.py (Optional) |

---

## 🗂️ Project Structure

```

decentralized-credit-scoring/
├── app/
│   ├── dashboard.py
│   ├── utils.py
├── models/
│   ├── model\_training.py
│   ├── shap\_explain.py
│   └── credit\_model.pkl
├── data/
│   └── create\_synthetic\_data.py
├── ipfs\_integration/
│   └── upload\_to\_ipfs.py
├── blockchain/
│   ├── smart\_contract.sol
│   ├── deploy\_contract.py
├── reports/
│   └── report\_template.html
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/decentralized-credit-scoring.git
cd decentralized-credit-scoring
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
# source venv/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Generate synthetic data and train the model

```bash
python data/create_synthetic_data.py
python models/model_training.py
```

### 5. Run the Streamlit app

```bash
streamlit run app/dashboard.py
```

---

## 📄 Report Generation

* Credit reports are generated in the `reports/` folder as `HTML` files.
* You can download them directly from the app.
* PDF support via `pdfkit` and `wkhtmltopdf` is optional.

---

## 🌐 Blockchain Integration (Optional)

* Store credit score + IPFS hash on Ethereum or Polygon testnets.
* Smart contract included in `blockchain/smart_contract.sol`
* Use `Web3.py` to interact with the contract.
* Metamask-based authentication can be added for DID integration.

---

## 📡 IPFS Integration (Optional)

* Upload reports to decentralized storage using [Web3.Storage](https://web3.storage/) or [Pinata](https://pinata.cloud/).
* Requires API key in `.env` file.

---

## 🤖 Chatbot Assistant

Ask simple questions about:

* What affects your credit score
* How to improve it
* What trust badges mean
* Report downloads

---

## 📂 View My History

* All user predictions are stored locally in the current Streamlit session.
* Access history via the “📂 View My History” section in the app.

---

## 📜 License

This project is licensed under the MIT License. Feel free to fork, modify, and build upon it.

---

## 🙌 Contributions

Found a bug or have an idea to improve? PRs are welcome!

---

## 💡 Future Enhancements

* Full DID wallet integration (Metamask)
* Language support (Hindi, Tamil, etc.)
* Mobile-first UI
* Decentralized loan eligibility prediction

```

---

Let me know if you want:
- Screenshots or demo links added  
- GitHub badges for license, Streamlit, etc.  
- `live app` badge if you deploy this on Streamlit Cloud  

Happy coding! 🚀
```
