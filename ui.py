import streamlit as st

st.set_page_config(page_title="Nieliniowe UI", page_icon="🌀", layout="centered")

st.title("Wybierz przestrzeń wejścia")

options = {
    "👪 CEL": "cel",
    "🔮 META": "meta",
    "🦋 sensory": "sensory",
    "⭐ sukces": "sukces"
}

choice = st.selectbox(
    " ",
    list(options.keys()),
    index=None,
    placeholder="Kliknij ikonę…"
)

if choice:
    st.markdown(f"### Wybrałaś: {choice}")

    st.divider()
    st.header("Wybierz sposób pracy")

    mode = st.radio(
        " ",
        ["DEMO", "META", "META-ASYNC"],
        horizontal=True
    )

    st.divider()

    if st.button("START", type="primary"):
        st.success(f"Uruchamiam tryb **{mode}** w przestrzeni **{choice}**…")
        # tu później podłączymy backend:
        # run(mode=mode.lower(), space=options[choice])
