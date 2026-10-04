# ============================================================
# MAP COLORING CSP
# Real-world application:
# Mobile Network Frequency Allocation
# ============================================================

def map_coloring(graph, frequencies):

    assignment = {}

    def is_valid(tower, frequency):

        for neighbour in graph[tower]:

            if assignment.get(neighbour) == frequency:
                return False

        return True

    def backtrack():

        # All towers assigned
        if len(assignment) == len(graph):
            return True

        # Select an unassigned tower
        unassigned = [
            tower for tower in graph
            if tower not in assignment
        ]

        tower = unassigned[0]

        # Try every available frequency
        for frequency in frequencies:

            if is_valid(tower, frequency):

                assignment[tower] = frequency

                if backtrack():
                    return True

                # Backtrack
                del assignment[tower]

        return False

    if backtrack():
        return assignment

    return None


# ------------------------------------------------------------
# REAL-WORLD DATA
# ------------------------------------------------------------

# Towers connected by interference/coverage relationships
tower_network = {

    "Tower A": ["Tower B", "Tower C"],
    "Tower B": ["Tower A", "Tower C", "Tower D"],
    "Tower C": ["Tower A", "Tower B", "Tower D"],
    "Tower D": ["Tower B", "Tower C"]
}

# Available frequencies
frequencies = [
    "900 MHz",
    "1800 MHz",
    "2100 MHz"
]


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

solution = map_coloring(
    tower_network,
    frequencies
)


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

print("=" * 50)
print("MOBILE NETWORK FREQUENCY ALLOCATION")
print("=" * 50)

if solution:

    for tower, frequency in solution.items():
        print(f"{tower:10} -> {frequency}")

    print("\nResult: Valid frequency allocation")

else:

    print("No valid frequency allocation exists.")