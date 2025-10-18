# Metaheuristic SAT Solver: Genetic Algorithm & Simulated Annealed

## 🌟 Project Overview

This is an **Artificial Intelligence** project designed to solve the **Boolean Satisfiability Problem (SAT)**, a fundamental problem in computer science. Instead of using complete but time-consuming algorithms (like DPLL), this project utilizes two powerful **metaheuristic search algorithms** to find a satisfying assignment efficiently: the **Genetic Algorithm (GA)** and **Simulated Annealing (SA)**.

The objective is to compare how these population-based (GA) and single-state local search (SA) strategies explore the solution space defined by a Conjunctive Normal Form (CNF) expression.

## ⚙️ Algorithms Implemented

| Algorithm | File | Paradigm | Key Mechanism |
| :--- | :--- | :--- | :--- |
| **Genetic Algorithm (GA)** | `SATSolver.py` | Population-Based Search | Evolution, Crossover, Mutation, and Fitness-Based Selection. |
| **Simulated Annealing (SA)** | `algo2.py` | Local Search | Probabilistic acceptance of inferior solutions based on a cooling schedule (simulated temperature). |

### The SAT Problem and Fitness

The problem instance is provided in the **DIMACS CNF format** (`Input.cnf`). A "solution" is a variable assignment (a list of 100 literals) that satisfies the maximum number of clauses.

  * **Fitness Function (`TRUEnumber`):** Measures the number of clauses satisfied by a given variable assignment (individual/state). The goal is to maximize this number up to the total number of clauses.

## 📁 Project Structure

| File | Role |
| :--- | :--- |
| `SATSolver.py` | **Genetic Algorithm Implementation.** Contains the `person` class, GA operators (selection, crossover, mutation), and the main evolution loop. |
| `algo2.py` | **Simulated Annealing Implementation.** Contains the SA logic, including random variable flipping and probabilistic move acceptance. |
| `Input.cnf` | The primary CNF file used for the SAT instance (e.g., 100 variables, 429 clauses). |
| `UInput.cnf` | A supplementary CNF file (used for demonstration or testing). |

## 💻 How to Run the Project

1.  **Prerequisites:** Ensure you have **Python 3** and the `pysat` library installed:
    ```bash
    pip install python-sat
    ```
2.  **Run Genetic Algorithm:**
    ```bash
    python SATSolver.py
    ```
3.  **Run Simulated Annealing:**
    ```bash
    python algo2.py
    ```

**Note:** Both algorithms run in an infinite loop (`while(True)`) by design to continuously search for a better solution or a fully satisfying assignment. The code will output the best solution found so far as it attempts to converge.