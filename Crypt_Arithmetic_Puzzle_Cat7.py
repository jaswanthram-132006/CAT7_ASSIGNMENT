# ============================================================
# CRYPT-ARITHMETIC CSP
#
# Problem:
# SEND + MORE = MONEY
#
# Each letter represents a unique digit.
# ============================================================

from itertools import permutations


def solve_cryptarithm():

    letters = "SENDMORY"

    # Leading letters cannot be zero
    for digits in permutations(range(10), len(letters)):

        mapping = dict(zip(letters, digits))

        if mapping["S"] == 0:
            continue

        if mapping["M"] == 0:
            continue

        SEND = (
            1000 * mapping["S"]
            + 100 * mapping["E"]
            + 10 * mapping["N"]
            + mapping["D"]
        )

        MORE = (
            1000 * mapping["M"]
            + 100 * mapping["O"]
            + 10 * mapping["R"]
            + mapping["E"]
        )

        MONEY = (
            10000 * mapping["M"]
            + 1000 * mapping["O"]
            + 100 * mapping["N"]
            + 10 * mapping["E"]
            + mapping["Y"]
        )

        if SEND + MORE == MONEY:

            return mapping, SEND, MORE, MONEY

    return None


# ------------------------------------------------------------
# SOLVE
# ------------------------------------------------------------

solution = solve_cryptarithm()


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

print("=" * 50)
print("CRYPT-ARITHMETIC CSP")
print("=" * 50)

if solution:

    mapping, SEND, MORE, MONEY = solution

    print("\nLetter -> Digit")

    for letter in sorted(mapping):
        print(
            f"{letter} -> {mapping[letter]}"
        )

    print("\nVerification:")
    print(
        f"{SEND} + {MORE} = {MONEY}"
    )

    print("\nResult: Puzzle solved successfully")

else:

    print("No solution exists.")