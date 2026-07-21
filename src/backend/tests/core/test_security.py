from app.core.security import hash_password, verify_password


def test_hash_password_does_not_return_the_plaintext():
    hashed = hash_password("supersecret")
    assert hashed != "supersecret"


def test_verify_password_accepts_the_correct_password():
    hashed = hash_password("supersecret")
    assert verify_password("supersecret", hashed) is True


def test_verify_password_rejects_the_wrong_password():
    hashed = hash_password("supersecret")
    assert verify_password("wrong-password", hashed) is False


def test_hash_password_is_salted_and_nondeterministic():
    assert hash_password("supersecret") != hash_password("supersecret")
