class Todolist:
    def __init__(self) -> None:
        self.todo_ids = set()
        self.todo_list = {}
    def get_valid_id(self):
        for i , v in enumerate(self.todo_ids,start=1):
            if i != v:
                return i
        return(len(self.todo_ids)+1)
    def add_todo(self , todo_title):
        todo_id = self.get_valid_id()  
        self.todo_list[todo_id] = todo_title
        self.todo_ids.add(todo_id)
    def show_todos(self):
        for todo_id in self.todo_ids:
            print(f"[{todo_id}] {self.todo_list[todo_id]}")  
    def mark_done(self , todo_id):
        self.todo_list.pop(todo_id,None)
        self.todo_ids.discard(todo_id)

if __name__ == "__main__" :
    todo_list = Todolist()
    todo_list.add_todo("Write todo app")
    todo_list.add_todo("Take some time")
    todo_list.add_todo("Dss")
    todo_list.get_valid_id()
    todo_list.show_todos()
    todo_list.mark_done(todo_id=2)
    print("\nmarked 2nd todo as done\n")
    todo_list.show_todos()
