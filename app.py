import random
import time
import math
import streamlit as st

# ============================================================
# Utilitaires
# ============================================================

LABELS = ["A", "B", "C", "D", "E"]

def pick_unique(nums, k, avoid=None):
    avoid = set() if avoid is None else set(avoid)
    out = []
    for x in nums:
        if x not in avoid and x not in out:
            out.append(x)
        if len(out) >= k:
            break
    return out

def make_mcq(correct, wrongs, n=5):
    """
    correct: str
    wrongs: list[str]
    returns (choices, answer_idx)
    """
    pool = [w for w in wrongs if w != correct]
    # garantis assez de propositions
    while len(pool) < (n - 1):
        pool.append(random.choice(wrongs) + " ")  # fallback léger (rare)
        pool = list(dict.fromkeys(pool))  # unique preserve order

    choices = [correct] + random.sample(pool, n - 1)
    random.shuffle(choices)
    return choices, choices.index(correct)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# ============================================================
# Générateurs “Kangourou 6e” (QCM 5 choix)
# Chaque exo renvoie dict: question, choices(5), answer_index, explanation
# ============================================================

def ex_trap_addition():
    # "piège" avec compensation : 49 + 38, 59 + 27 etc.
    a = random.choice([39, 49, 59, 69, 79])
    b = random.randint(21, 48)
    correct = a + b
    # distractors typiques
    wrongs = [
        str(correct + 1),
        str(correct - 1),
        str(correct + 10),
        str(correct - 10),
        str((a + 1) + (b - 1)),  # même résultat -> éviter, mais c'est correct; on le met pas
        str((a - 1) + (b + 1)),  # idem
        str(a + (b + 2)),
        str((a - 2) + b),
    ]
    # Nettoyage
    wrongs = [w for w in wrongs if w != str(correct)]
    correct_s = str(correct)
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        f"Astuce de compensation : {a} est proche de {a+1}.\n"
        f"{a} + {b} = ({a}+1) + ({b}-1) = {a+1} + {b-1} = {correct}."
    )
    return {"question": f"Calcule : {a} + {b}", "choices": choices, "answer_index": ans, "explanation": explanation}

