import random

import streamlit as st

st.set_page_config(page_title="Selityskone", page_icon="🧾", layout="wide")

EXCUSE_POOL = [
    "Olin oikeasti hyvässä vireessä, mutta kohtalo teki yllätysliikkeen juuri ratkaisevalla hetkellä.",
    "Valmentajan katse osui minuun vinosti, ja siitä meni koko rytmi sekaisin.",
    "En hävinnyt, universumi vain testasi nöyryyttäni poikkeuksellisen näkyvästi.",
    "Aamukahvi oli liian vahvaa, joten olin 0,7 sekuntia liian aggressiivinen jokaisessa ratkaisussa.",
    "Vastustaja käytti epäreilua taktiikkaa: hän onnistui paremmin kuin minä.",
    "Sukissa oli väärä energiatila, enkä saanut niistä kisamoodia päälle.",
    "Yleisö taputti eri tahtiin kuin sydämeni, ja synkka petti täysin.",
    "Tuomari ei huomioinut henkistä ylivoimaani lainkaan tulosta laskiessaan.",
    "Harjoittelin tätä varten liikaa, ja siitä tuli suorituspäivänä liian valmis.",
    "Minulla oli voittajan asenne, mutta se jäi hetkeksi pukuhuoneeseen.",
    "Teknisesti kaikki meni suunnitelman mukaan, suunnitelma oli vain huono.",
    "Olin tänään enemmän taiteellinen kuin tuloshakuinen.",
]

SPORTS = [
    "jääkiekossa",
    "hiihdossa",
    "jalkapallossa",
    "runonlausunnassa",
    "Euroviisuissa",
    "mäkihypyssä",
    "missä tahansa",
]


st.markdown(
    """
    <style>
    .character-card {
        background: linear-gradient(135deg, #0f172a, #1e3a8a 65%, #1d4ed8);
        border-radius: 20px;
        padding: 1.2rem;
        color: #f8fafc;
        min-height: 320px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 35px rgba(15, 23, 42, 0.35);
    }
    .character {
        font-size: 7rem;
        text-align: center;
        animation: sway 2.5s ease-in-out infinite;
        filter: drop-shadow(0 8px 6px rgba(2, 6, 23, 0.35));
    }
    .speech {
        background: rgba(255, 255, 255, 0.12);
        border: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 12px;
        padding: 0.8rem;
        font-size: 1rem;
        line-height: 1.35;
    }
    .small-note {
        opacity: 0.8;
        font-size: 0.88rem;
    }
    @keyframes sway {
        0% {transform: translateY(0px) rotate(-2deg);} 
        50% {transform: translateY(-9px) rotate(2deg);} 
        100% {transform: translateY(0px) rotate(-2deg);} 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🇫🇮 Selityskone: miksi hävisit?")
st.write("Valitse laji tai tilanne, paina nappia ja kuuntele erittäin heikkotasoista mutta itsevarmaa selitystä.")

left_col, right_col = st.columns([1.2, 1])

with right_col:
    selected_sport = st.selectbox("Miksi hävisit...", SPORTS)
    if st.button("Generoi surkea selitys", type="primary", use_container_width=True):
        selected_excuse = random.choice(EXCUSE_POOL)
        st.session_state["current_excuse"] = (
            f"No siis, hävisin {selected_sport}, koska {selected_excuse}"
        )

    st.caption(
        "Voit myöhemmin korvata selitykset omalla liitteelläsi. Rakensin nyt väliaikaisen satunnaislistan."
    )

current_excuse = st.session_state.get(
    "current_excuse",
    "No siis, hävisin missä tahansa, koska tänään tähdet muodostivat vastustajalle taktisen etumatkan.",
)

with left_col:
    st.markdown(
        f"""
        <div class="character-card">
            <div class="character">🕺</div>
            <div class="speech">{current_excuse}</div>
            <p class="small-note">Animoitu suomalainen selittäjä on aina valmis kertomaan, miksi tappio ei ollut hänen vikansa.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
