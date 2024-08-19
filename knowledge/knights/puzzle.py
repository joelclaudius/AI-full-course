from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can either be a Knight or a knave, but not both
    Or(AKnight, AKnave),

    # If A is a Knight, then the statement "I am both a Knight and a knave" must be true
    Implication(AKnight, And(AKnight, AKnave)),

    # If A is a knave, then the statement "I am neither a Knight nor a knave" must be false
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can either be a knight or a knave, but not both
    Or(AKnight, AKnave),

    # B can either be a knight or a knave, but not both.
    Or(BKnight, BKnave),

    # If A is a knight, then the statement "We are both knaves" should be true.
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a knave, then the statement "We are both knaves" should be false.
    Implication(AKnave, Not(And(AKnave, BKnave))),


)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A says "We are the same kind"
    Biconditional(AKnight, Biconditional(AKnight, BKnight)),   # A is a knight and A and B are the same kind
    Biconditional(AKnave, Not(Biconditional(AKnight, BKnight))),  # A is a knave and A and B are different kinds

    # B says "We are of different kinds"
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  # B is a knight and A and B are different kinds
    Implication(BKnave, Biconditional(AKnight, BKnight))   
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A says either "I am a knight" or "I am a knave"
    Or(
        Biconditional(AKnight, AKnight),  # If A is a knight, A says "I am a knight" is true
        Biconditional(AKnave, AKnave)     # If A is a knave, A says "I am a knave" is true
    ),
    And(
        Not(And(AKnight, AKnave))  # A cannot be both a knight and a knave
    ),
    
    # B says "A said 'I am a knave'."
    Implication(BKnight, Biconditional(AKnave, AKnave)),  # If B is a knight, B says "A said 'I am a knave'"
    Implication(BKnave, Not(Biconditional(AKnave, AKnave))),  # If B is a knave, B is lying about A's statement

    # B says "C is a knave."
    Implication(BKnight, CKnave),  # If B is a knight, C is a knave
    Implication(BKnave, CKnight),  # If B is a knave, C is a knight

    # C says "A is a knight."
    Implication(CKnight, AKnight),  # If C is a knight, A is a knight
    Implication(CKnave, Not(AKnight))  # If C is a knave, A is not a knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
