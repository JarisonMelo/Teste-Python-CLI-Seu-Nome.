import random
import time
from dataclasses import dataclass
from .operations import OPERATIONS

@dataclass
class Question:
    text: str
    answer: float

@dataclass
class QuizResult:
    total_questions: int
    correct_answers: int = 0
    total_time: float = 0.0

    @property
    def incorrect_answers(self):
        return self.total_questions - self.correct_answers

    @property
    def accuracy(self):
        return (self.correct_answers / self.total_questions) * 100 if self.total_questions > 0 else 0

    @property
    def average_time(self):
        return self.total_time / self.total_questions if self.total_questions > 0 else 0

class Quiz:
    def __init__(self, num_questions, operations, min_val, max_val, use_decimals, decimal_places):
        self.num_questions = num_questions
        self.operations = [OPERATIONS[op] for op in operations]
        self.min_val = min_val
        self.max_val = max_val
        self.use_decimals = use_decimals
        self.decimal_places = decimal_places
        self.results = QuizResult(total_questions=num_questions)

    def _generate_question(self):
        op = random.choice(self.operations)
        a = self._generate_operand()
        b = self._generate_operand()
        if op.name == "/" and b == 0: b = 1
        text = f"Quanto é {a} {op.name} {b}?"
        return Question(text, op(a, b))

    def _generate_operand(self):
        num = random.uniform(self.min_val, self.max_val)
        return round(num, self.decimal_places) if self.use_decimals else int(num)

    def run(self):
        start_time = time.time()
        for i in range(self.num_questions):
            question = self._generate_question()
            try:
                user_answer = float(input(f"Questão {i+1}: {question.text} "))
                if abs(user_answer - question.answer) < 1e-9:
                    print("Correto!")
                    self.results.correct_answers += 1
                else:
                    print(f"Incorreto. A resposta era {question.answer}")
            except ValueError:
                print("Entrada inválida.")
        self.results.total_time = time.time() - start_time

    def display_report(self):
        res = self.results
        print(f"\n--- Relatório Final ---\nAcertos: {res.correct_answers}/{res.total_questions} ({res.accuracy:.2f}%)\nTempo total: {res.total_time:.2f}s")
