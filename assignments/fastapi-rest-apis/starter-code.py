"""
Starter code for FastAPI REST APIs assignment.

This file provides the basic structure to get you started. 
Complete the tasks by implementing the required endpoints and models.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# TODO: Define a Pydantic model for Todo items
# Should have: id (int), title (str), completed (bool)


# TODO: Create an in-memory list to store todos
todos = []


# Task 1: Create a simple GET endpoint at "/" that returns a welcome message
@app.get("/")
def read_root():
    """Welcome endpoint."""
    # TODO: Return a greeting message
    pass


# Task 2: Implement CRUD endpoints for todos
@app.get("/todos")
def get_todos():
    """Retrieve all todos."""
    # TODO: Return the list of todos
    pass


@app.post("/todos")
def create_todo(todo):
    """Create a new todo."""
    # TODO: Add the todo to the list and return it
    pass


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo):
    """Update an existing todo by ID."""
    # TODO: Find the todo by ID, update it, and return it
    # Should return 404 if not found
    pass


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a todo by ID."""
    # TODO: Find and delete the todo by ID
    # Should return 404 if not found
    pass


# Task 4 (Optional): Add query parameters for filtering and sorting
@app.get("/todos/filtered")
def get_todos_filtered(completed: Optional[bool] = None, sort: Optional[str] = None):
    """Retrieve todos with optional filtering and sorting."""
    # TODO: Filter todos by completed status if provided
    # TODO: Sort by title or creation order if requested
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
