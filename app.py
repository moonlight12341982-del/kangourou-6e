import random
import streamlit as st

# ----------------------------
# Générateurs d'exercices 6e (style Kangourou)
# Chaque exercice = {question, choices[4], answer_index, explanation}
# ----------------------------

def ex_addition_astuce():
    # Exemple: 48 + 39 = ?
    a = random.randint(20, 79)
    b = random.randint(20, 79)
    correct = a + b
    # Propositions proches
    distractors = {correct + 1, correct - 1, correct + 10, correct - 10, correct + 9, correct - 9}
    distractors.discard(correct)
    choices = [correct] + random.sample(list(distractors), 3)
    random.shuffle(choices)
    answer_index = choices.index(correct)

    # Explication "astuce"
    # (découper b en dizaines + unités)
    tens = (b // 10) * 10
    ones = b % 10
    explanation = (
        f"On peut décomposer {b} en {tens} + {ones}.\n"
        f"{a} + {b} = {a} + {tens} + {ones} = {a+tens} + {ones} = {a+tens+ones}."
    )

    return {
        "question": f"Calcule : {a} + {b}",
        "choices": [str(x) for x in choices],
        "answer_index": answer_index,
        "explanation": explanation
    }

def ex_multiplication():
    # Exemple: 7 × 8
    a = random.randint(3, 12)
    b = random.randint(3, 12)
    correct = a * b
    distractors = {correct + a, correct + b, correct - a, correct - b, correct + 1, correct - 1}
    distractors = {x for x in distractors if x > 0}
    distractors.discard(correct)
    choices = [correct] + random.sample(list(distractors), 3)
    random.shuffle(choices)
    answer_index = choices.index(correct)

    explanation = f"{a} × {b} = {correct}. (Table de {a} ou de {b})"

    return {
        "question": f"Calcule : {a} × {b}",
        "choices": [str(x) for x in choices],
        "answer_index": answer_index,
        "explanation": explanation
    }

def ex_fraction_simple():
    # Exemple : 3/4 de 20
    denom = random.choice([2, 3, 4, 5, 6, 8, 10])
    num = random.randint(1, denom - 1)
    k = random.randint(2, 10)
    total = denom * k
    correct = num * k  # num/denom of total

    # distractors
    distractors = {correct + k, correct - k, num * denom, total - correct, correct + 1, correct - 1}
    distractors = {x for x in distractors if x >= 0}
    distractors.discard(correct)
    # éviter doublons / manque
    distractors_list = list(distractors)
    while len(distractors_list) < 3:
        distractors_list.append(correct + random.randint(2, 12))
    choices = [correct] + random.sample(distractors_list, 3)
    random.shuffle(choices)
    answer_index = choices.index(correct)

    explanation = (
        f"Pour calculer {num}/{denom} de {total} :\n"
        f"1) On divise {total} par {denom} → {total} ÷ {denom} = {k}\n"
        f"2) Puis on multiplie par {num} → {k} × {num} = {correct}"
    )

    return {
        "question": f"Quelle est la valeur de {num}/{denom} de {total} ?",
        "choices": [str(x) for x in choices],
        "answer_index": answer_index,
        "explanation": explanation
    }

def ex_perimetre_rectangle():
    # Rectangle longueur L, largeur l
    L = random.randint(4, 20)
    l = random.randint(3, min(15, L))
    correct = 2 * (L + l)

    distractors = {L + l, 2 * L + l, L + 2 * l, L * l, correct + 2, correct - 2}
    distractors = {x for x in distractors if x > 0}
    distractors.discard(correct)
    choices = [correct] + random.sample(list(distractors), 3)
    random.shuffle(choices)
    answer_index = choices.index(correct)

    explanation = f"Périmètre d’un rectangle = 2 × (L + l) = 2 × ({L} + {l}) = {correct}."

    return {
        "question": f"Un rectangle a une longueur de {L} cm et une largeur de {l} cm. Quel est son périmètre ?",
        "choices": [str(x) for x in choices],
        "answer_index": answer_index,
        "explanation": explanation
    }

def ex_suite():
    # Suite simple type +d
    start = random.randint(1, 30)
    d = random.randint(2, 9)
    n_terms = 4
    seq = [start + i * d for i in range(n_terms)]
    correct = start + n_terms * d  # prochain terme

    distractors = {correct + d, correct - d, correct + 1, correct - 1, start * d}
    distractors = {x for x in distractors if x > 0}
    distractors.discard(correct)
    choices = [correct] + random.sample(list(distractors), 3)
    random.shuffle(choices)
    answer_index = choices.index(correct)

    explanation = (
        f"La suite augmente de {d} à chaque fois.\n"
        f"Donc après {seq[-1]}, on ajoute encore {d} : {seq[-1]} + {d} = {correct}."
    )

    return {
        "question": f"Complète la suite : {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ... Quel est le prochain terme ?",
        "choices": [str(x) for x in choices],
        "answer_index": answer_index,
        "explanation": explanation
    }

EXERCISE_FACTORIES = [
    ex_addition_astuce,
    ex_multiplication,
    ex_fraction_simple,
    ex_perimetre_rectangle,
    ex_suite,
]

def new_exercise():
    factory = random.choice(EXERCISE_FACTORIES)
    ex = factory()
    ex["id"] = random.randint(100000, 999999)
    return ex

# ----------------------------
# UI Streamlit
# ----------------------------

st.set_page_config(page_title="Agent IA Kangourou 6e", page_icon="🦘", layout="centered")

st.title("🦘 Agent IA — Exercices Kangourou (niveau 6e)")
st.caption("QCM + correction expliquée. Clique sur une réponse, puis sur Suivant pour un nouvel exercice.")

# Session state
if "exercise" not in st.session_state:
    st.session_state.exercise = new_exercise()
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = None
if "score" not in st.session_state:
    st.session_state.score = 0
if "total" not in st.session_state:
    st.session_state.total = 0

ex = st.session_state.exercise

# Header / score
colA, colB = st.columns([1, 1])
with colA:
    st.metric("Score", f"{st.session_state.score} / {st.session_state.total}")
with colB:
    difficulty = st.selectbox("Mode", ["Kangourou (QCM)"], index=0, disabled=True)

st.divider()

# Question
st.subheader("Exercice")
st.write(ex["question"])

choices = ex["choices"]
labels = ["A", "B", "C", "D"]

st.write("**Choisis une réponse :**")

# Réponses via boutons
btn_cols = st.columns(4)
for i in range(4):
    with btn_cols[i]:
        if st.button(f"{labels[i]} : {choices[i]}", key=f"choice_{ex['id']}_{i}", disabled=st.session_state.answered):
            st.session_state.selected = i
            st.session_state.answered = True
            st.session_state.total += 1
            if i == ex["answer_index"]:
                st.session_state.score += 1

# Feedback + correction
if st.session_state.answered:
    correct_i = ex["answer_index"]
    user_i = st.session_state.selected

    if user_i == correct_i:
        st.success(f"✅ Bonne réponse ! ({labels[correct_i]})")
    else:
        st.error(f"❌ Pas tout à fait. La bonne réponse est {labels[correct_i]} : {choices[correct_i]}")

    with st.expander("Voir la correction expliquée", expanded=True):
        st.markdown("**Correction**")
        st.write(ex["explanation"])

    st.divider()

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔁 Refaire (même exercice)"):
            st.session_state.answered = False
            st.session_state.selected = None
            # total/score ne bougent pas ici (c’est un “rejouer”)
            # Si tu veux que ça compte, dis-moi et je l’ajuste.
            st.rerun()

    with col2:
        if st.button("➡️ Suivant (nouvel exercice)"):
            st.session_state.exercise = new_exercise()
            st.session_state.answered = False
            st.session_state.selected = None
            st.rerun()

# Footer: reset
st.divider()
if st.button("🧹 Réinitialiser le score"):
    st.session_state.exercise = new_exercise()
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.score = 0
    st.session_state.total = 0
    st.rerun()
