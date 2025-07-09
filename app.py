# import streamlit as st
# import pandas as pd
# import pickle
# import random
#
# # ─── Page Config ───────────────────────────
# st.set_page_config(
#     page_title="Perfume Recommender",
#     page_icon="🌸",
#     layout="wide"
# )
#
# # ─── Custom CSS Styling ─────────────────────
# st.markdown("""
# <style>
# /* 1. Gradient background */
# body, .stApp, .reportview-container, .block-container, .main {
#     background: linear-gradient(135deg, #ffb6b9, #fdfd96, #f6abb6, #e0c3fc);
#     background-size: 400% 400%;
#     animation: gradientBG 15s ease infinite;
#     color: #3d2a4f !important;
#     font-family: 'Segoe UI', sans-serif;
# }
#
# /* Animate gradient flow */
# @keyframes gradientBG {
#     0% { background-position: 0% 50%; }
#     50% { background-position: 100% 50%; }
#     100% { background-position: 0% 50%; }
# }
#
# /* 2. Sidebar */
# [data-testid="stSidebar"] {
#     background: linear-gradient(135deg, #f6abb6, #e0c3fc);
#     color: #3d2a4f !important;
# }
# [data-testid="stSidebar"] * {
#     color: #3d2a4f !important;
# }
#
# /* 3. Dropdowns */
# div[data-baseweb="select"] {
#     background-color: #ffe4ec !important;
#     border-radius: 10px;
# }
# div[data-baseweb="select"] * {
#     color: #3d2a4f !important;
# }
# div[data-baseweb="menu"] {
#     background-color: #ffe4ec !important;
#     color: #3d2a4f !important;
# }
#
# /* 4. Buttons */
# .stButton > button {
#     background-color: #ffb6b9 !important;
#     color: white !important;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 8px 20px;
#     box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
#     transition: background 0.3s ease-in-out;
# }
# .stButton > button:hover {
#     background-color: #e38cae !important;
# }
#
# /* 5. Cards */
# .card {
#     background-color: rgba(255, 255, 255, 0.9);
#     border-radius: 15px;
#     box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
#     padding: 20px;
#     margin: 10px;
#     text-align: center;
#     color: #3d2a4f;
# }
# .card img {
#     border-radius: 12px;
#     height: 180px;
#     object-fit: cover;
#     margin-bottom: 10px;
# }
# .card h4 {
#     margin: 5px 0;
#     font-size: 17px;
#     color: #4b2e63;
# }
# .card p {
#     font-size: 14px;
#     color: #59406f;
# }
#
# /* 6. Layout adjustment for wider grid */
# .css-18e3th9 {
#     padding-left: 4rem !important;
#     padding-right: 4rem !important;
# }
# </style>
# """, unsafe_allow_html=True)
#
# # ─── Load Data and Models ───────────────────
# @st.cache_data
# def load_data():
#     return pd.read_pickle("perfumes.pkl")
#
# @st.cache_resource
# def load_models():
#     with open("vectorizer.pkl", "rb") as f:
#         vectorizer = pickle.load(f)
#     with open("cosine_sim.pkl", "rb") as f:
#         cosine_sim = pickle.load(f)
#     return vectorizer, cosine_sim
#
# perfumes = load_data()
# _, cosine_sim = load_models()
#
# # ─── Recommendation Logic ───────────────────
# def recommend_perfumes(selected_names, n=9):
#     idxs = perfumes[perfumes['Name'].isin(selected_names)].index
#     sim_scores = cosine_sim[idxs].mean(axis=0)
#     ranked = sim_scores.argsort()[::-1]
#     rec_idxs = [i for i in ranked if i not in idxs][:n]
#     return perfumes.iloc[rec_idxs][['Name','Brand','Ingredients','Image URL']]
#
# # ─── Sidebar ────────────────────────────────
# st.sidebar.header("🎀 Your Perfume Picks")
# perfume_list = perfumes['Name'].tolist()
# selected = st.sidebar.multiselect("Select one or more perfumes", perfume_list)
#
# if st.sidebar.button("🎲 Random 5"):
#     selected = random.sample(perfume_list, 5)
#     st.sidebar.success("Random perfumes selected!")
#
# # ─── Main Area ──────────────────────────────
# st.markdown("<h1 style='text-align: center;'>🌸 Perfume Recommendation System</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center;'>Choose your favorite scents and get personalized recommendations 🌷</p>", unsafe_allow_html=True)
# st.markdown("---")
#
# if selected:
#     recs = recommend_perfumes(selected)
#     st.subheader("✨ Recommended for You")
#
#     cols = st.columns(3, gap="medium")  # Slightly wider grid
#     for i, (_, row) in enumerate(recs.iterrows()):
#         with cols[i % 3]:
#             st.markdown(f"""
#                 <div class="card">
#                     <img src="{row['Image URL']}" alt="{row['Name']}"/>
#                     <h4>{row['Name']}</h4>
#                     <p><strong>{row['Brand']}</strong></p>
#                     <p>{row['Ingredients']}</p>
#                 </div>
#             """, unsafe_allow_html=True)
# else:
#     st.info("Select at least one perfume from the sidebar to get recommendations.")
#
# # ─── Expand to See Dataset ───────────────────
# with st.expander("📋 View All Perfume Data"):
#     st.dataframe(perfumes[['Name', 'Brand', 'Ingredients']])
import streamlit as st
import pandas as pd
import pickle
import random

# ─── Page Config ───────────────────────────
st.set_page_config(
    page_title="Perfume Recommender",
    page_icon="🌸",
    layout="wide"
)

