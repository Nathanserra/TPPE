from models import Author

author1 = Author('Brasil', 'Brasil', 'São Paulo', 'SP', '123456789', '987654321')
author2 = Author('Brasil', 'Brasil', 'São Paulo', 'SP', '', '987654321')
author3 = Author('Brasil', 'Brasil', 'São Paulo', 'SP', '', '')
author4 = Author('Brasil', 'Brasil', 'São Paulo', 'SP', '123456789', '')

author5 = Author('', '', '', 'SP', '123456789', '987654321')
author6 = Author('Brasil', '', '', 'SP', '', '987654321')


def test_indetifier_completeness():
    assert author1.identifier.completeness() == 0 
    assert author2.identifier.completeness() == 1
    assert author3.identifier.completeness() == 0
    assert author4.identifier.completeness() == 1

def test_author_completeness():
    assert author1.completeness() == 0.5
    assert author2.completeness() == 1
    assert author3.completeness() == 0.5
    assert author4.completeness() == 1
    assert author5.completeness() == 0.125
    assert author6.completeness() == 0.75