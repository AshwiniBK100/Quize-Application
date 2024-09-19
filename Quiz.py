class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
 
    def get_question_text(self):
        return self.question_text
 
    def get_options(self):
        return self.options
 
    def get_correct_answer(self):
        return self.correct_answer
 
 
class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []
 
    def add_question(self, question):
        self.questions.append(question)
 
    def get_title(self):
        return self.title
 
    def get_questions(self):
        return self.questions
 
 
class QuizGenerator:
    quizzes = {}
 
    @staticmethod
    def main():
        while True:
            
            command = print("1.create")
            command = print("2.take")
            command = print("3.exit")
            command = input("enter your choice:")
            
 
            if command.lower() == "1":
                QuizGenerator.create_quiz()
            elif command.lower() == "2":
                QuizGenerator.take_quiz()
            elif command.lower() == "3":
                break
            else:
                print("Invalid command. Please try again.")
 
    @staticmethod
    def create_quiz():
        title = input("Enter quiz title: ")
        quiz = Quiz(title)
 
        while True:
            question_text = input("Enter question (or type 'done' to finish): ")
            if question_text.lower() == "done":
                break
 
            options = []
            for i in range(4):
                option = input(f"Enter option {i + 1}: ")
                options.append(option)
 
            correct_answer = input("Enter correct answer: ")
            quiz.add_question(Question(question_text, options, correct_answer))
 
        QuizGenerator.quizzes[title] = quiz
        print("Quiz created successfully!")
 
    @staticmethod
    def take_quiz():
        title = input("Enter quiz title to take: ")
        quiz = QuizGenerator.quizzes.get(title)
 
        if quiz is None:
            print("Quiz not found.")
            return
 
        score = 0
        for question in quiz.get_questions():
            print(question.get_question_text())
            for i, option in enumerate(question.get_options()):
                print(f"{i + 1}. {option}")
 
            answer_index = int(input("Your answer: ")) - 1
 
            if question.get_options()[answer_index] == question.get_correct_answer():
                score += 1
 
        print(f"Your score: {score}/{len(quiz.get_questions())}")
 
 
if __name__ == "__main__":
    QuizGenerator.main()