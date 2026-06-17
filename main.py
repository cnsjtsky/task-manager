from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime
import database

app = FastAPI(title="Task Manager Assessment Application")
templates = Jinja2Templates(directory="templates")

# Initialize database tables on startup
@app.on_event("startup")
def startup_event():
    database.init_db()

# Read Route: Renders UI and handles Search/Filter features
@app.get("/", response_class=HTMLResponse)
def index(
    request: Request, 
    search: str = None, 
    status_filter: str = None, 
    db: Session = Depends(database.get_db)
):
    query = db.query(database.Task)
    
    # 1. Search Logic: Filters tasks containing search keyword in title
    if search:
        query = query.filter(database.Task.title.ilike(f"%{search}%"))
        
    # 2. Filter Logic: Filters tasks based on selected completion status
    if status_filter and status_filter != "All":
        query = query.filter(database.Task.status == status_filter)
        
    tasks = query.order_by(database.Task.due_date.asc()).all()
    # Change the return statement at the bottom of your index function to this:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tasks": tasks, "search": search, "status_filter": status_filter}
    )

# Create Route: Add a new task item
@app.post("/tasks/add")
def add_task(
    title: str = Form(...),
    description: str = Form(None),
    due_date: str = Form(...),
    db: Session = Depends(database.get_db)
):
    date_obj = datetime.strptime(due_date, "%Y-%m-%d").date()
    new_task = database.Task(title=title, description=description, due_date=date_obj, status="Pending")
    db.add(new_task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Update Route: Update an existing task's status
@app.post("/tasks/update/{task_id}")
def update_task_status(
    task_id: int, 
    status: str = Form(...), 
    db: Session = Depends(database.get_db)
):
    task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = status
    db.commit()
    return RedirectResponse(url="/", status_code=303)

# Delete Route: Remove an operational task completely
@app.post("/tasks/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)