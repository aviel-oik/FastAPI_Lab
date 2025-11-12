from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id : int
    name : str
    price : float

def load_dada():
    with open("data.json", "r") as j:
        return json.load(j)

def save_data(data):
    with open("data.json", "w") as j:
        json.dump(data, j, indent=4)


@app.get("/")
def read_root():
    return {"Hello": "in my server"}

@app.get("/items/")
def read_all():
    return load_dada()

@app.put("/change_price/{item_id}", response_model=Item)
def change_price(item_id, item : Item):
    data = load_dada()
    for i in data:
        if i["id"] == item_id:
            i["price"] = item["price"]
            save_data(data)
            return i
    raise HTTPException(status_code=404, detail="Item not found")

