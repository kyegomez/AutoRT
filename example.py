# Import necessary modules
import os
from autort import AutoRTSwarm, AutoRTAgent

# Set the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define a list of AutoRTAgent instances
agents = [
    AutoRTAgent(openai_api_key, max_tokens=1000),
    AutoRTAgent(openai_api_key, max_tokens=1000),
]

# Create an instance of AutoRTSwarm with the agents and datastore
autort_swarm = AutoRTSwarm(agents)

# Run the AutoRTSwarm with the given inputs
autort_swarm.run(
    "There is a bottle on the table.",
    "https://i.imgur.com/2qY9f8U.png",
)