# ─── Custom CSS Styling ─────────────────────
st.markdown("""
<style>
body, .stApp, .reportview-container, .block-container, .main {
    background: linear-gradient(135deg, #ffb6b9, #fdfd96, #f6abb6, #e0c3fc);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: #3d2a4f !important;
    font-family: 'Segoe UI', sans-serif;
}
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #f6abb6, #e0c3fc);
    color: #3d2a4f !important;
}
[data-testid="stSidebar"] * {
    color: #3d2a4f !important;
}
div[data-baseweb="select"] {
    background-color: #ffe4ec !important;
    border-radius: 10px;
}
div[data-baseweb="select"] * {
    color: #3d2a4f !important;
}
div[data-baseweb="menu"] {
    background-color: #ffe4ec !important;
    color: #3d2a4f !important;
}
.stButton > button {
    background-color: #ffb6b9 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 10px;
    padding: 8px 20px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
    transition: background 0.3s ease-in-out;
}
.stButton > button:hover {
    background-color: #e38cae !important;
}
.card {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
    padding: 20px;
    margin: 10px;
    text-align: center;
    color: #3d2a4f;
}
.card img {
    border-radius: 12px;
    height: 180px;
    object-fit: cover;
    margin-bottom: 10px;
}
.card h4 {
    margin: 5px 0;
    font-size: 17px;
    color: #4b2e63;
}
.card p {
    font-size: 14px;
    color: #59406f;
}
.css-18e3th9 {
    padding-left: 4rem !important;
    padding-right: 4rem !important;
}

.notes-button-wrapper button {
    width: 130px !important;
    height: 42px !important;
    font-size: 14px !important;
    font-weight: 600;
    border-radius: 10px !important;
    background-color: #d17ba1 !important;
    color: #ffffff !important;
    margin: 6px;
    box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
    transition: background 0.3s ease;
}
.notes-button-wrapper button:hover {
    background-color: #b34e80 !important;
    color: #fff !important;
}

</style>
""", unsafe_allow_html=True)

# ─── Load Data and Models ───────────────────
@st.cache_data
def load_data():
    return pd.read_pickle("perfumes.pkl")

@st.cache_resource
def load_models():
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("cosine_sim.pkl", "rb") as f:
        cosine_sim = pickle.load(f)
    return vectorizer, cosine_sim

perfumes = load_data()
_, cosine_sim = load_models()

# ─── Recommendation Logic ───────────────────
def recommend_perfumes(selected_names, n=9):
    idxs = perfumes[perfumes['Name'].isin(selected_names)].index
    sim_scores = cosine_sim[idxs].mean(axis=0)
    ranked = sim_scores.argsort()[::-1]
    rec_idxs = [i for i in ranked if i not in idxs][:n]
    return perfumes.iloc[rec_idxs][['Name', 'Brand', 'Ingredients', 'Image URL']]

# ─── Sidebar ────────────────────────────────
st.sidebar.header("🎀 Your Perfume Picks")
perfume_list = perfumes['Name'].tolist()
selected = st.sidebar.multiselect("Select one or more perfumes", perfume_list)

if st.sidebar.button("🎲 Random 5"):
    selected = random.sample(perfume_list, 5)
    st.sidebar.success("Random perfumes selected!")

# ─── Main Area ──────────────────────────────
st.markdown("<h1 style='text-align: center;'>🌸 Perfume Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose your favorite scents and get personalized recommendations 🌷</p>", unsafe_allow_html=True)
st.markdown("---")

if selected:
    recs = recommend_perfumes(selected)
    st.subheader("✨ Recommended for You")
    cols = st.columns(3, gap="medium")
    for i, (_, row) in enumerate(recs.iterrows()):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="card">
                    <img src="{row['Image URL']}" alt="{row['Name']}"/>
                    <h4>{row['Name']}</h4>
                    <p><strong>{row['Brand']}</strong></p>
                    <p>{row['Ingredients']}</p>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("Select at least one perfume from the sidebar to get recommendations.")

# ─── Filter by Notes ────────────────────────
st.markdown("---")
st.subheader("🌺 Explore by Notes")

common_notes = ['Vanilla', 'Floral', 'Musk', 'Woody', 'Citrus', 'Rose', 'Spicy', 'Fruity', 'Amber', 'Leather', 'Green']

clicked_note = None
st.markdown('<div class="notes-button-wrapper">', unsafe_allow_html=True)

# Display 4 buttons per row for better spacing
buttons_per_row = 4
for i in range(0, len(common_notes), buttons_per_row):
    row_notes = common_notes[i:i + buttons_per_row]
    cols = st.columns(buttons_per_row)
    for col, note in zip(cols, row_notes):
        with col:
            if st.button(note, key=f"note-{note}"):
                clicked_note = note

st.markdown('</div>', unsafe_allow_html=True)

# Display perfumes with selected note
if clicked_note:
    st.markdown(f"### 🌼 Perfumes with **{clicked_note}** notes:")
    filtered = perfumes[perfumes['Ingredients'].str.contains(clicked_note, case=False, na=False)]
    if filtered.empty:
        st.warning("No perfumes found with that note.")
    else:
        cols = st.columns(3, gap="medium")
        for i, (_, row) in enumerate(filtered.iterrows()):
            with cols[i % 3]:
                st.markdown(f"""
                    <div class="card">
                        <img src="{row['Image URL']}" alt="{row['Name']}"/>
                        <h4>{row['Name']}</h4>
                        <p><strong>{row['Brand']}</strong></p>
                        <p>{row['Ingredients']}</p>
                    </div>
                """, unsafe_allow_html=True)

# ─── Expand to See Dataset ───────────────────
with st.expander("📋 View All Perfume Data"):
    st.dataframe(perfumes[['Name', 'Brand', 'Ingredients']])
