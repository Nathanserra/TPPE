from models import Author

author1 = Author('Brasileiro', 'Brasil', 'São Paulo', 'SP', '123456789', '987654321')


def test_indetifier_completeness():
    assert author1.identifier.completeness() == 0 