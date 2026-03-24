# Krypto Puzzle Solver & Difficulty Engine  

## 🧠 Overview  

This project implements a computational engine for solving and analyzing **Krypto-style arithmetic puzzles**, where the goal is to combine five numbers using basic operations (+, −, ×, ÷) to reach a target value.

Beyond solving puzzles, this project focuses on **quantifying puzzle difficulty** using algorithmic and data-driven methods. The system explores the structure of the solution space to evaluate how challenging a puzzle is, making it a blend of:

- Combinatorics  
- Search algorithms  
- Optimization  
- Data analysis  

---

## 🎯 Problem  

Given:
- 5 numbers (1–30)  
- 1 target number (1–30)  

Use each number exactly once with arithmetic operations to reach the target.

Example:
7, 11, 18, 23, 29 → Target: 15

---

## ⚙️ Core Features  

### 🔍 Puzzle Solver  
- Exhaustively searches all valid arithmetic expressions  
- Uses recursive backtracking to explore combinations  
- Ensures each number is used exactly once  
- Returns all valid solutions  

---

### 📊 Difficulty Engine  
Each puzzle is scored based on properties of its solution space:

- Number of valid solutions  
- Depth and complexity of solution paths  
- Presence of misleading intermediate states  

Difficulty levels:
- **Easy** → many solutions  
- **Medium** → moderate solutions  
- **Hard** → few solutions  
- **Expert** → unique or highly constrained solutions  

---

### 📈 Data Analysis  
- Generates and analyzes large sets of puzzles  
- Studies distribution of difficulty levels  
- Evaluates how puzzle structure impacts solvability  
- Identifies patterns in solution complexity  

---

### 🧪 Experimental Extensions (Planned)  
- Simulated player strategies (random vs optimal)  
- Solve time estimation models  
- Adaptive difficulty tuning using performance data  

---

## 🛠️ Tech Stack  

- Python  
- NumPy  
- pandas  
- Jupyter Notebook  

---

## 🧮 Algorithmic Approach  

The solver is based on:

- Recursive search (backtracking)  
- Permutation of number orderings  
- Enumeration of operator combinations  
- Pruning invalid or redundant states  

This approach ensures full coverage of the solution space while maintaining computational efficiency.

---

## 📊 Example Output  

Input: [4, 11, 17, 23, 29], Target = 18

Example Solution:
4 * (17 - 11) - (29 - 23) = 18

Difficulty: Medium

---

## 🚀 Future Work  

- Web-based interface for interactive gameplay  
- Daily puzzle generation system  
- Leaderboards and competitive modes  
- Deployment as a web application  
- Integration of machine learning for difficulty prediction  

---

## 💡 Motivation  

This project combines mathematics, algorithms, and data science to explore how problem structure affects human solvability.

It is inspired by competitive puzzle games like Krypto and Wordle, with a focus on building a scalable system that can generate, evaluate, and adapt puzzles dynamically.

---

## 📌 Author  

Lily Kinney  
M.S. Data Science | Applied Mathematics  
