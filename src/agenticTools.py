from agents import Agent
from src.geminiModel import gemini_model
from src.projectFunctions import arithmetic_tool

instructions1 = "You are a math tutor agent that helps students understand and solve mathematical problems. \
You provide clear explanations and step-by-step solutions to help students learn. \
You can handle all types of math problems. \
You use the arithmetic_tool for performing basic calculations to ensure accuracy. \
You always show your work and explain your reasoning."

instructions2 = "You are a knowledgeable physics tutor agent that helps students understand and solve physics problems. \
You provide clear explanations and step-by-step solutions to help students learn. \
You can handle all types of physics problems. \
You always show your work, explain your reasoning, and use relevant formulas and equations."





math_tutor_agent = Agent(
        name="Math Tutor Agent",
        instructions=instructions1,
        model=gemini_model,
        tools=[arithmetic_tool]
)

physics_tutor_agent = Agent(
        name="Physics Tutor Agent",
        instructions=instructions2,
        model=gemini_model
)





description = "Solve a math problem"
description2 = "Solve a physics problem"

tool1math = math_tutor_agent.as_tool(tool_name="math_tutor_agent", tool_description=description)
tool2physics = physics_tutor_agent.as_tool(tool_name="physics_tutor_agent", tool_description=description2)
