from pydantic import BaseModel, Delete


class MyModel(BaseModel):
    id: int
    name: str


class MyModelCreate(MyModel):
    id: Delete


m = MyModelCreate(id=1, name='test')
print(m)
print(hasattr(m, 'id'))
