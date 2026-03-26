from app.digest import generate_digest

def test_generate_digest():
    result = generate_digest()
    assert isinstance(result, str)
    assert "URGENT" in result