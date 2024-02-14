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
autort_swarm = AutoRTSwarm(agents=agents)

# Run the AutoRTSwarm with the given inputs
autort_swarm.run(
    "There is a bottle on the table.",
    "https://i.imgur.com/2qY9f8U.png",
)


# Run a single agent in the swarm
run_agent = autort_swarm.run_single_agent(
    autort_swarm.agents[0].id,
    (
        "Pick up the bottle and place it on the shelf."
        "https://i.imgur.com/2qY9f8U.png"
    ),
)
