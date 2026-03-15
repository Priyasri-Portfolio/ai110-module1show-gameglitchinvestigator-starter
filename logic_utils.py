def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """Compare guess to secret and return an outcome string.

    Outcome values:
    - "Win" when guess equals secret
    - "Too High" when guess is greater than secret
    - "Too Low" when guess is less than secret
    """

    if guess == secret:
        return "Win"
    # Fixcorrected reversed hint bug: if guess is greater than secret, it should return "Too High"
    #verified with pytest that the hint is now correct and not reversed
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
