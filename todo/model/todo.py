class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title 
        self.description: str = description
        self.completed: bool = False 
        self.tags: list = []


    def mark_completed (self):
        self.completed: str = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"
    

class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo]= {}
    
    def add_todo(self, title: str, description:str) -> int:
        new_id = len(self.todos) + 1
        new_todo = Todo(new_id, title, description)
        self.todos[new_id] = new_todo
        return new_id 
        

    

        

    
