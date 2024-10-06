import pi

def test_pi_digits():
    expected = "314159265358979323846264"
    result = pi.get_pi_digits()
    assert result == expected, f"Expected {expected}, but got {result}"