def ex_logic_odd_even():
    # logique parité
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    # question: (a+b) est pair/impair ?
    correct = "pair" if (a + b) % 2 == 0 else "impair"
    wrongs = ["pair", "impair", "multiple de 3", "multiple de 5", "premier"]
    # Choix texte (Kangourou aime ça)
    # On veut 5 choix dont pair/impair toujours présents
    options = ["pair", "impair", "multiple de 3", "multiple de 5", "premier"]
    choices = options[:]  # déjà 5
    ans = choices.index(correct)

    explanation = (
        f"{a} est {'pair' if a%2==0 else 'impair'} et {b} est {'pair' if b%2==0 else 'impair'}.\n"
        "Règle : pair+pair=pair, impair+impair=pair, pair+impair=impair.\n"
        f"Donc {a}+{b} est {correct}."
    )
    return {
        "question": f"{a} + {b} est un nombre :",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_fraction_of_number():
    denom = random.choice([2, 3, 4, 5, 6, 8, 10, 12])
    num = random.randint(1, denom - 1)
    k = random.randint(2, 12)
    total = denom * k
    correct = num * k

    correct_s = str(correct)
    wrongs = [
        str(total - correct),
        str(num * denom),
        str(k + num),
        str(k * denom),
        str(correct + k),
        str(max(0, correct - k)),
        str(correct + 1),
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        f"Pour calculer {num}/{denom} de {total} :\n"
        f"1) {total} ÷ {denom} = {k}\n"
        f"2) {k} × {num} = {correct}"
    )
    return {
        "question": f"Quelle est la valeur de {num}/{denom} de {total} ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_conversion_cm_mm():
    # conversion piège
    cm = random.randint(12, 190)
    correct = cm * 10  # mm
    correct_s = f"{correct} mm"
    wrongs = [
        f"{cm} mm",
        f"{cm*100} mm",
        f"{cm//10} mm",
        f"{cm*10 + 1} mm",
        f"{max(0, cm*10 - 10)} mm",
        f"{cm} cm",  # mauvais unité
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = f"1 cm = 10 mm, donc {cm} cm = {cm} × 10 = {correct} mm."
    return {
        "question": f"Convertis : {cm} cm en millimètres (mm).",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_time_trap():
    # heure + minutes avec passage d'heure
    h = random.randint(8, 18)
    m = random.choice([35, 40, 45, 50, 55])
    add = random.choice([10, 15, 20, 25, 30, 35])
    start = h * 60 + m
    end = start + add
    hh = (end // 60) % 24
    mm = end % 60
    correct_s = f"{hh:02d} h {mm:02d}"

    # distractors
    wrongs = [
        f"{h:02d} h {min(59, m+add):02d}",
        f"{(h+1):02d} h {m:02d}",
        f"{hh:02d} h {((mm+5)%60):02d}",
        f"{hh:02d} h {((mm+10)%60):02d}",
        f"{(hh-1)%24:02d} h {mm:02d}",
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        f"On ajoute {add} minutes à {h:02d} h {m:02d}.\n"
        f"En minutes : {h*60+m} + {add} = {end} minutes.\n"
        f"Donc {hh:02d} h {mm:02d}."
    )
    return {
        "question": f"Il est {h:02d} h {m:02d}. Quelle heure sera-t-il dans {add} minutes ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_angles_triangle():
    # somme angles triangle = 180
    a = random.randint(30, 80)
    b = random.randint(30, 80)
    # assurer a+b<180
    if a + b >= 170:
        b = 160 - a
    c = 180 - (a + b)
    correct_s = f"{c}°"

    wrongs = [
        f"{180 - a}°",
        f"{180 - b}°",
        f"{a + b}°",
        f"{a}°",
        f"{b}°",
        f"{c + 10}°",
        f"{max(0, c - 10)}°",
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        "Dans un triangle, la somme des angles vaut 180°.\n"
        f"Donc angle manquant = 180° - ({a}° + {b}°) = {c}°."
    )
    return {
        "question": f"Dans un triangle, deux angles mesurent {a}° et {b}°. Combien mesure le troisième angle ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_perimeter_trap():
    # rectangle / carré déguisé
    L = random.randint(5, 20)
    l = random.randint(3, min(15, L))
    correct = 2 * (L + l)
    correct_s = f"{correct} cm"

    wrongs = [
        f"{L + l} cm",
        f"{L * l} cm",
        f"{2*L + l} cm",
        f"{L + 2*l} cm",
        f"{correct + 2} cm",
        f"{max(0, correct - 2)} cm",
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = f"Périmètre = 2 × (L + l) = 2 × ({L} + {l}) = {correct} cm."
    return {
        "question": f"Un rectangle a une longueur de {L} cm et une largeur de {l} cm. Quel est son périmètre ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_area_vs_perimeter_trap():
    # piège classique: confondre aire / périmètre
    L = random.randint(6, 16)
    l = random.randint(3, 10)
    correct = L * l
    correct_s = f"{correct} cm²"
    wrongs = [
        f"{2*(L+l)} cm²",     # mélange unités
        f"{2*(L+l)} cm",
        f"{L+l} cm²",
        f"{L*l} cm",          # mauvaise unité
        f"{(L+l)} cm",
        f"{correct + L} cm²",
        f"{max(0, correct - l)} cm²",
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        "Aire d’un rectangle = longueur × largeur.\n"
        f"Ici : {L} × {l} = {correct} cm²."
    )
    return {
        "question": f"Un rectangle mesure {L} cm sur {l} cm. Quelle est son aire ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_divisibility_trap():
    # “quel nombre est divisible par 3 ?”
    base = random.randint(100, 999)
    # fabrique 1 multiple de 3, et 4 non
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
    explanation = (
        "Un nombre est divisible par 3 si la somme de ses chiffres est divisible par 3.\n"
        f"Ici, pour {correct} : somme = {sum(map(int, str(correct)))} (multiple de 3)."
    )
    return {
        "question": "Quel nombre est divisible par 3 ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_pattern_kangourou():
    # suite “piège” alternée
    a = random.randint(2, 8)
    b = random.randint(2, 8)
    start = random.randint(5, 20)
    # suite: +a, +b, +a, +b
    s1 = start
    s2 = s1 + a
    s3 = s2 + b
    s4 = s3 + a
    correct = s4 + b
    correct_s = str(correct)

    wrongs = [
        str(s4 + a),              # répète +a
        str(s4 + (a + b)),        # ajoute tout
        str(s4 + (b - 1)),
        str(s4 + (b + 1)),
        str(s4 + 2*b),
        str(s4 + 2*a),
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        f"La règle alterne +{a} puis +{b}.\n"
        f"{s1} → {s2} (+{a}) → {s3} (+{b}) → {s4} (+{a}) → {correct} (+{b})."
    )
    return {
        "question": f"Complète la suite : {s1}, {s2}, {s3}, {s4}, ... Quel est le prochain terme ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_word_problem_money():
    # problème simple mais “piège” d’addition/multiplication
    price = random.choice([3, 4, 5, 6, 7, 8, 9])
    qty = random.randint(3, 7)
    pay = random.choice([20, 30, 40])
    total = price * qty
    change = pay - total
    # on force change positif
    if change <= 0:
        pay = total + random.choice([5, 10, 20])
        change = pay - total

    correct_s = f"{change} €"
    wrongs = [
        f"{total} €",
        f"{pay - price} €",
        f"{pay - qty} €",
        f"{change + price} €",
        f"{max(0, change - price)} €",
        f"{pay} €",
    ]
    wrongs = [w for w in wrongs if w != correct_s]
    choices, ans = make_mcq(correct_s, wrongs, 5)

    explanation = (
        f"Coût total = {qty} × {price} = {total} €.\n"
        f"Monnaie rendue = {pay} - {total} = {change} €."
    )
    return {
        "question": f"Un cahier coûte {price} €. Tu en achètes {qty}. Tu payes avec {pay} €. Quelle monnaie te rend-on ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

def ex_fraction_compare():
    # compare fractions same denom or close; Kangourou aime comparer rapidement
    denom = random.choice([8, 10, 12, 14])
    a = random.randint(1, denom - 1)
    b = random.randint(1, denom - 1)
    while b == a:
        b = random.randint(1, denom - 1)

    # question: lequel est plus grand ?
    fa = a / denom
    fb = b / denom
    correct = f"{a}/{denom}" if fa > fb else f"{b}/{denom}"

    choices = [
        f"{a}/{denom}",
        f"{b}/{denom}",
        "Ils sont égaux",
        f"{denom}/{a}",  # piège inversion
        f"{denom}/{b}",
    ]
    ans = choices.index(correct)
    explanation = (
        f"Les deux fractions ont le même dénominateur ({denom}).\n"
        "Celle qui a le plus grand numérateur est la plus grande.\n"
        f"Ici : {a} et {b} → la plus grande est {correct}."
    )
    return {
        "question": f"Quelle fraction est la plus grande ?",
        "choices": choices,
        "answer_index": ans,
        "explanation": explanation
    }

EXERCISES = [
    ex_trap_addition,
    ex_logic_odd_even,
    ex_fraction_of_number,
    ex_conversion_cm_mm,
    ex_time_trap,
    ex_angles_triangle,
    ex_perimeter_trap,
    ex_area_vs_perimeter_trap,
    ex_divisibility_trap,
    ex_pattern_kangourou,
    ex_word_problem_money,
    ex_fraction_compare,
]

def new_exercise():
    ex = random.choice(EXERCISES)()
    ex["id"] = random.randint(100000, 999999)
    return ex

# ============================================================
# Gestion session: série, chrono, score
# ============================================================

SERIE_LEN = 10
DURATION_SEC = 20 * 60  # 20 minutes

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
    # fin si chrono à 0 ou 10 questions faites
    if remaining_seconds() <= 0:
        st.session_state.finished = True
    if st.session_state.question_idx >= SERIE_LEN:
        st.session_state.finished = True

# ============================================================
# UI
# ============================================================

st.set_page_config(page_title="Kangourou 6e — Agent IA", page_icon="🦘", layout="centered")

st.title("🦘 Agent IA — Kangourou (niveau 6e)")
st.caption("Série de 10 questions • QCM (A–E) • Correction expliquée • Chrono 20 min")

# init state
if "game_started" not in st.session_state:
    reset_game()

# Bandeau haut: chrono + progression
top1, top2, top3 = st.columns([1.2, 1, 1])

with top1:
    st.metric("Progression", f"{min(st.session_state.question_idx, SERIE_LEN)} / {SERIE_LEN}")
with top2:
    st.metric("Score", f"{st.session_state.score}")
with top3:
    r = remaining_seconds()
    st.metric("Temps restant", f"{r//60:02d}:{r%60:02d}")

st.divider()

# Écran d'accueil
if not st.session_state.game_started:
    st.subheader("Prêt ?")
    st.write("Clique sur **Démarrer** : tu as **20 minutes** pour faire **10 questions**.")
    cols = st.columns([1, 1])
    with cols[0]:
        if st.button("▶️ Démarrer", use_container_width=True):
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.session_state.finished = False
            st.rerun()
    with cols[1]:
        if st.button("🧹 Réinitialiser", use_container_width=True):
            reset_game()
            st.rerun()

    st.info("Astuce : le chrono se met à jour à chaque clic. (C’est normal sur Streamlit.)")
    st.stop()

# Vérifie fin
finish_if_needed()

# Écran fin
if st.session_state.finished:
    st.subheader("🏁 Série terminée")
    r = remaining_seconds()
    reason = "⏱️ Temps écoulé" if r <= 0 else "✅ 10 questions complétées"
    st.write(reason)
    st.success(f"Ton score final : **{st.session_state.score} / {min(st.session_state.question_idx, SERIE_LEN)}**")

    colA, colB = st.columns([1, 1])
    with colA:
        if st.button("🔁 Rejouer une série (10 questions)", use_container_width=True):
            reset_game()
            st.rerun()
    with colB:
        if st.button("⏹️ Revenir à l’accueil", use_container_width=True):
            reset_game()
            st.rerun()

    st.stop()

# Si le chrono est à 0 au milieu d’une question
if remaining_seconds() <= 0:
    st.session_state.finished = True
    st.rerun()

# Question courante
ex = st.session_state.exercise

st.subheader(f"Question {st.session_state.question_idx + 1}")
st.write(ex["question"])

st.write("**Choisis une réponse :**")

# Boutons de réponses A–E
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
                st.session_state.last_feedback = ("ko", f"❌ Faux. La bonne réponse est {LABELS[correct_i]}")

            st.rerun()

# Affiche les choix (lisibles)
st.markdown("**Propositions :**")
for i, choice in enumerate(ex["choices"]):
    st.write(f"- **{LABELS[i]}** : {choice}")

# Feedback + correction
if st.session_state.answered:
    kind, msg = st.session_state.last_feedback if st.session_state.last_feedback else ("", "")
    if kind == "ok":
        st.success(msg)
    else:
        st.error(msg)

    correct_i = ex["answer_index"]
    st.info(f"Réponse : **{LABELS[correct_i]}** — {ex['choices'][correct_i]}")

    with st.expander("Voir la correction expliquée", expanded=True):
        st.markdown("**Correction**")
        st.write(ex["explanation"])

    st.divider()

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("🔁 Refaire (sans compter)", use_container_width=True):
            st.session_state.answered = False
            st.session_state.selected = None
            st.session_state.last_feedback = None
            st.rerun()

    with col2:
        if st.button("➡️ Suivant", use_container_width=True):
            st.session_state.question_idx += 1
            st.session_state.exercise = new_exercise()
            st.session_state.answered = False
            st.session_state.selected = None
            st.session_state.last_feedback = None
            finish_if_needed()
            st.rerun()

    with col3:
        if st.button("🧹 Reset série", use_container_width=True):
            reset_game()
            st.rerun()

else:
    st.warning("Réponds en cliquant sur A, B, C, D ou E.")

st.divider()
st.caption("Contenu : logique + géométrie + calcul + conversions + problèmes (niveau 6e, style Kangourou).")
