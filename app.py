import random
import time
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch, Circle

# ============================================================
# Config
# ============================================================

LABELS = ["A", "B", "C", "D", "E"]
SERIE_LEN = 10
DURATION_SEC = 20 * 60  # 20 minutes
BANK_SIZE = 50

# ============================================================
# Helpers QCM + figures
# ============================================================

def make_mcq(correct: str, wrongs: list[str], n: int = 5):
    pool = [w for w in wrongs if w != correct]
    pool = list(dict.fromkeys(pool))
    while len(pool) < n - 1:
        pool.append(random.choice(wrongs))
        pool = list(dict.fromkeys(pool))
        if len(pool) > 100:
            break
    choices = [correct] + random.sample(pool, n - 1)
    random.shuffle(choices)
    return choices, choices.index(correct)

def fig_base():
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax

# ============================================================
# Exercices “Kangourou 6e” (plus corsés, avec schémas)
# Each exercise returns dict:
# {topic, question, choices(5), answer_index, explanation, draw?(ax)}
# ============================================================

def ex_grid_area_missing():
    w = random.randint(7, 11)
    h = random.randint(5, 9)

    hole_w = random.randint(1, max(1, w // 3))
    hole_h = random.randint(1, max(1, h // 3))
    hx = random.randint(1, w - hole_w - 1) if w - hole_w - 1 >= 1 else 0
    hy = random.randint(1, h - hole_h - 1) if h - hole_h - 1 >= 1 else 0

    total = w * h
    hole = hole_w * hole_h
    correct = total - hole

    correct_s = str(correct)
    wrongs = [
        str(total),
        str(hole),
        str(total + hole),
        str((w + h) * 2),  # piège périmètre
        str(correct + 1),
        str(max(0, correct - 1)),
        str(w + h),
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        for i in range(w + 1):
            ax.plot([i, i], [0, h], linewidth=1)
        for j in range(h + 1):
            ax.plot([0, w], [j, j], linewidth=1)
        ax.add_patch(Rectangle((hx, hy), hole_w, hole_h, facecolor="white", edgecolor="black", linewidth=2))
        ax.set_xlim(-0.5, w + 0.5)
        ax.set_ylim(-0.5, h + 0.5)
        ax.set_title("Chaque petit carré = 1 unité d'aire", fontsize=11)

    explanation = (
        f"Aire totale du grand rectangle = {w} × {h} = {total}.\n"
        f"Aire du trou = {hole_w} × {hole_h} = {hole}.\n"
        f"Aire grisée = {total} − {hole} = {correct}."
    )

    return {
        "topic": "Aire / Grille",
        "question": "On a un rectangle pavé de carrés (côté 1). Un petit rectangle blanc est enlevé. Quelle est l’aire grisée ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_L_shape_perimeter():
    W = random.randint(8, 12)
    H = random.randint(6, 10)

    cut_w = random.randint(2, max(2, W // 2))
    cut_h = random.randint(2, max(2, H // 2))

    # contour: W + (H-cut_h) + cut_w + cut_h + (W-cut_w) + H
    correct = W + (H - cut_h) + cut_w + cut_h + (W - cut_w) + H
    correct_s = str(correct)

    wrongs = [
        str(2 * (W + H)),
        str(2 * (W + H) - 2 * (cut_w + cut_h)),
        str(2 * (W + H) + 2 * (cut_w + cut_h)),
        str(correct + 2),
        str(max(0, correct - 2)),
        str(W * H),
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        for i in range(W + 1):
            ax.plot([i, i], [0, H], linewidth=0.8)
        for j in range(H + 1):
            ax.plot([0, W], [j, j], linewidth=0.8)

        ax.add_patch(Rectangle((W - cut_w, H - cut_h), cut_w, cut_h, facecolor="white", edgecolor="black", linewidth=2))
        ax.add_patch(Rectangle((0, 0), W, H, fill=False, linewidth=2))
        ax.set_xlim(-0.5, W + 0.5)
        ax.set_ylim(-0.5, H + 0.5)
        ax.set_title("Périmètre de la forme en L", fontsize=11)

    explanation = (
        "On suit le contour de la forme :\n"
        f"W + (H−cut_h) + cut_w + cut_h + (W−cut_w) + H\n"
        f"= {W} + ({H}−{cut_h}) + {cut_w} + {cut_h} + ({W}−{cut_w}) + {H} = {correct}."
    )

    return {
        "topic": "Périmètre / Grille",
        "question": "Sur la grille (côté 1), on a une forme en L. Quel est son périmètre ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_triangle_angle_with_extension():
    a = random.randint(30, 85)
    b = random.randint(20, 75)
    while a + b >= 170:
        b = random.randint(20, 75)

    c = 180 - (a + b)
    ext = a + b
    correct_s = f"{ext}°"

    wrongs = [f"{c}°", f"{180 - a}°", f"{180 - b}°", f"{a}°", f"{b}°", f"{ext + 10}°"]
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
        ax.set_title("Angle extérieur (x) au prolongement", fontsize=11)

    explanation = (
        "Somme des angles d’un triangle = 180°.\n"
        f"Angle intérieur au sommet = 180° − ({a}° + {b}°) = {c}°.\n"
        f"Angle extérieur x = 180° − {c}° = {ext}° (donc aussi x = {a}° + {b}°)."
    )

    return {
        "topic": "Angles",
        "question": f"Sur la figure, deux angles valent {a}° et {b}°. Quelle est la mesure de l’angle extérieur x ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_fraction_bar_model():
    denom = random.choice([6, 8, 10, 12, 14])
    num = random.randint(1, denom - 1)
    correct = f"{num}/{denom}"

    wrongs = [
        f"{denom}/{num}",
        f"{max(1, num-1)}/{denom}",
        f"{min(denom-1, num+1)}/{denom}",
        "1/2", "2/3", "3/4", "1",
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

    explanation = f"La barre est découpée en {denom} parts égales. {num} parts sont coloriées ⇒ {num}/{denom}."
    return {
        "topic": "Fractions",
        "question": "Quelle fraction de la barre est coloriée ? (Lis la fraction sur la figure.)",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_route_perimeter_path():
    L = random.randint(10, 26)
    l = random.randint(6, 18)
    missing = random.choice(["grand", "petit"])
    if missing == "grand":
        correct = 2 * (L + l) - L
        miss_txt = f"un côté de {L} m"
    else:
        correct = 2 * (L + l) - l
        miss_txt = f"un côté de {l} m"

    correct_s = f"{correct} m"
    wrongs = [
        f"{2*(L+l)} m",
        f"{L+l} m",
        f"{2*L+2*l} m",
        f"{2*(L+l)+L} m",
        f"{abs(2*(L+l)-L-l)} m",
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        ax.add_patch(Rectangle((0, 0), L, l, fill=False, linewidth=2))
        ax.add_patch(FancyArrowPatch((1, -0.8), (L-1, -0.8), arrowstyle="->", mutation_scale=15, linewidth=2))
        ax.add_patch(FancyArrowPatch((L+0.8, 1), (L+0.8, l-1), arrowstyle="->", mutation_scale=15, linewidth=2))
        ax.add_patch(FancyArrowPatch((L-1, l+0.8), (1, l+0.8), arrowstyle="->", mutation_scale=15, linewidth=2))
        ax.text(L/2 - 1, -0.2, f"{L} m", fontsize=11)
        ax.text(L+0.2, l/2, f"{l} m", fontsize=11, rotation=90)
        ax.set_xlim(-2.5, L + 3.0)
        ax.set_ylim(-2.5, l + 3.0)
        ax.set_title("Trajet sur 3 côtés", fontsize=11)

    explanation = (
        f"Périmètre du rectangle = 2×({L}+{l}) = {2*(L+l)} m.\n"
        f"On ne parcourt pas {miss_txt}.\n"
        f"Trajet = {2*(L+l)} − ({L if missing=='grand' else l}) = {correct} m."
    )

    return {
        "topic": "Périmètre / Problème",
        "question": f"On marche le long de 3 côtés d’un rectangle (pas le tour complet). On ne parcourt pas {miss_txt}. Quelle est la longueur du trajet ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_balance_logic():
    A = random.randint(3, 9)
    B = random.randint(4, 12)
    left1 = 2*A + B
    left2 = A + 2*B
    ask = random.choice(["A", "B"])
    correct = A if ask == "A" else B
    correct_s = str(correct)

    wrongs = [str(correct + 1), str(max(0, correct - 1)), str(A + B), str(abs(A - B)), str(2*correct)]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        y1, y2 = 2.0, 0.6

        x = 0.5
        for _ in range(2):
            ax.add_patch(Circle((x, y1), 0.25, fill=False, linewidth=2))
            ax.text(x-0.08, y1-0.07, "A", fontsize=10)
            x += 0.7
        ax.add_patch(Rectangle((x-0.25, y1-0.25), 0.5, 0.5, fill=False, linewidth=2))
        ax.text(x-0.07, y1-0.07, "B", fontsize=10)
        ax.text(x+0.7, y1-0.08, f"= {left1}", fontsize=12)

        x = 0.5
        ax.add_patch(Circle((x, y2), 0.25, fill=False, linewidth=2))
        ax.text(x-0.08, y2-0.07, "A", fontsize=10)
        x += 0.7
        for _ in range(2):
            ax.add_patch(Rectangle((x-0.25, y2-0.25), 0.5, 0.5, fill=False, linewidth=2))
            ax.text(x-0.07, y2-0.07, "B", fontsize=10)
            x += 0.7
        ax.text(x+0.2, y2-0.08, f"= {left2}", fontsize=12)

        ax.set_xlim(0, 6.5)
        ax.set_ylim(0, 3.0)
        ax.set_title("Deux balances (masses inconnues)", fontsize=11)

    explanation = (
        "On a :\n"
        f"2A + B = {left1}\n"
        f"A + 2B = {left2}\n"
        f"Solution entière : A = {A}, B = {B}.\n"
        f"Donc la valeur demandée est {correct}."
    )

    return {
        "topic": "Logique / Balance",
        "question": f"D’après les deux balances, quelle est la valeur de {ask} ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

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
    return {
        "topic": "Divisibilité",
        "question": "Quel nombre est divisible par 3 ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
    }

EXERCISES = [
    ex_grid_area_missing,
    ex_L_shape_perimeter,
    ex_triangle_angle_with_extension,
    ex_fraction_bar_model,
    ex_route_perimeter_path,
    ex_balance_logic,
    ex_div_by_3,
]

def new_exercise():
    ex = random.choice(EXERCISES)()
    ex["id"] = random.randint(100000, 999999)
    return ex

def make_bank(n=BANK_SIZE):
    return [new_exercise() for _ in range(n)]

# ============================================================
# Game state helpers
# ============================================================

def reset_game():
    st.session_state.game_started = False
    st.session_state.start_time = None
    st.session_state.question_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.exercise = new_exercise()
    st.session_state.finished = False
    st.session_state.last_feedback = None

def remaining_seconds():
    if not st.session_state.start_time:
        return DURATION_SEC
    elapsed = time.time() - st.session_state.start_time
    return max(0, int(DURATION_SEC - elapsed))

# ============================================================
# UI
# ============================================================

st.set_page_config(page_title="Kangourou 6e — Agent IA", page_icon="🦘", layout="centered")
st.title("🦘 Kangourou 6e — Bonjour Camille (Série + Banque + Annales)")

# init session state
if "game_started" not in st.session_state:
    reset_game()
if "bank" not in st.session_state:
    st.session_state.bank = make_bank(n=BANK_SIZE)

tab1, tab2, tab3 = st.tabs(["🎮 Série (10 questions)", "📚 Banque (50) + corrigés", "🗂️ Annales officielles"])

# ----------------------------
# TAB 1 : Série
# ----------------------------
with tab1:
    st.caption("Série de 10 questions • QCM A–E • Correction expliquée • Chrono 20 min • Schémas")

    # Header metrics
    r = remaining_seconds()
    top1, top2, top3 = st.columns([1.2, 1, 1])
    with top1:
        st.metric("Progression", f"{min(st.session_state.question_idx, SERIE_LEN)} / {SERIE_LEN}")
    with top2:
        st.metric("Score", f"{st.session_state.score}")
    with top3:
        st.metric("Temps restant", f"{r//60:02d}:{r%60:02d}")

    st.divider()

    # Not started screen
    if not st.session_state.game_started:
        st.subheader("Prêt ?")
        st.write("Clique **Démarrer** : tu as **20 minutes** pour faire **10 questions**.")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("▶️ Démarrer", use_container_width=True):
                st.session_state.game_started = True
                st.session_state.start_time = time.time()
                st.rerun()
        with c2:
            if st.button("🧹 Réinitialiser", use_container_width=True):
                reset_game()
                st.rerun()

        st.info("Le chrono se met à jour à chaque interaction (normal sur Streamlit).")
    else:
        # Game running
        if r <= 0:
            st.session_state.finished = True

        if st.session_state.question_idx >= SERIE_LEN:
            st.session_state.finished = True

        if st.session_state.finished:
            st.subheader("🏁 Série terminée")
            reason = "⏱️ Temps écoulé" if r <= 0 else "✅ 10 questions complétées"
            st.write(reason)
            done = min(st.session_state.question_idx, SERIE_LEN)
            st.success(f"Score final : **{st.session_state.score} / {done}**")

            a, b = st.columns(2)
            with a:
                if st.button("🔁 Rejouer", use_container_width=True):
                    reset_game()
                    st.rerun()
            with b:
                if st.button("🧹 Reset (accueil)", use_container_width=True):
                    reset_game()
                    st.rerun()
        else:
            ex = st.session_state.exercise

            st.subheader(f"Question {st.session_state.question_idx + 1}")
            st.write(ex["question"])

            if "draw" in ex and callable(ex["draw"]):
                fig, ax = fig_base()
                ex["draw"](ax)
                st.pyplot(fig, clear_figure=True)

            st.write("**Choisis une réponse :**")
            btn_cols = st.columns(5)
            for i in range(5):
                with btn_cols[i]:
                    if st.button(
                        f"{LABELS[i]}",
                        key=f"pick_{ex['id']}_{i}",
                        disabled=st.session_state.answered,
                        use_container_width=True
                    ):
                        st.session_state.selected = i
                        st.session_state.answered = True
                        correct_i = ex["answer_index"]
                        if i == correct_i:
                            st.session_state.score += 1
                            st.session_state.last_feedback = ("ok", f"✅ Bonne réponse : {LABELS[correct_i]}")
                        else:
                            st.session_state.last_feedback = ("ko", f"❌ Faux. Bonne réponse : {LABELS[correct_i]}")
                        st.rerun()

            st.markdown("**Propositions :**")
            for i, choice in enumerate(ex["choices"]):
                st.write(f"- **{LABELS[i]}** : {choice}")

            if st.session_state.answered:
                kind, msg = st.session_state.last_feedback if st.session_state.last_feedback else ("", "")
                (st.success if kind == "ok" else st.error)(msg)

                correct_i = ex["answer_index"]
                st.info(f"Réponse : **{LABELS[correct_i]}** — {ex['choices'][correct_i]}")

                with st.expander("Voir la correction expliquée", expanded=True):
                    st.markdown("**Correction**")
                    st.write(ex["explanation"])

                st.divider()
                c1, c2, c3 = st.columns(3)

                with c1:
                    if st.button("🔁 Refaire (sans compter)", use_container_width=True):
                        st.session_state.answered = False
                        st.session_state.selected = None
                        st.session_state.last_feedback = None
                        st.rerun()

                with c2:
                    if st.button("➡️ Suivant", use_container_width=True):
                        st.session_state.question_idx += 1
                        st.session_state.exercise = new_exercise()
                        st.session_state.answered = False
                        st.session_state.selected = None
                        st.session_state.last_feedback = None
                        st.rerun()

                with c3:
                    if st.button("🧹 Reset série", use_container_width=True):
                        reset_game()
                        st.rerun()
            else:
                st.warning("Clique sur A–E pour répondre.")

# ----------------------------
# TAB 2 : Banque 50 + corrigés
# ----------------------------
with tab2:
    st.caption("50 exercices “style Kangourou 6e” (générés une fois, puis figés) + corrigés.")

    left, right = st.columns([1, 1])
    with left:
        if st.button("🔄 Régénérer la banque (50 exos)"):
            st.session_state.bank = make_bank(n=BANK_SIZE)
            st.rerun()
    with right:
        show_solutions = st.toggle("Afficher les corrigés", value=False)

    st.divider()

    topics = {}
    for ex in st.session_state.bank:
        topics.setdefault(ex.get("topic", "Autres"), []).append(ex)

    for topic, exos in topics.items():
        st.subheader(f"📌 {topic}")
        for idx, ex in enumerate(exos, start=1):
            title = ex["question"]
            if len(title) > 70:
                title = title[:70] + "…"
            with st.expander(f"Exercice {idx} — {title}"):
                st.write(ex["question"])

                if "draw" in ex and callable(ex["draw"]):
                    fig, ax = fig_base()
                    ex["draw"](ax)
                    st.pyplot(fig, clear_figure=True)

                st.markdown("**Propositions :**")
                for i, choice in enumerate(ex["choices"]):
                    st.write(f"- **{LABELS[i]}** : {choice}")

                if show_solutions:
                    correct_i = ex["answer_index"]
                    st.success(f"✅ Réponse : {LABELS[correct_i]} — {ex['choices'][correct_i]}")
                    st.markdown("**Correction**")
                    st.write(ex["explanation"])

# ----------------------------
# TAB 3 : Annales officielles (liens)
# ----------------------------
with tab3:
    st.caption("Liens officiels ACL / Kangourou (mathkang.org) vers sujets & solutions. Pour le niveau 6e, vise en général le **Sujet B (6e–5e)**.")

    st.markdown("### Sujets & solutions (pages par année)")
    st.markdown("""
- 2025 : https://www.mathkang.org/concours/sujsol2025.html
- 2024 : https://www.mathkang.org/concours/sujsol2024.html
- 2023 : https://www.mathkang.org/concours/sujsol2023.html
- 2022 : https://www.mathkang.org/concours/sujsol2022.html
- 2021 : https://www.mathkang.org/concours/sujsol2021.html
- 2020 : https://www.mathkang.org/concours/sujsol2020.html
""")

    st.markdown("### Menu concours")
    st.markdown("""
- Concours Kangourou : https://www.mathkang.org/concours/
""")

    st.markdown("### Base d’exercices (archives)")
    st.markdown("""
- Exos-Kangourou : https://www.mathkang.org/ExosKangourou/default.htm
""")

    st.markdown("### Catalogue annales")
    st.markdown("""
- Annales (catalogue) : https://www.mathkang.org/catalogue/annales.html
""")

    st.info("Astuce : sur les pages “Sujets & solutions”, choisis le **Sujet B (6e–5e)**.")
