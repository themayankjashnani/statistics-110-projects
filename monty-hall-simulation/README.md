# Monty Hall Simulation 🚪🎯

This simulation solves the famous **Monty Hall Problem** using Python and Monte Carlo trials. It answers:
> "If you’re shown 3 doors, one with a car and two with goats — should you switch after the host reveals a goat?"

## 🔍 Problem Setup

- 3 doors: 1 car, 2 goats
- Contestant picks 1 door
- Host (who knows) opens 1 of the remaining **goat** doors
- Contestant chooses whether to **stay** or **switch**

## 🧪 Simulation

We ran `1,000,000` trials using Python. The results:

| Strategy | Win Rate |
|----------|----------|
| ✅ Switch | ~66.7%   |
| ❌ Stay   | ~33.3%   |

## 📊 Visualization

![Simulation Result](./result.png)

## 💻 Code

Check out `montyhall_problem.py` for the full implementation. Uses `random` and `matplotlib`.

---

> Part of my `statistics-110-projects` collection based on the Harvard Statistics 110 course by Prof. Joe Blitzstein.
