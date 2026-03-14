from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting the high/low string-comparison bug ---
# On even attempts, app.py passed secret as a str instead of int.
# The old code fell back to lexicographic comparison, so e.g.
# "9" > "10" even though 9 < 10, producing the wrong hint.
#TESTS BELOW TARGET THE FIX FOR THIS BUG. ALL MUST PASS.
def test_string_secret_too_low():
    # 9 < 10 numerically, but "9" > "10" lexicographically.
    # The fix must return "Too Low", not "Too High".
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too Low"

def test_string_secret_too_high():
    # 20 > 9 numerically, but "20" < "9" lexicographically.
    # The fix must return "Too High", not "Too Low".
    outcome, _ = check_guess(20, "9")
    assert outcome == "Too High"

def test_string_secret_win():
    # Winning when secret is passed as a string should still work.
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"
