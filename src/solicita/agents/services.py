from agents.schemas import AgentIn, AgentOut
from agents.order_agents import order_agent

class AgentServices:

    @staticmethod
    async def extract_order(self, agentIn : AgentIn):

        result = await order_agent.run(
            user_prompt=agentIn.mensage,
            output_type= AgentOut
        )

        return result.output