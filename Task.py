class Task:
    def __init__(self, explanation):
        self.is_completed = False
        self.explanation = explanation

    def to_dict(self):
        return {
            "explanation": self.explanation,
            "is_completed": self.is_completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["explanation"])
        task.is_completed = data["is_completed"]
        return task