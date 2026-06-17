# Educational Practice Mini-Project

This repository is for the Educational Practice project.

## Team Information

Academic group:IT-2504

Team name:Batys

Project track:WEB CRUD
- Web CRUD / Machine Learning / Deep Learning

Project topic:Task manager

## Team Members

| No. | Full Name | Role / Contribution |
|---|---|---|
| 1 | Abdysadykov Daniyar |Team leader|
| 2 | Nurali Amangeldi | Member |
| 3 | Aidynuly Makhambet |Member |
| 4 |  -| - |

## Project Description

The Centralized Task Manager Board is a lightweight, high-performance web application engineered to streamline workload tracking and optimize task management within academic and team settings. Developed as an educational practice project for the IT-2504 cohort, the system replaces fragmented communication methods with a unified, interactive kanban-style dashboard where tasks can be systematically initialized, monitored, and modified in real time.

The application is built on a production-grade, asynchronous architecture powered by FastAPI (Python 3.11+) to handle concurrent user operations effectively without thread-locking or performance delays. Data persistence is managed via a relational PostgreSQL 15 backend database, utilizing SQLAlchemy 2.0 ORM for secure database operations and Pydantic for live data-type validation.

Core System Capabilities:
Asynchronous CRUD Operations: Users can create, read, update, and delete tasks featuring strict data constraints (atomic integer primary keys, non-nullable titles, optional descriptions, and explicit due dates).

Dynamic Lifecycle Management: Tasks transition through explicit progress states (Pending, In Progress, and Completed) rendered cleanly via a responsive Bootstrap 5 frontend and Jinja2 template engine.

Efficient Lookups and Filtration: The dashboard supports case-insensitive partial text searching (using SQL ILIKE operations) and quick status filtering to find specific records instantaneously without full page reloads.

Containerized Deployment: The web server and database are isolated into repeatable microservices using Docker and Docker-Compose, eliminating configuration conflicts across different development machines.

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

## Demo Video

Paste demo video link here.

## Report

The final report must be submitted on Moodle as PDF.
