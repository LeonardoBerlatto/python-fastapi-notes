# 🗒️ python-fastapi-notes

Notes API made with Python to learn about FastAPI

## :book: About

This repo consists in one python API with CRUD methods to handle notes like this:

```json
{
"title":"A Note",
"description":"I guess I'm not that creative"
}
```

## ▶ Running the project 
1. Download dependencies
```bash
pip intall -r requirements.txt
```
2. Run with uvicorn
```bash
uvicorn api:app:app --reload
```

***Or you can also run with docker*** <br>
3. Run using docker-compose
```bash
docker-compose up
```

## :crystal_ball: Technologies
### Python
* FastAPI
* Pydantic
* PythonDI
### NoSQL Database
* MongoDB
