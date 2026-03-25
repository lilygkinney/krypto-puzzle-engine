import streamlit as st
import random
import re
from datetime import datetime
from zoneinfo import ZoneInfo


st.set_page_config(page_title="Krypto", page_icon="🧠")

def extract_numbers(expr):
    found = re.findall(r'\d+', expr)
    return list(map(int, found))

def valid_number_usage(expr, allowed_numbers):
    used = extract_numbers(expr)
    return sorted(used) == sorted(allowed_numbers)

def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return None
    
# solver functions
def solve_krypto(nums, target):
    solutions = set()
    
    def helper(numbers, expressions):
        if len(numbers) == 1:
            if abs(numbers[0] - target) < 1e-6:
                solutions.add(expressions[0])
            return
        
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j:
                    a, b = numbers[i], numbers[j]
                    exp_a, exp_b = expressions[i], expressions[j]
                    
                    remaining_nums = [numbers[k] for k in range(len(numbers)) if k not in (i, j)]
                    remaining_exp = [expressions[k] for k in range(len(numbers)) if k not in (i, j)]
                    
                    results = [
                        (a + b, f"({exp_a} + {exp_b})"),
                        (a - b, f"({exp_a} - {exp_b})"),
                        (a * b, f"({exp_a} * {exp_b})")
                    ]
                    
                    if b != 0:
                        results.append((a / b, f"({exp_a} / {exp_b})"))
                    
                    for val, expr in results:
                        helper(remaining_nums + [val], remaining_exp + [expr])
    
    helper(nums, [str(n) for n in nums])
    return list(solutions)

def classify_difficulty(num_solutions):
    if num_solutions > 20:
        return "Easy"
    elif num_solutions > 5:
        return "Medium"
    elif num_solutions > 1:
        return "Hard"
    elif num_solutions == 1:
        return "Expert"
    else:
        return "No Solution"
    
# puzzle generators

def generate_random_puzzle():
    numbers = random.sample(range(1, 31), 5)
    target = random.randint(1, 30)
    return numbers, target

def generate_puzzle_by_difficulty(desired_level, max_tries=200):
    for _ in range(max_tries):
        numbers = random.sample(range(1, 31), 5)
        target = random.randint(1, 30)
        solutions = solve_krypto(numbers, target)
        difficulty = classify_difficulty(len(solutions))

        if difficulty == desired_level:
            return numbers, target

    return numbers, target

def get_daily_puzzle():
    today = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")
    rng = random.Random(today)

    for _ in range(200):
        numbers = rng.sample(range(1, 31), 5)
        target = rng.randint(1, 30)
        solutions = solve_krypto(numbers, target)
        difficulty = classify_difficulty(len(solutions))

        if difficulty in ["Medium", "Hard"]:
            return numbers, target

    return numbers, target

# streamlit app

st.title("🧠 Krypto")
st.caption("Use all 5 numbers exactly once with +, -, *, / to solve the equation.")

mode = st.radio("Choose a mode:", ["Daily Puzzle", "Unlimited Play"])

if mode == "Unlimited Play":
    level = st.selectbox("Choose a level:", ["Easy", "Medium", "Hard", "Expert"])
else:
    level = None

if "show_solution" not in st.session_state:
    st.session_state.show_solution = False

if "unlimited_puzzle" not in st.session_state:
    st.session_state.unlimited_puzzle = generate_puzzle_by_difficulty("Easy")

if "current_level" not in st.session_state:
    st.session_state.current_level = "Easy"

if mode == "Daily Puzzle":
    numbers, target = get_daily_puzzle()
    st.subheader("Daily Puzzle")
else:
    if st.session_state.current_level != level:
        st.session_state.current_level = level
        st.session_state.unlimited_puzzle = generate_puzzle_by_difficulty(level)
        st.session_state.show_solution = False

    numbers, target = st.session_state.unlimited_puzzle
    st.subheader("Unlimited Play")

solutions = solve_krypto(numbers, target)
difficulty = classify_difficulty(len(solutions))

st.write(f"**Numbers:** {numbers}")
st.write(f"**Target:** {target}")
st.write(f"**Difficulty:** {difficulty}")

user_input = st.text_input("Enter your expression:")

if st.button("Check Answer"):
    if not user_input:
        st.warning("Please enter an expression.")
    elif not valid_number_usage(user_input, numbers):
        st.error("You must use each of the 5 numbers exactly once.")
    else:
        result = safe_eval(user_input)
        if result is None:
            st.error("Invalid expression.")
        elif abs(result - target) < 1e-6:
            st.success(f"🎉 Correct! You solved it!")
            st.balloons()
        else:
            st.error(f"Not quite — your expression evaluates to {result}.")


if st.button("Show Solution"):
    st.session_state.show_solution = True
if st.session_state.show_solution:
    if solutions:
        st.write("Example solution:", solutions[0])
    else:
        st.write("No solution found.")

if mode == "Unlimited Play":
    if st.button("Next Puzzle"):
        st.session_state.unlimited_puzzle = generate_puzzle_by_difficulty()
        st.session_state.show_solution = False
        st.rerun()