import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# col1, col2 = st.columns(2)

def main():
    col1, col2, col3 = st.columns(3)

    for _ in range(15):
        col1.write("")
        col3.write("")
    col1.metric(label="**Szanse na zatrudnienie**", value="125%", delta="75%")
    col3.metric(label="**Sobotni czas wolny**", value="16h", delta="-8h")

    style_metric_cards(background_color=False, border_left_color=False, border_color=False, box_shadow=False)

main()