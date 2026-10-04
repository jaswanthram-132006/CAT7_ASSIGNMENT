# ============================================================
# LOCAL SEARCH FOR CSP
#
# Real-world application:
# Hospital Doctor Shift Scheduling
#
# Algorithm:
# Min-Conflicts Local Search
# ============================================================

import random


def local_search(
    doctors,
    shifts,
    conflicts,
    max_steps=10000
):

    # --------------------------------------------------------
    # Create neighbour relationship
    # --------------------------------------------------------

    neighbours = {
        doctor: set()
        for doctor in doctors
    }

    for doctor1, doctor2 in conflicts:

        neighbours[doctor1].add(doctor2)
        neighbours[doctor2].add(doctor1)

    # --------------------------------------------------------
    # Random initial schedule
    # --------------------------------------------------------

    assignment = {
        doctor: random.choice(shifts)
        for doctor in doctors
    }

    # --------------------------------------------------------
    # Count conflicts
    # --------------------------------------------------------

    def count_conflicts(doctor, shift):

        count = 0

        for neighbour in neighbours[doctor]:

            if assignment.get(neighbour) == shift:
                count += 1

        return count

    # --------------------------------------------------------
    # Min-Conflicts algorithm
    # --------------------------------------------------------

    for step in range(max_steps):

        conflicted_doctors = []

        # Find doctors violating constraints
        for doctor in doctors:

            if count_conflicts(
                doctor,
                assignment[doctor]
            ) > 0:

                conflicted_doctors.append(doctor)

        # No conflicts -> solution found
        if not conflicted_doctors:

            return assignment

        # Select a random conflicted doctor
        doctor = random.choice(
            conflicted_doctors
        )

        # Calculate conflicts for every shift
        conflict_values = {
            shift: count_conflicts(
                doctor,
                shift
            )
            for shift in shifts
        }

        # Find minimum conflict
        minimum = min(
            conflict_values.values()
        )

        best_shifts = [
            shift
            for shift in shifts
            if conflict_values[shift] == minimum
        ]

        # Move doctor to a better shift
        assignment[doctor] = random.choice(
            best_shifts
        )

    # No solution found within step limit
    return None


# ============================================================
# HOSPITAL DATA
# ============================================================

doctors = [
    "Dr. Arun",
    "Dr. Priya",
    "Dr. Ravi",
    "Dr. Meena",
    "Dr. Karthik",
    "Dr. Divya"
]


shifts = [
    "Morning",
    "Afternoon",
    "Night"
]


# Doctors that should not be assigned
# to the same shift
conflicts = [

    ("Dr. Arun", "Dr. Priya"),

    ("Dr. Priya", "Dr. Ravi"),

    ("Dr. Ravi", "Dr. Meena"),

    ("Dr. Meena", "Dr. Karthik"),

    ("Dr. Karthik", "Dr. Divya"),

    ("Dr. Divya", "Dr. Arun")
]


# ============================================================
# SOLVE
# ============================================================

solution = local_search(
    doctors,
    shifts,
    conflicts
)


# ============================================================
# DISPLAY
# ============================================================

print("=" * 55)
print("HOSPITAL DOCTOR SHIFT SCHEDULING")
print("=" * 55)

if solution:

    for doctor, shift in solution.items():

        print(
            f"{doctor:15} -> {shift}"
        )

    print(
        "\nResult: Conflict-free schedule generated."
    )

else:

    print(
        "Could not find a solution."
    )