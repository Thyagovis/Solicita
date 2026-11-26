from fastapi import APIRouter

from agents.schemas import AgentIn
from agents.services import AgentServices

router = APIRouter(prefix= "/api/v1/extract")

@router.post("/")
async def extract_order(agentIn : AgentIn):

    return await AgentServices.extract_order(agentIn)