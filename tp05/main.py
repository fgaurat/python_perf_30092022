from Todo import Todo
from TodoDAO import TodoDAO
import httpx
from pprint import pprint


class TheList:

    def __init__(self):
        self._data = [d for d in range(100)]


    # @property
    # def data(self):
    #     return self._data

    @property
    def data(self):
        print('start')
        for i in self._data: 
            yield i
        print('end')

def main():

    with TodoDAO() as dao:
        todos = list(dao.find_all())
        
        for todo in todos[:3]:
            print(todo)
    print("la fin")
def main03():
    dao = TodoDAO()
    todos = dao.find_all()

    for todo in todos:
        print(todo)
def main03():
    dao = TodoDAO()
    todos = dao.find_all()

    for todo in todos:
        print(todo)

def main02():
    r = httpx.get('https://jsonplaceholder.typicode.com/todos')
    data = r.json()
    pprint(data)
    dao = TodoDAO()
    for todo in data:
        del todo['id'],todo['userId']
        todo_tosave = Todo(**todo)
        print(todo_tosave)
        dao.save(todo_tosave)


        

def main01():
    t = TheList()


    l = list(t.data)
    # for i in t.data:
    #     print(i)
    print(l)
if __name__ == '__main__':
    main()