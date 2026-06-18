from fastapi import APIRouter, HTTPException
from database.agent_db import AgentDB
from pydantic import BaseModel
from typing import Literal

router = APIRouter(prefix= "/agent")

db = AgentDB()

class AgentSchema(BaseModel):
    name : str
    specialty : str
    agent_rank : Literal['Junior', 'Senior', 'Commander']

@router.post("/", status_code= 201)
def create_agent(agent_data: AgentSchema):
    insteret_id = db.create_agent(agent_data)
    if not insteret_id:
        raise HTTPException(status_code=500, detail= "failed to create agent")
    return {"success": True, "agent_id": insteret_id}

@router.get("/")
def get_all_agents():
    all_agents = db.get_all_agents()
    if not all_agents:
        raise HTTPException(status_code=500, detail= "failed to get all books")
    return all_agents

@router.get("/{id}")
def get_agent(id:int):
    agent = db.get_agent_by_id(id)
    if not agent:
        raise HTTPException(status_code= 404, detail= f"agent with id {id} not found")
    return agent

@router.put("/{id}")
def update_agent(details:AgentSchema, id: int):
    agent = db.update_agent(details, id)
    if not agent:
        return HTTPException(status_code= 404, detail= f"agent with id {id} not found")
    return {"success": True }

@router.put("/{id}/deactivate")
def deactivate_agent(id:int):
    deacivate = db.deactivate_agent(id)
    if not deacivate:
        raise HTTPException(status_code= 404, detail= f"agent with id {id} not found as activate")
    return {"success": True }


