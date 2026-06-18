from fastapi import FastAPI
from database.db_connection import DB_connector
from routes.agent_routes import router as agent_router

db = DB_connector()

# db.create_database()

db.create_tables()

app =FastAPI()
app.include_router(agent_router)

