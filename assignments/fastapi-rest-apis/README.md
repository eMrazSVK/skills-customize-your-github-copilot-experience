# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build scalable and performant REST APIs using the FastAPI framework. You'll create a backend service with multiple endpoints, implement proper HTTP methods, handle request/response validation, and understand API best practices.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI and Create Your First Endpoint

#### Description
Set up a new FastAPI project and create a simple API with a basic GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and initialize FastAPI
- Create a GET endpoint at `/` that returns a greeting message
- Run the server using `uvicorn` on localhost:8000
- Be able to test the endpoint in a browser or API client (like Postman or curl)

---

### 🛠️ Task 2: Build a Todo List API with CRUD Operations

#### Description
Extend your API to handle a simple todo list. Implement endpoints for creating, reading, updating, and deleting todos. Use in-memory storage (a Python list or dictionary) for now.

#### Requirements
Completed program should:

- Define a Todo model with `id`, `title`, and `completed` fields
- Implement a GET `/todos` endpoint to retrieve all todos
- Implement a POST `/todos` endpoint to create a new todo
- Implement a PUT `/todos/{id}` endpoint to update a todo
- Implement a DELETE `/todos/{id}` endpoint to delete a todo
- Return appropriate HTTP status codes (200, 201, 204, 404)

---

### 🛠️ Task 3: Add Input Validation and Error Handling

#### Description
Improve your API by validating incoming requests and handling errors gracefully. Use FastAPI's built-in validation and create custom error responses.

#### Requirements
Completed program should:

- Use Pydantic models for request/response validation
- Return a 400 status code if a request is missing required fields
- Return a 404 status code when trying to access a non-existent todo
- Provide meaningful error messages in responses
- Validate that a todo's title is not empty and has a reasonable length (1-200 characters)

---

### 🛠️ Task 4 (Stretch Goal): Add Filtering and Sorting

#### Description
Add query parameters to the GET endpoint to allow filtering and sorting of todos. This demonstrates how to build more sophisticated API features.

#### Requirements
Completed program should:

- Support a query parameter `completed` to filter todos by completion status
- Support a query parameter `sort` to sort by title or by creation order
- Maintain backward compatibility (the endpoint should still work without these parameters)
- Return results in the expected order/filter when parameters are provided
