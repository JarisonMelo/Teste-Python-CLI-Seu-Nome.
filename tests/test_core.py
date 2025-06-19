import pytest
from mathquiz.core import Quiz

def test_quiz_creation():
    """Testa se a criação do Quiz funciona."""
    quiz = Quiz(5, ['+'], 1, 10, False, 2)
    assert quiz.num_questions == 5

def test_invalid_operation():
    """Testa se o Quiz falha com operação inválida."""
    with pytest.raises(ValueError):
        Quiz(5, ['^'], 1, 10, False, 2)
