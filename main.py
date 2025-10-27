import streamlit as st

st.set_page_config(
    page_title="Student Survey"
)

visualise = st.Page('home1.py', title='Pencapaian Akademik Pelajar', icon=":material/school:")

home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

home = st.Page('page1.py', title='Page 1', default=True, icon=":material/home:")

home = st.Page('page2.py', title='Page 2', default=True, icon=":material/home:")

home = st.Page('page3.py', title='Page 3', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise]
        }
    )

pg.run()
