import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
AGRIDATA x BuscoCampo
"""
st.sidebar.title("Sobre nosotros")
st.sidebar.info(markdown)


# Customize page title
st.title("AgriData reportes")

st.markdown(
    """
    
    """
)

st.header("")

markdown = """


"""

st.markdown(markdown)
