"""Gives classes our project"""

class Question:
    """Acts like a quesion"""
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer