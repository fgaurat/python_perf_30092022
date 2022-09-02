import sqlite3
from Todo import Todo

class TodoDAO:

    def __init__(self):
        self._con = sqlite3.connect(r"todos.db")


    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, type, value, traceback):
        print("__exit__")
        self._con.close()

    def find_all(self):
        cur = self._con.cursor()
        res = cur.execute("SELECT * FROM tbl_todos")
        for id,title,completed in res.fetchall():
            yield Todo(id,title,completed)


    def save(self,todo:Todo):
        cur = self._con.cursor()
        save = f"INSERT INTO tbl_todos(title,completed) VALUES('{todo.title}',{todo.completed});"
        print(save)
        cur.execute(save)
        self._con.commit()


    def __del__(self):
        self._con.close()