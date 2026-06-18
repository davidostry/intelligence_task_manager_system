from fastapi import APIRouter, HTTPException
from database.mission_db import MissionDB
from database.agent_db import AgentDB
from pydantic import BaseModel


router = APIRouter(prefix= "/mission")

db = MissionDB()

class MissionSchema(BaseModel):
    title : str
    description : str
    location : str
    difficulty : int
    importance : int

@router.post("/", status_code=201)
def create_mission(data:MissionSchema):
    insteret_id = db.create_mission(data)
    if not insteret_id:
        raise HTTPException(status_code=500, detail= "failed to create mission")
    return {"success": True, "mission_id": insteret_id}

@router.get("/")
def get_all_missions():
    all_missions = db.get_all_missions()
    if not all_missions:
        raise HTTPException(status_code=500, detail= "failed to get all missions")
    return all_missions

@router.get("/{id}")
def get_mission(id:int):
    mission = db.get_mission_by_id(id)
    if not mission:
        raise HTTPException(status_code= 404, detail= f"mission with id {id} not found")
    return mission

@router.put("/{id}/assign/{agent_id}")
def assign(mission_id, agent_id):
    mission = get_mission(mission_id)
    agent_db = AgentDB()
    agent = agent_db.get_agent_by_id(agent_id)

    if not mission:
        raise HTTPException(status_code=404, detail="mission not found")
    if not agent:
        raise HTTPException(status_code=404, detail="agent not found")
    if mission["status"] != "new":
        raise HTTPException(status_code=400,detail="mission not available")
    if agent["is_active"] == False:
        raise HTTPException(status_code=400, detail= "agent is not active")
    if mission["risk_level"] == "critical" and agent["agent_rank"] != "commander":
        raise HTTPException(status_code=400, detail="only commander can handle critical mission")
