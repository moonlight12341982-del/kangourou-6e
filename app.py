import random
import time
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch

# ============================================================
# Config
# ============================================================

LABELS = ["A", "B", "C", "D", "E"]
SERIE_LEN = 10
DURATION_SEC = 20 * 60  # 20 min

# ============================================================
# Outils QCM
# ============================================================

def make_mcq(correct, wrongs, n=5):
    pool = [w for w in wrongs if w != correct]
    pool = list(dict.fromkeys(pool))  # unique
    while len(pool) < n - 1:
        pool.append(str(int(correct) + random.randint(2, 15)) if correct.isdigit() else random.choice(wrongs))

    choices = [correct] + random.sample(pool, n - 1)
    random.shuffle(choices)
    return choices, choices.index(correct)

def fig_base():
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax

# ============================================================
# EXERCICES AVEC IMAGES (Kangourou 6e un peu plus corsé)
# Chaque ex: question, choices(5), answer_index, explanation, (optional) draw(ax)
# ============================================================

def ex_grid_area_missing():
    """
    Grille 1x1 : rectangle pavé, un bloc manquant -> aire.
    Style Kangourou: compter vite, éviter de confondre périmètre/aire.
    """
    w = random.randint(6, 10)
    h = random.randint(4, 8)
    # un trou rectangulaire
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
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        # dessine grille
        for i in range(w + 1):
            ax.plot([i, i], [0, h], linewidth=1)
        for j in range(h + 1):
            ax.plot([0, w], [j, j], linewidth=1)
        # trou en blanc (overlay)
        ax.add_patch(Rectangle((hx, hy), hole_w, hole_h, facecolor="white", edgecolor="black", linewidth=2))
        ax.set_xlim(-0.5, w + 0.5)
        ax.set_ylim(-0.5, h + 0.5)
        ax.set_title("Chaque petit carré vaut 1 unité d'aire", fontsize=11)

    explanation = (
        f"Aire totale du grand rectangle = {w} × {h} = {total}.\n"
        f"Aire du trou = {hole_w} × {hole_h} = {hole}.\n"
        f"Aire grisée = {total} − {hole} = {correct}."
    )

    return {
        "question": "On a un grand rectangle pavé de petits carrés de côté 1. Un petit rectangle blanc est “enlevé”. Quelle est l’aire grisée ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_triangle_angle_with_extension():
    """
    Triangle avec un angle extérieur (piège): angle extérieur = somme des deux angles intérieurs opposés.
    """
    a = random.randint(30, 80)
    b = random.randint(20, 70)
    while a + b >= 170:
        b = random.randint(20, 70)
    c = 180 - (a + b)

    # angle extérieur en prolongement de l'angle c : ext = 180 - c = a+b
    ext = a + b
    correct_s = f"{ext}°"

    wrongs = [
        f"{c}°",
        f"{180 - a}°",
        f"{180 - b}°",
        f"{a}°",
        f"{b}°",
        f"{ext + 10}°",
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        # triangle simple
        P = (0, 0)
        Q = (4, 0)
        R = (1.2, 2.8)
        tri = Polygon([P, Q, R], closed=True, fill=False, linewidth=2)
        ax.add_patch(tri)
        # prolongement côté PQ à droite
        ax.plot([4, 5.5], [0, 0], linewidth=2)
        ax.text(0.1, -0.35, f"{a}°", fontsize=12)
        ax.text(3.2, 0.25, f"{b}°", fontsize=12)
        ax.text(4.6, 0.25, "x°", fontsize=12)
        ax.set_xlim(-0.8, 6.0)
        ax.set_ylim(-1.0, 4.0)
        ax.set_title("Angle extérieur (x) au prolongement", fontsize=11)

    explanation = (
        "Dans un triangle : somme des angles = 180°.\n"
        f"L’angle au sommet (intérieur) vaut {c}°.\n"
        "L’angle extérieur en prolongement est supplémentaire : extérieur = 180° − intérieur.\n"
        f"Donc x = 180° − {c}° = {ext}° (et aussi x = {a}° + {b}°)."
    )

    return {
        "question": f"Sur la figure, les angles à la base valent {a}° et {b}°. Quelle est la mesure de l’angle extérieur x ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_fraction_bar_model():
    """
    Bar model: une barre découpée en parts égales. Une fraction est coloriée.
    Question: quelle fraction est coloriée ? (piège simplification possible)
    """
    denom = random.choice([6, 8, 10, 12])
    num = random.randint(1, denom - 1)

    g = num
    d = denom
    # simplifie parfois pour piéger (ex: 6/12 -> 1/2)
    simp = random.choice([True, False])
    if simp:
        k = random.choice([2, 3])
        if denom % k == 0 and num % k == 0:
            g = num // k
            d = denom // k

    correct = f"{num}/{denom}"
    # distractors : inversions, num-1, simplifiée
    wrongs = [
        f"{denom}/{num}",
        f"{max(1, num-1)}/{denom}",
        f"{min(denom-1, num+1)}/{denom}",
        f"{g}/{d}",  # version simplifiée (piège si on demande forme exacte)
        "1/2",
        "1",
    ]
    # Ici on veut la fraction EXACTE coloriée, pas forcément simplifiée
    choices, ans = make_mcq(correct, wrongs, 5)

    def draw(ax):
        # barre de longueur denom
        ax.add_patch(Rectangle((0, 0), denom, 1, fill=False, linewidth=2))
        for i in range(1, denom):
            ax.plot([i, i], [0, 1], linewidth=1)
        # colorie num parts
        ax.add_patch(Rectangle((0, 0), num, 1, facecolor="lightgray", edgecolor="none"))
        ax.set_xlim(-0.5, denom + 0.5)
        ax.set_ylim(-0.8, 1.8)
        ax.text(0, 1.25, "Partie coloriée :", fontsize=11)
        ax.text(0, -0.45, f"{num} parts sur {denom}", fontsize=11)

    explanation = (
        f"La barre est découpée en {denom} parts égales.\n"
        f"{num} parts sont coloriées.\n"
        f"Donc la fraction coloriée est {num}/{denom}."
    )

    return {
        "question": "Quelle fraction de la barre est coloriée ? (Donne la fraction telle qu’on la lit sur la figure.)",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

def ex_route_perimeter_path():
    """
    Problème plus “piège”: chemin autour d’un rectangle mais un côté manquant (on ne fait pas le tour complet).
    On demande la longueur du trajet.
    """
    L = random.randint(10, 24)
    l = random.randint(6, 16)
    missing = random.choice(["grand", "petit"])  # côté qu'on ne parcourt pas

    if missing == "grand":
        correct = 2*(L + l) - L
        miss_txt = f"un côté de {L} m"
    else:
        correct = 2*(L + l) - l
        miss_txt = f"un côté de {l} m"

    correct_s = f"{correct} m"
    wrongs = [
        f"{2*(L+l)} m",
        f"{L+l} m",
        f"{2*L+2*l} m",
        f"{2*(L+l)+L} m",
        f"{abs(2*(L+l)-L-l)} m",
        f"{(2*(L+l))//2} m",
    ]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    def draw(ax):
        ax.add_patch(Rectangle((0, 0), L, l, fill=False, linewidth=2))
        # flèches sur 3 côtés
        # bas
        ax.add_patch(FancyArrowPatch((1, -0.8), (L-1, -0.8), arrowstyle="->", mutation_scale=15, linewidth=2))
        # droite
        ax.add_patch(FancyArrowPatch((L+0.8, 1), (L+0.8, l-1), arrowstyle="->", mutation_scale=15, linewidth=2))
        # haut
        ax.add_patch(FancyArrowPatch((L-1, l+0.8), (1, l+0.8), arrowstyle="->", mutation_scale=15, linewidth=2))
        # côté manquant indiqué
        if missing == "grand":
            ax.text(L/2 - 2, l/2, "Côté non parcouru", fontsize=10, rotation=90)
        else:
            ax.text(L/2 - 3, l/2, "Côté non parcouru", fontsize=10)

        ax.text(L/2 - 1, -0.2, f"{L} m", fontsize=11)
        ax.text(L+0.2, l/2, f"{l} m", fontsize=11, rotation=90)
        ax.set_xlim(-2.5, L + 3.0)
        ax.set_ylim(-2.5, l + 3.0)
        ax.set_title("Trajet sur 3 côtés", fontsize=11)

    explanation = (
        f"Périmètre du rectangle = 2×({L}+{l}) = {2*(L+l)} m.\n"
        f"On ne parcourt pas {miss_txt}.\n"
        f"Longueur du trajet = {2*(L+l)} − ({L if missing=='grand' else l}) = {correct} m."
    )

    return {
        "question": f"On marche le long de 3 côtés d’un rectangle (on ne fait pas le tour complet). On ne parcourt pas {miss_txt}. Quelle est la longueur du trajet ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation,
        "draw": draw,
    }

# Quelques exos sans image (pour varier)
def ex_div_by_3():
    # Quel nombre est divisible par 3 ? (règle somme chiffres)
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
    explanation = f"Somme des chiffres de {correct} = {sum(map(int, str(correct)))} (multiple de 3) ⇒ divisible par 3."
    return {"question": "Quel nombre est divisible par 3 ?", "choices": choices, "answer_index": ans, "explanation": explanation}

EXERCISES = [
    ex_grid_area_missing,
    ex_triangle_angle_with_extension,
    ex_fraction_bar_model,
    ex_route_perimeter_path,
    ex_div_by_3,
]

def new_exercise():
    ex = random.choice(EXERCISES)()
    ex["id"] = random.randint(100000, 999999)
    return ex

# ============================================================
# Gestion partie
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

def finish_if_needed():
    if remaining_seconds() <= 0:
        st.session_state.finished = True
    if st.session_state.question_idx >= SERIE_LEN:
        st.session_state.finished = True

# ============================================================
# UI
# ============================================================

st.set_page_config(page_title="Kangourou 6e — Agent IA (images)", page_icon="🦘", layout="centered")

st.title("🦘 Agent IA — Kangourou 6e (problèmes + images)")
st.caption("Série 10 questions • QCM A–E • Correction • Chrono 20 min • Schémas générés")

if "game_started" not in st.session_state:
    reset_game()

top1, top2, top3 = st.columns([1.2, 1, 1])
with top1:
    st.metric("Progression", f"{min(st.session_state.question_idx, SERIE_LEN)} / {SERIE_LEN}")
with top2:
    st.metric("Score", f"{st.session_state.score}")
with top3:
    r = remaining_seconds()
    st.metric("Temps restant", f"{r//60:02d}:{r%60:02d}")

st.divider()

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

    st.info("Le chrono se met à jour à chaque interaction (c’est normal sur Streamlit).")
    st.stop()

finish_if_needed()

if st.session_state.finished:
    st.subheader("🏁 Série terminée")
    reason = "⏱️ Temps écoulé" if remaining_seconds() <= 0 else "✅ 10 questions complétées"
    st.write(reason)
    done = min(st.session_state.question_idx, SERIE_LEN)
    st.success(f"Score final : **{st.session_state.score} / {done}**")

    a, b = st.columns(2)
    with a:
        if st.button("🔁 Rejouer", use_container_width=True):
            reset_game()
            st.rerun()
    with b:
        if st.button("⏹️ Accueil", use_container_width=True):
            reset_game()
            st.rerun()
    st.stop()

if remaining_seconds() <= 0:
    st.session_state.finished = True
    st.rerun()

ex = st.session_state.exercise

st.subheader(f"Question {st.session_state.question_idx + 1}")
st.write(ex["question"])

# Image si dispo
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
            finish_if_needed()
            st.rerun()

    with c3:
        if st.button("🧹 Reset série", use_container_width=True):
            reset_game()
            st.rerun()
else:
    st.warning("Clique sur A–E pour répondre.")

st.divider()
st.caption("Exos : aire sur grille, angle extérieur, fractions en barres, trajet sur périmètre (piège), divisibilité…")
