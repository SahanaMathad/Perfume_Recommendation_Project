# 🌸Perfume_Recommendation_Project


A two-part project that lets you:

1. **Train & evaluate** an XGBoost classifier on perfume descriptions (Jupyter Notebook).  
2. **Interactively explore** and get content-based perfume recommendations via a Streamlit app.

---

## 📁 Repository Structure

```
├── app.py
├── perfume_xgboost.ipynb
├── final_perfume_data.csv
├── vectorizer.pkl
├── cosine_sim.pkl
├── perfumes.pkl
├── environment.yml
├── requirements.txt
├── screenshots/
│   ├── home.png
│   └── recommendations.png
└── README.md
```

- **`perfume_xgboost.ipynb`**  
  Jupyter Notebook that:
  - Loads `final_perfume_data.csv`
  - Preprocesses & vectorizes perfume descriptions using TF-IDF
  - Trains an XGBoost classifier
  - Evaluates with accuracy, classification report & confusion matrix
  - Generates word clouds of key fragrance notes
  - Saves trained artifacts with `joblib` (e.g., `classifier.pkl`)

- **`app.py`**  
  A Streamlit application for content-based recommendations:
  - Loads precomputed `perfumes.pkl`, `vectorizer.pkl` & `cosine_sim.pkl`
  - Lets users select or randomly pick perfumes
  - Computes cosine similarity over TF-IDF vectors
  - Displays top-9 recommendations with images, brand, and ingredients

- **`environment.yml`**  
  Conda environment file listing all dependencies and exact versions.

- **`requirements.txt`**  
  Pip requirements file with exact package versions for environments without Conda.

- **`screenshots/`**  
  Directory containing interface screenshots for this README.

---

## 🛠️ Installation

### 1. Conda Environment (Recommended)

```bash
# Create the environment from environment.yml
conda env create -f environment.yml

# Activate it
conda activate perfume-recommender
```

### 2. Pip Environment

```bash
# Create & activate a virtualenv
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate.bat   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### Train & Evaluate (Notebook)

1. Launch the notebook:  
   ```bash
   jupyter notebook perfume_xgboost.ipynb
   ```
2. Run cells to preprocess data, train the model, and view evaluation plots.
3. Model artifacts (e.g., `classifier.pkl`) will be saved automatically.

### Run the Streamlit App

1. Ensure you have:
   - `perfumes.pkl`
   - `vectorizer.pkl`
   - `cosine_sim.pkl`

2. Start the app:  
   ```bash
   streamlit run app.py
   ```
3. In your browser sidebar, select perfumes or click **Random 5** for recommendations.

---

## 🎨 UI Screenshots

Below are example screenshots of the Streamlit interface. Place your images in the `screenshots/` folder:

### Home Page View

![alt text](01-1.PNG)

### Recommendations View

![Recommendations Screen](screenshots/recommendations.png)

---


