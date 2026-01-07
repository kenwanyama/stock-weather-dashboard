import streamlit as st

def apply_paper_theme():
    st.markdown(
        """
        <style>
        /* -----------------------------
           Global App Styling
        ----------------------------- */

        html, body, [class*="css"] {
            font-family: Georgia, "Times New Roman", serif;
            background-color: #fdfcf9;
            color: #111;
        }

        /* Main content container */
        .main {
            background-color: #fdfcf9;
            padding-left: 3rem;
            padding-right: 3rem;
        }

        /* Headings */
        h1, h2, h3 {
            font-family: Georgia, "Times New Roman", serif;
            color: #111;
            letter-spacing: -0.5px;
        }

        h1 {
            text-align: center;
            font-size: 3rem;
            border-bottom: 2px solid #111;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }

        h2 {
            font-size: 1.8rem;
            margin-top: 2.5rem;
            border-bottom: 1px solid #999;
            padding-bottom: 0.3rem;
        }

        h3 {
            font-size: 1.4rem;
            margin-top: 1.5rem;
        }

        /* Paragraph text */
        p {
            font-size: 1.05rem;
            line-height: 1.7;
            color: #222;
        }

        /* Links */
        a {
            color: #111 !important;
            font-weight: 600;
            text-decoration: underline;
        }

        a:hover {
            color: #000 !important;
            text-decoration: none;
        }

        /* Divider */
        hr {
            border-top: 1px solid #aaa;
            margin: 2rem 0;
        }

        /* Dataframe styling */
        .stDataFrame {
            border: 1px solid #ccc;
        }

        /* -----------------------------
           Sidebar Styling
        ----------------------------- */

        section[data-testid="stSidebar"] {
            background-color: #f5f2eb;
            border-right: 1px solid #ccc;
            padding-top: 1rem;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            font-family: Georgia, "Times New Roman", serif;
            color: #111;
        }

        section[data-testid="stSidebar"] a {
            color: #111 !important;
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 600;
            text-decoration: none;
        }

        section[data-testid="stSidebar"] a:hover {
            color: #000 !important;
            text-decoration: underline;
        }

        /* Remove Streamlit footer */
        footer {
            visibility: hidden;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

