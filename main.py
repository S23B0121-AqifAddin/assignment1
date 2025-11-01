import streamlit as st

st.set_page_config(page_title="Bangladesh Motorbike Accident")

# Define each page
page_1 = st.Page("page1.py", title="Page 1")
page_2 = st.Page("page2.py", title="Page 2")
page_3 = st.Page("page3.py", title="Page 3")

# Create navigation menu
pg = st.navigation(
    {
        "Menu": [page_1, page_2, page_3]
    }
)

pg.run()
