````md
# Meeting Notes Summariser API

A small beginner project built while learning FastAPI and REST APIs.  
This API takes raw meeting notes and uses Ollama with the Llama 3.2 model to generate a short summary and important discussion points.

## Features

- Built with FastAPI
- Uses Ollama locally
- Summarises meeting notes
- Extracts important action points

## Tech Stack

- Python
- FastAPI
- Pydantic
- Ollama
- Llama 3.2

## How to Run

1. Install dependencies

``` 
pip install fastapi uvicorn ollama
````

2. Make sure Ollama is installed and running

Pull the model:

``` 
ollama pull llama3.2
```

3. Start the API

``` 
uvicorn main:app --reload
```

## API Endpoint

### POST `/summarise`

Example request:

```json
{
  "notes": "John will fix the login bug, Sara will update frontend by Friday."
}
```

## What I Learned

* Creating APIs with FastAPI
* Using POST requests
* Request validation with Pydantic
* Connecting AI models with APIs
* Basic REST API structure

## Note

This is a simple learning project and still a work in progress while I learn FastAPI and REST APIs.

```
```
