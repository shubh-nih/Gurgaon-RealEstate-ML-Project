# 🏙️ Gurgaon Real Estate ML Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg?logo=streamlit)](https://gurgaon-estate-mlnihs.streamlit.app/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Model-orange.svg?logo=scikit-learn)](https://scikit-learn.org/)
[![GitHub repo](https://img.shields.io/badge/View%20on-GitHub-black.svg?logo=github)](https://github.com/shubh-nih/Gurgaon-RealEstate-ML-Project)

> 🧠 **End to End Machine Learning Project for Real Estate Price Prediction & Recommendation System**
>
> Predict property prices, analyze data trends, and recommend similar properties across **Gurgaon, India**.  
> Fully integrated ML + Streamlit app, deployed here 👉 [**Live Demo**](https://gurgaon-estate-mlnihs.streamlit.app/)

---

## 📖 Overview

This project builds a **complete data science pipeline** to predict housing prices in Gurgaon and recommend similar listings based on user preferences.

It covers:
- Data collection, cleaning, and EDA  
- Feature engineering and model building  
- Evaluation and recommendation system  
- Frontend UI built with Streamlit for interaction  

---

## ✨ Key Features

✅ **Price Prediction** - Predict prices using ML models trained on real-world Gurgaon housing data.  
✅ **Recommendation Engine** - Suggests similar properties using hybrid cosine similarity.  
✅ **Analytics Dashboard** - Explore sector-wise price distributions and market patterns.  
✅ **Streamlit App** - Beautiful UI for non-technical users.  
✅ **End to End ML Pipeline** - Clean structure for reproducibility and scaling.

---

## 📊 Model Performance

| Model | R² Score | Cross Validation Score (Mean ± Std) |
|------------|----------|---------------------------------|
| **Random Forest** | 0.90 | 0.89 ± 0.01 |

---
## 📂 Dataset Information

- **Source:** [99acres.com](https://www.99acres.com/)  
- **Description:** Real world housing listings from Gurgaon, India.  
- **Usage:** The dataset was **scraped and preprocessed** solely for **academic and educational purposes**.  

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Language** | Python |
| **Libraries** | pandas, numpy, scikit-learn, matplotlib, seaborn |
| **App Framework** | Streamlit |
| **Model Saving** | pickle |
| **Version Control** | Git, GitHub |
| **Deployment** | Streamlit Cloud |

---

## 📂 Repository Structure
Gurgaon-RealEstate-ML-Project/</br>
│</br>
├── Datasets/          # processed data</br>
├── Notebooks/         # Jupyter notebooks (EDA, Preprocessing, Modeling)</br>
├── model/             # Trained ML models (.pkl files)</br>
├── pages/             # Streamlit multipage components</br>
│</br>
├── Home.py            # Main Streamlit app entry point</br>
├── requirements.txt   # Dependencies</br>
├── README.md          # Documentation</br>
├── .gitignore         # Ignored files</br>
└── .gitattributes     # LFS tracking for large model files</br>

---

## ⚙️ Installation & Usage

```bash
# 1️⃣ Clone the repository
git clone https://github.com/shubh-nih/Gurgaon-RealEstate-ML-Project.git
```
```bash
# 2️⃣ Navigate to the folder
cd Gurgaon-RealEstate-ML-Project
```
```bash
# 3️⃣ Install dependencies
pip install -r requirements.txt
```
```bash
# 4️⃣ Run the Streamlit app
streamlit run Home.py
```

--- 

## 📷 Screenshots

> #### 🏠 Prediction Page 
 <img width="960" height="475" alt="image" src="https://github.com/user-attachments/assets/b529d90b-ca56-40bc-ba27-3218c8595b29" />

> #### 📊 Analysis Page
<img width="960" height="473" alt="image" src="https://github.com/user-attachments/assets/fe193463-8223-4e33-9608-9ae4f4bb126e" />

> #### 💡 Recommender Page 
<img width="960" height="473" alt="image" src="https://github.com/user-attachments/assets/ba1b4f0e-66a1-4bef-8ceb-5f097c0d2678" />

---
⚠️ License & Usage

This project and its code, developed for educational, academic, and portfolio purposes.

> 🛑 Unauthorized copying, reuse, or redistribution of any code, dataset, or model is strictly prohibited.
> Please do not fork, clone, or modify this repository without explicit written permission.




