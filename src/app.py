from agents import Agent, Runner, trace
import asyncio
from src.geminiModel import gemini_model
from src.agenticTools import tool1math, tool2physics

tools = [tool1math, tool2physics]

instructions = "You are a tutor  agent that helps students with math and physics questions. \
You use the provided tools to solve problems and provide detailed explanations. You never solve the problems yourself, you always use the tools. \
For math questions, you use the tool1math tool which can perform calculations and provide step-by-step solutions. \
For physics questions, you use the tool2physics tool which can solve physics problems using relevant formulas and equations. \
You always show your work, explain your reasoning, and ensure students understand the concepts being taught."


tutor_manager = Agent(
    name="Tutor Manager", 
    instructions=instructions, 
    tools=tools, 
    model=gemini_model
    )

async def tutor_managerr(message="Solve the following math problem: 2 + 2", history=None):
    message = ("chat history : \n" +  str(history) + "\n" + "user message : \n" + message)
    with trace("Tutor manager"):
        result = await Runner.run(tutor_manager, message)
        return result.final_output

if __name__ == "__main__":
    print(instructions)
    asyncio.run(tutor_managerr())
