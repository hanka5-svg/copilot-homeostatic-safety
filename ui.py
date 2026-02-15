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

 # --- NAWIGACJA MIĘDZY EKRANAMI ---
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    # EKRAN STARTOWY
    if st.button("START", type="primary"):
        st.session_state.started = True
        st.rerun()
else:
    # EKRAN PO START
    st.success(f"Tryb **{mode}** w przestrzeni **{choice}** został uruchomiony.")
    st.header("To jest nowy ekran ✨")
    st.write("Tu możesz dodać logikę, moduły, backend, cokolwiek chcesz.")

        # tu później podłączymy backend:
        # run(mode=mode.lower(), space=options[choice])
