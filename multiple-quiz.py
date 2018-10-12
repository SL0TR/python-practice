class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_promps = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promps[0], "a"),
    Question(question_promps[1], "c"),
    Question(question_promps[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "out of" + str(len(questions)) + " questions correct")

run_test(questions)
