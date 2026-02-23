import random
import time
import streamlit as st

# matplotlib est optionnel : si absent, l'app marche sans images
try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle
    HAS_MPL = True
except Exception:
    HAS_MPL = False

# ---------- CONFIG (UNE SEULE FOIS) ----------
st.set_page_config(page_title="Kangourou 6e — Agent IA", page_icon="🦘", layout="centered")

LABELS = ["A", "B", "C", "D", "E"]
SERIE_LEN = 10
DURATION_SEC = 20 * 60
BANK_SIZE = 50

# ---------- HELPERS ----------
def make_mcq(correct: str, wrongs: list[str], n: int = 5):
    pool = [w for w in wrongs if w != correct]
    pool = list(dict.fromkeys(pool))
    while len(pool) < n - 1:
        pool.append(random.choice(wrongs))
        pool = list(dict.fromkeys(pool))
        if len(pool) > 200:
            break
    choices = [correct] + random.sample(pool, n - 1)
    random.shuffle(choices)
    return choices, choices.index(correct)

def fig_base():
    if not HAS_MPL:
        return None, None
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax

# ---------- EXERCICES ----------
def ex_div_by_3():
    def make_div3():
        x = random.randint(100, 999)
        s = sum(map(int, str(x)))
        return x if s % 3 == 0 else x + ((3 - (s % 3)) % 3)

    correct = make_div3()
    options = {correct}
    while len(options) < 5:
        x = random.randint(100, 999)
        if sum(map(int, str(x))) % 3 != 0:
            options.add(x)

    choices_nums = list(options)
    random.shuffle(choices_nums)
    choices = [str(x) for x in choices_nums]
    ans = choices_nums.index(correct)
    explanation = f"Divisible par 3 ⇔ somme des chiffres multiple de 3. Pour {correct} : somme = {sum(map(int, str(correct)))}."
    return {"topic": "Divisibilité", "question": "Quel nombre est divisible par 3 ?", "choices": choices, "answer_index": ans, "explanation": explanation}

def ex_fraction_bar_model():
    denom = random.choice([6, 8, 10, 12, 14])
    num = random.randint(1, denom - 1)
    correct = f"{num}/{denom}"
    wrongs = [
        f"{denom}/{num}",
        "1/2", "2/3", "3/4", "1",
        f"{max(1, num-1)}/{denom}",
        f"{min(denom-1, num+1)}/{denom}",
    ]
    choices, ans = make_mcq(correct, wrongs, 5)

    def draw(ax):
        ax.add_patch(Rectangle((0, 0), denom, 1, fill=False, linewidth=2))
        for i in range(1, denom):
            ax.plot([i, i], [0, 1], linewidth=1)
        ax.add_patch(Rectangle((0, 0), num, 1, facecolor="lightgray", edgecolor="none"))
        ax.set_xlim(-0.5, denom + 0.5)
        ax.set_ylim(-0.8, 1.8)
        ax.text(0, 1.25, "Partie coloriée :", fontsize=11)
        ax.text(0, -0.45, f"{num} parts sur {denom}", fontsize=11)

    explanation = f"La barre a {denom} parts égales, {num} sont coloriées ⇒ {num}/{denom}."
    ex = {"topic": "Fractions", "question": "Quelle fraction de la barre est coloriée ?", "choices": choices, "answer_index": ans, "explanation": explanation}
    if HAS_MPL:
        ex["draw"] = draw
    return ex

def ex_triangle_angle_with_extension():
    a = random.randint(30, 85)
    b = random.randint(20, 75)
    while a + b >= 170:
        b = random.randint(20, 75)
    c = 180 - (a + b)
    ext = a + b
    correct_s = f"{ext}°"
    wrongs = [f"{c}°", f"{180-a}°", f"{180-b}°", f"{a}°", f"{b}°", f"{ext+10}°"]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        P, Q, R = (0, 0), (4, 0), (1.2, 2.8)
        ax.add_patch(Polygon([P, Q, R], closed=True, fill=False, linewidth=2))
        ax.plot([4, 6], [0, 0], linewidth=2)
        ax.text(0.1, -0.35, f"{a}°", fontsize=12)
        ax.text(3.0, 0.25, f"{b}°", fontsize=12)
        ax.text(4.8, 0.25, "x°", fontsize=12)
        ax.set_xlim(-0.8, 6.4)
        ax.set_ylim(-1.0, 4.0)
        ax.set_title("Angle extérieur (x)", fontsize=11)

    explanation = f"Somme triangle = 180°. Angle intérieur sommet = 180°-({a}+{b})={c}°. Angle extérieur x = 180°-{c}={ext}°."
    ex = {"topic": "Angles", "question": f"Deux angles valent {a}° et {b}°. Mesure de l’angle extérieur x ?", "choices": choices, "answer_index": ans, "explanation": explanation}
    if HAS_MPL:
        ex["draw"] = draw
    return ex

EXERCISES = [ex_div_by_3, ex_fraction_bar_model, ex_triangle_angle_with_extension]

def new_exercise():
    ex = random.choice(EXERCISES)()
    ex["id"] = random.randint(100000, 999999)
    return ex

def make_bank(n=BANK_SIZE):
    return [new_exercise() for _ in range(n)]

# ---------- STATE INIT ----------
if "page" not in st.session_state:
    st.session_state.page = "🎮 Série"
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "question_idx" not in st.session_state:
    st.session_state.question_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "finished" not in st.session_state:
    st.session_state.finished = False
if "exercise" not in st.session_state:
    st.session_state.exercise = new_exercise()
if "bank" not in st.session_state:
    st.session_state.bank = make_bank(BANK_SIZE)
if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = None

def remaining_seconds():
    if not st.session_state.start_time:
        return DURATION_SEC
    return max(0, int(DURATION_SEC - (time.time() - st.session_state.start_time)))

def reset_series():
    st.session_state.game_started = False
    st.session_state.start_time = None
    st.session_state.question_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.finished = False
    st.session_state.last_feedback = None
    st.session_state.exercise = new_exercise()

# ---------- UI ----------
st.title("🦘 Kangourou 6e — Agent IA")

with st.sidebar:
    st.write("Navigation")
    page = st.radio("Menu", ["🎮 Série", "📚 Banque (50)", "🗂️ Annales"], index=0)
    st.write("Matplotlib:", "OK ✅" if HAS_MPL else "Non (pas d'images) ⚠️")

# ===== PAGE: SERIE =====
if page == "🎮 Série":
    st.subheader("Série (10 questions) — Chrono 20 min")
    r = remaining_seconds()
    c1, c2, c3 = st.columns(3)
    c1.metric("Progression", f"{min(st.session_state.question_idx, SERIE_LEN)}/{SERIE_LEN}")
    c2.metric("Score", str(st.session_state.score))
    c3.metric("Temps", f"{r//60:02d}:{r%60:02d}")
    st.divider()

    if not st.session_state.game_started:
        st.write("Clique **Démarrer** pour lancer la série.")
        if st.button("▶️ Démarrer"):
            reset_series()
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        if r <= 0 or st.session_state.question_idx >= SERIE_LEN:
            st.session_state.finished = True

        if st.session_state.finished:
            done = min(st.session_state.question_idx, SERIE_LEN)
            st.success(f"🏁 Terminé — Score : {st.session_state.score}/{done}")
            colA, colB = st.columns(2)
            with colA:
                if st.button("🔁 Rejouer"):
                    reset_series()
                    st.rerun()
            with colB:
                if st.button("🧹 Reset"):
                    reset_series()
                    st.rerun()
        else:
            ex = st.session_state.exercise
            st.write(f"### Question {st.session_state.question_idx + 1}")
            st.write(ex["question"])

            if HAS_MPL and "draw" in ex:
                fig, ax = fig_base()
                ex["draw"](ax)
                st.pyplot(fig, clear_figure=True)

            st.markdown("**Propositions :**")
            for i, choice in enumerate(ex["choices"]):
                st.write(f"- **{LABELS[i]}** : {choice}")

            st.write("**Répondre :**")
            cols = st.columns(5)
            for i in range(5):
                with cols[i]:
                    if st.button(LABELS[i], key=f"ans_{ex['id']}_{i}", disabled=st.session_state.answered, use_container_width=True):
                        st.session_state.answered = True
                        correct_i = ex["answer_index"]
                        if i == correct_i:
                            st.session_state.score += 1
                            st.session_state.last_feedback = ("ok", "✅ Bonne réponse")
                        else:
                            st.session_state.last_feedback = ("ko", f"❌ Faux (bonne réponse : {LABELS[correct_i]})")
                        st.rerun()

            if st.session_state.answered:
                kind, msg = st.session_state.last_feedback
                (st.success if kind == "ok" else st.error)(msg)

                correct_i = ex["answer_index"]
                st.info(f"Réponse : **{LABELS[correct_i]}** — {ex['choices'][correct_i]}")
                with st.expander("Correction", expanded=True):
                    st.write(ex["explanation"])

                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("➡️ Suivant"):
                        st.session_state.question_idx += 1
                        st.session_state.exercise = new_exercise()
                        st.session_state.answered = False
                        st.session_state.last_feedback = None
                        st.rerun()
                with col2:
                    if st.button("🔁 Refaire (sans compter)"):
                        st.session_state.answered = False
                        st.session_state.last_feedback = None
                        st.rerun()
                with col3:
                    if st.button("🧹 Reset série"):
                        reset_series()
                        st.rerun()

