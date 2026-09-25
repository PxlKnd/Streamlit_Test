import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

# Erste Seite bauen
st.set_page_config(page_title="Meine erste Streamlit App", layout="wide")

st.write("Wir bauen unsere erste Streamlit App mit Streamlit.")
st.title("Das ist die Überschrift.")
st.title("This is the app title")  # groesste Ueberschrift (Seitentitel)
st.header("This *is* the **header**")  # Abschnitts-Ueberschrift
st.markdown(
    "This is the markdown", text_alignment="center", width="content"
)  # Text mit Markdown-Formatierung (**fett**, *kursiv*, ...)
st.subheader("This is the subheader")  # kleinere Unter-Ueberschrift
st.caption("This is the caption")  # kleiner, grauer Hinweistext
st.code("x = 2021")  # Code-Block mit Syntax-Hervorhebung
st.latex(r""" a+a r^1+a r^2+a r^3 """)  # mathematische Formel (LaTeX)

st.checkbox("Yes")  # Haekchen (True/False)
st.button("Click Me")  # Schaltflaeche (True beim Klick)
st.radio("Pick your gender", ["Male", "Female"])  # Auswahl EINER Option (Radiobuttons)
st.selectbox(
    "Pick a fruit", ["Apple", "Banana", "Orange"]
)  # Dropdown-Auswahl (eine Option)
st.multiselect("Choose a planet", ["Jupiter", "Mars", "Neptune"])  # Mehrfachauswahl
st.select_slider(
    "Pick a mark", ["Bad", "Good", "Excellent"]
)  # Schieberegler ueber Text-Werte
st.slider("Pick a number", 0, 50)  # Zahlen-Schieberegler (min, max)

st.number_input("Pick a number", 0, 10)  # Zahlen-Eingabefeld (mit +/- Buttons)
st.text_input("Email address")  # einzeiliges Text-Eingabefeld
st.date_input("Traveling date")  # Datums-Auswahl (Kalender)
st.time_input("School time")  # Uhrzeit-Auswahl
st.text_area("Description")  # mehrzeiliges Textfeld
st.file_uploader("Upload a photo")  # Datei-Upload
st.color_picker("Choose your favorite color")  # Farbauswahl

st.progress(value=0.33, text="Fortschritt Copy to Dev NULL ;)")
# with st.spinner("Warten sie noch etwas"):
#    time.sleep(5)
st.success("Done!")
st.success("You did it!")  # gruen: Erfolg
st.error("Error occurred")  # rot: Fehler
st.warning("This is a warning")  # gelb: Warnung
st.info("It's easy to build a Streamlit app")  # blau: Info-Hinweis
st.exception(
    RuntimeError("RuntimeError exception")
)  # zeigt eine Exception formatiert an


st.sidebar.title("My sidebar title")
st.sidebar.markdown("*Das ist ein MD Test*")
st.sidebar.progress(value=20, text="Coole Aktion")

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.line_chart(df)  # Liniendiagramm

df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.bar_chart(df)  # Balkendiagramm

df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.area_chart(df)  # Flaechendiagramm

# --- Altair-Diagramm (interaktiv, anpassbar) ----------------
# Altair ist deklarativ: man beschreibt, welche Spalte auf welche
# "Encoding" (x, y, Groesse, Farbe, Tooltip) abgebildet wird.
df = pd.DataFrame(np.random.randn(500, 3), columns=["x", "y", "z"])
chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="x", y="y", size="z", color="z", tooltip=["x", "y", "z"])
)
st.altair_chart(chart, use_container_width=True)  # nutzt die volle Breite

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(df)
