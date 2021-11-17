import random
class Quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_true_answer(self, user_answer):
        if user_answer.lower() == self.answer.lower():
            return True
        else:
            return False

    def __str__(self):
        return f"{self.question}? "


class TrueFalse(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def show_choice(self):
        print("1)True\n2)False")

    def check_true_answer(self, user_answer):
        if user_answer.lower() == 'true' or user_answer.lower() == 'false':
            if user_answer.lower() == self.answer.lower():
                return True
            else:
                return False
        else:
            return "wrong format"


class MultipleChoice(Quiz):
    def __init__(self, question, answer, choice_list):
        super().__init__(question, answer)
        self.choice_list = choice_list

    def show_choice(self):
        print("this is multiplechoice question please select true answer from below!")
        for i, j in enumerate(self.choice_list):
            print(i, j)

    def check_true_answer(self, user_answer):
        if user_answer in self.choice_list:

            if user_answer.lower() == self.answer.lower():
                return True
            else:
                return False
        else:
            return "wrong format"


class ShortAnswer(Quiz):
    def __init__(self, question, answer):
        super().__init__(question, answer)

    def show_choice(self):
        print("this is short answer question please enter a short answer for this question")

    def check_true_answer(self, user_answer):
        if len(user_answer) <= 20:
            if user_answer.lower() == self.answer.lower():
                return True
            else:
                return False
        else:
            return "wrong format"


class Score:
    def __init__(self, score):
        self.score = score
        self.status = None

    def check_status(self):
        if self.score > 40:
            self.status = True
            print("You win!")
        else:
            self.status = False
            print("You loose!")

    def __str__(self):
        return f"Your score is {self.score}"

    def __add__(self, other):
        return self.score + other

    def __abs__(self, other):
        return self.score - other

quizes_truefalse = []
q1 = TrueFalse('sana is girl?','true')
q2 = TrueFalse('is water solid?','false')
q3 = TrueFalse('is sam a boy?','true')
q4 = TrueFalse('2+2 = 5?','false')
q5 = TrueFalse('Is Iran an islamic country?','true')

quizes_truefalse.append(q1)
quizes_truefalse.append(q2)
quizes_truefalse.append(q3)
quizes_truefalse.append(q4)
quizes_truefalse.append(q5)

quizes_multiple = []
q6 = MultipleChoice('what temp water is boiling?','100',['100','80','90','110'])
q7 = MultipleChoice('what is Iran captil?','tehran',['tabriz','rasht','tehran','esfahan'])
q8 = MultipleChoice('who is Iran present?','raeisi',['hashemi','raeisi','ahmadi','ruhani'])
q9 = MultipleChoice('how many days are maktab classes?','3',['4','3','5','2'])
q10 = MultipleChoice('how many years late corona?','3',['1','5','2','3'])
quizes_multiple.append(q6)
quizes_multiple.append(q7)
quizes_multiple.append(q8)
quizes_multiple.append(q9)
quizes_multiple.append(q10)

quizes_shortanswer = []
q11 = quizes_shortanswer.append(ShortAnswer('what is french captial?','paris'))
q12 = quizes_shortanswer.append(ShortAnswer('what is Iran captial?','tehran'))
q13 = quizes_shortanswer.append(ShortAnswer('what is turkey captial?','istanbul'))
q14 = quizes_shortanswer.append(ShortAnswer('what is england captial?','london'))
q15 = quizes_shortanswer.append(ShortAnswer('what is armnestan captial?','iravan'))

quizes = []
for i in range(2):
    q = random.choice(quizes_multiple)
    quizes.append(q)
    while q not in quizes:
        q = random.choice(quizes_multiple)
        quizes.append(q)

for i in range(2):
    q = random.choice(quizes_truefalse)
    quizes.append(q)
    while q not in quizes:
        q = random.choice(quizes_truefalse)
        quizes.append(q)
q = random.choice(quizes_shortanswer)
quizes.append(q)
score = 0
correct = 0
wrong = 0
remaining = len(quizes)
for i,j in enumerate(quizes):
    print(j)
    j.show_choice()
    answer = input("enter answer: ")
    if answer:
        if j.check_true_answer(answer):
            print("Corroct answer!")
            s1 = Score(score)
            score = s1.__add__(10)
            # score += 10
            correct += 1
        else:
            print("Wrong answer!")
            s1 = Score(score)
            score = s1.__abs__(3)
            wrong += 1
    else:
        score = s1.__add__(0)

    print("Q\tCorroct\tWrong\tScore\tRemaining")
    print(f"{i+1}\t\t{correct}\t\t{wrong}\t\t{score}\t\t{4-i}")
# s2 = Score(score)
s1.check_status()