# ===== PAGE: BANQUE =====
elif page == "📚 Banque (50)":
    st.subheader("Banque (50) — exercices + corrigés")
    st.write("Banque générée une fois, puis figée (tu peux régénérer).")
    colA, colB = st.columns([1, 1])
    with colA:
        if st.button("🔄 Régénérer la banque"):
            st.session_state.bank = make_bank(BANK_SIZE)
            st.rerun()
    with colB:
        show_solutions = st.toggle("Afficher les corrigés", value=False)

    st.divider()

    topics = {}
    for ex in st.session_state.bank:
        topics.setdefault(ex.get("topic", "Autres"), []).append(ex)

    for topic, exos in topics.items():
        st.write(f"### 📌 {topic}")
        for idx, ex in enumerate(exos, start=1):
            title = ex["question"]
            if len(title) > 70:
                title = title[:70] + "…"
            with st.expander(f"Exercice {idx} — {title}"):
                st.write(ex["question"])
                if HAS_MPL and "draw" in ex:
                    fig, ax = fig_base()
                    ex["draw"](ax)
                    st.pyplot(fig, clear_figure=True)

                st.markdown("**Propositions :**")
                for i, choice in enumerate(ex["choices"]):
                    st.write(f"- **{LABELS[i]}** : {choice}")

                if show_solutions:
                    ci = ex["answer_index"]
                    st.success(f"✅ Réponse : {LABELS[ci]} — {ex['choices'][ci]}")
                    st.write(ex["explanation"])

# ===== PAGE: ANNALES =====
else:
    st.subheader("Annales officielles (liens)")
    st.write("Liens officiels ACL / Kangourou (mathkang.org). Pour 6e, viser en général le **Sujet B (6e–5e)**.")
    st.markdown("""
- 2025 : https://www.mathkang.org/concours/sujsol2025.html  
- 2024 : https://www.mathkang.org/concours/sujsol2024.html  
- 2023 : https://www.mathkang.org/concours/sujsol2023.html  
- 2022 : https://www.mathkang.org/concours/sujsol2022.html  
- 2021 : https://www.mathkang.org/concours/sujsol2021.html  
- 2020 : https://www.mathkang.org/concours/sujsol2020.html  

- Exos-Kangourou : https://www.mathkang.org/ExosKangourou/default.htm  
- Catalogue annales : https://www.mathkang.org/catalogue/annales.html  
- Menu concours : https://www.mathkang.org/concours/  
""")
