from app.digest import DigestService

def test_generate_digest():
    service = DigestService()
    result = service.generate()
    assert isinstance(result, str)
    assert "URGENT" in result