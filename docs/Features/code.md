## block
```python 
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

## inline
The `range()` function is used to generate a sequence of numbers.

[[docs/Features/Diagrams|Diagrams]]
[Diagrams](Diagrams.md)
[Draw](docs/Features/Draw.md)


