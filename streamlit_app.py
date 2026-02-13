import random

import streamlit as st

st.set_page_config(page_title="Selityskone", page_icon="🧾", layout="wide")

EXCUSE_POOL = [
    "Sukset oli väärää mallia tälle kelille",
    "Ladut oli liian pehmeät",
    "Ladut oli liian kovat",
    "Pito petti just ratkaisuhetkellä",
    "Luisto katosi täysin tokalla kierroksella",
    "Voitelu meni ihan pieleen",
    "Voitelukopissa tuli kiire",
    "Testisuksi jäi kotiin",
    "Suksiin tuli kivi pohjaan",
    "Sauva katkesi väärällä hetkellä",
    "Hiihtolasit huurtui heti alussa",
    "Aurinko paistoi silmiin koko ajan",
    "Tuuli kääntyi just meidän kohdalla",
    "Vastatuulta oli aina kun minä hiihdin",
    "Reitti oli liian mäkinen mun tyylille",
    "Reitti oli liian tasainen mun tyylille",
    "Startissa joku töni ja rytmi meni",
    "Edessä kaatui ja jouduin väistämään",
    "Ohituspaikat oli liian kapeat",
    "Tuomari ei nähnyt sitä rikettä",
    "Ajanotto oli varmasti väärässä",
    "Numerolappu hankasi ja keskittyminen meni",
    "Kenkä painoi varpaita",
    "Monossa oli rakko valmiiksi",
    "Sukat oli väärää materiaalia",
    "Kisapäivänä oli väärä aamupala",
    "Kahvi jäi juomatta, siitä se johtui",
    "Join liikaa kahvia, kädet tärisi",
    "Nesteytys epäonnistui täysin",
    "Vatsa meni sekaisin huoltoasemalta",
    "Yöllä nukuin vain neljä tuntia",
    "Naapuri porasi seinää yöllä",
    "Jännitys vei jalat alta",
    "En saanut hyvää alkulämmittelyä",
    "Alkulämmittely meni yli, tuli hapoille",
    "Lähtö meni vähän liian kovaa, maksoi lopussa",
    "Lähtö meni liian hiljaa, ei saanut kiinni porukkaa",
    "Tänään ei vaan ollut kroppa hereillä",
    "Kroppa oli liian hereillä, meni ylikierroksille",
    "Flunssa oli tulossa, tunsin sen jo aamulla",
    "Allergia iski just nyt, ei voi mitään",
    "Ilmankosteus oli outo",
    "Ilmanpaine laski, sen kyllä huomaa",
    "Sää oli liian suomalainen",
    "Sää oli liian epäsuomalainen",
    "En ollut tottunut tähän aikatauluun",
    "Matkustus väsytti, vaikka oli vain tunti",
    "Bussi oli myöhässä ja tuli kiire",
    "Parkkipaikka oli liian kaukana",
    "Varusteet oli lainassa ja väärän kokoiset",
    "Uudet varusteet ei ole vielä sisäänajettu",
    "Vanhat varusteet on loppuun ajetut",
    "Tuomari oli selvästi toista puolta",
    "Kilpailu oli liian kovatasoinen tänään",
    "Muut oli varmasti dopingilla",
    "Reitti oli merkitty epäselvästi",
    "Kartta oli painettu väärin",
    "Kompassi näytti omiaan",
    "Kello lagasi ja splitit meni sekaisin",
    "Puhelin piippasi kesken suorituksen",
    "Kuulutukset häiritsi keskittymistä",
    "Yleisö oli liian hiljaa, ei tullut fiilistä",
    "Yleisö oli liian äänekäs, meni pasmat sekaisin",
    "Musiikki oli väärä, ei sytyttänyt",
    "Kaiutin särisi, hermo meni",
    "Käsi kramppasi yllättäen",
    "Säärissä oli painoa eilisestä",
    "Eilen oli saunailta, palautuminen jäi vajaaksi",
    "Työpäivä venyi, ei ehtinyt valmistautua",
    "Valmentaja käski väärää taktiikkaa",
    "Taktiikka oli hyvä, mutta en toteuttanut",
    "En saanut peesiä, jouduin tekemään yksin",
    "Jouduin vetämään letkaa liian kauan",
    "Kengännauha aukesi ja piti säätää",
    "Teippi petti ja kaikki levisi",
    "Pyyhe jäi pukuhuoneeseen, siitä se lähti",
    "Lämmittelyalue oli liian ahdas",
    "Rata oli liian liukas",
    "Rata oli liian pitävä",
    "Kenttä oli kuoppainen",
    "Kenttä oli liian hyvä, ei sopinut mun pelille",
    "Pallo oli liian kova",
    "Pallo oli liian pehmeä",
    "Pallo oli eri merkkiä kuin treeneissä",
    "Valo-olosuhteet oli hankalat",
    "Varjo osui just ratkaisuhetkellä",
    "Katsomosta joku huusi ja häiritsi",
    "Tuoksui grillimakkara, tuli nälkä",
    "En löytänyt oikeaa vaihdetta ollenkaan",
    "Vaihteet jäi päälle, meni reisille",
    "Tämä oli selvästi harjoituskisa",
    "En ollut vielä kauden huipussa",
    "Huippukunto meni jo viime viikolla",
    "Kisa oli liian aikaisin keväällä",
    "Kisa oli liian myöhään syksyllä",
    "En ehtinyt tehdä kunnon herkistelyä",
    "Herkkistely meni yli, jalat tyhjeni",
    "Olin väärässä sarjassa vahingossa",
    "Säännöt oli epäselvät ja tulkinta vaihteli",
    "Tuomarit ei ymmärtäneet lajia",
    "Huolto ei toiminut, geeli jäi saamatta",
    "Geeli meni väärään taskuun, en löytänyt",
    "Juomapisteellä oli ruuhkaa",
    "Toiset oikoi, mutta ei ketään kiinnosta",
    "Mulla on parempi suoritus treeneissä, uskokaa pois",
    "Tänään oli henkisesti raskas päivä, siinä se",
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
        "Tässä selityksiä"
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
