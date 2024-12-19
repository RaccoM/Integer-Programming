import numpy as np

# Branch and Bound Algo
def branch_and_bound(revenues, days, max_days):
    n = len(revenues)
    best_revenue = 0
    best_solution = [0] * n

    # Stack to manage branches
    stack = [{"solution": [0] * n, "level": 0, "current_revenue": 0, "current_days": 0}]

    while stack:
        # Pop a branch
        node = stack.pop()
        solution = node["solution"]
        level = node["level"]
        current_revenue = node["current_revenue"]
        current_days = node["current_days"]

        # Check if the solution is the best
        if level == n:
            if current_revenue > best_revenue:
                best_revenue = current_revenue
                best_solution = solution[:]
            continue

        # Branch 1: Do not include the project
        stack.append({
            "solution": solution[:],
            "level": level + 1,
            "current_revenue": current_revenue,
            "current_days": current_days
        })

        # Branch 2: Include the project
        if current_days + days[level] <= max_days:
            new_solution = solution[:]
            new_solution[level] = 1 
            stack.append({
                "solution": new_solution,
                "level": level + 1,
                "current_revenue": current_revenue + revenues[level],
                "current_days": current_days + days[level]
            })

    return best_revenue, best_solution

# Example
revenues = [30, 20, 5, 25, 22, 17, 60]
days = [20, 28, 13, 60, 37, 10, 85]
max_days = 100

best_revenue, best_solution = branch_and_bound(revenues, days, max_days)

print("Best Revenue:", best_revenue)
print("Best Solution:", best_solution)
