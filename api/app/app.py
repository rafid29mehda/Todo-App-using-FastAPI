from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=['Rafid Todo App'])
async def root() -> dict:
    return{"Ping": "Pong"}


# Get -> Read the task of Todo
@app.get('/todo', tags=['Tasks for Today'])
async def get_todo() -> dict:
    return{"data": todos}


# Post -> Create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data": "A task has been added!"
    }
    
# Put -. Update Todo
@app.put("/todo/{id}", tags=['Update the List'])
async def update_todo(id: int,body: dict) -> dict:
    for todo in todos:
        if int((todo['id']))==id:
            todo['Activity']=body['Activity']
            return{
                "data": f"Todo with id {id} has been updated."
            }
        return{
            "data":f"Todo with the id {id} was not found!"
        }


# Delete -> Delete Todo
@app.delete("/todo/{id}", tags=["Remove Completed Activity"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return{
                "data": f"todo with id {id} has been deleted"
            }
        return{
            "data": f"todo with id {id} wasn't found!"
        }








todos = [
    {
        "id": "1",
        "Activity": "Submitting intern report before deadline."
    },
    {
        "id": "2",
        "Activity": "Get prepared for the intern presentation."
    }
] 