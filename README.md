[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)

# AutoRT
![AutoRTImage](autort.png)
Implementation of AutoRT: "AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents". This repo will implement the multi agent system that transforms a scene into a list of ranked and priortized tasks for an robotic action model to execute. This is an very effective setup that I personally believe is the future for swarming robotic foundation models!

This project will be implemented using Swarms, for the various llms and use the official RT-1 as the robotic action model.

[PAPER LINK](https://auto-rt.github.io/static/pdf/AutoRT.pdf)

## Install
`$ pip3 install autort-swarms`


## Usage

### Setting Up AutoRT

1. Load your environment variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

2. Instantiate the AutoRT class:

```python
from autort import AutoRT

# Load API keys from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Instantiate AutoRT with the necessary API keys
autort_system = AutoRT(openai_api_key)
```

### Running AutoRT

With AutoRT set up, you can now run the system by providing it with text and image inputs:

```python
text_input = "There is a bottle on the table."
image_url = "https://i.imgur.com/2qY9f8U.png"

# Run the AutoRT system
result = autort_system.run(text_input, image_url)
```

### Customizing AutoRT

AutoRT allows for extensive customization of its components. Here’s how you can do it:

#### Customizing Language Model Prompts
AutoRT uses predefined prompts to guide the language models. To customize these prompts:

```python
from autort.prompts import FUSED_SYSTEM_PROMPT_WITH_SOP

custom_visualization_prompt = "Custom SOP for visualizing objects."
autort_system.system_prompt_vllm = FUSED_SYSTEM_PROMPT_WITH_SOP(
    guidance=autort_system.guidance_vllm,
    sop=custom_visualization_prompt,
)
```

#### Customizing Task Generation
You can alter the guidance for task generation to focus on specific types of tasks:

```python
custom_task_generation_guidance = "Generate cleaning tasks for the robot."
autort_system.guidance_llm = custom_task_generation_guidance
```

#### Customizing Task Ranking
To modify the criteria for task ranking:

```python
custom_ranking_guidance = "Rank tasks based on safety and duration."
autort_system.guidance_rank = custom_ranking_guidance
```

#### Customizing the Robot Model
AutoRT can be tailored to work with different robot models by providing a custom callable:

```python
def custom_robot_model(task_descriptions, image):
    # Custom logic to execute tasks
    pass

autort_system.robot_model = custom_robot_model
```

### Running Customized AutoRT
After customization, invoke the `run` method with the new parameters:

```python
# Run the customized AutoRT system
custom_result = autort_system.run(text_input, image_url)
```

### Conclusion
AutoRT offers a flexible and powerful interface to bridge the gap between AI language understanding and robotic task execution. By customizing its components, you can tailor the system to a wide range of applications, from domestic robots to industrial automation systems. With this tutorial, you're now equipped to implement and customize AutoRT for your specific needs.


## Citation
```bibtext
@inproceedings{
    anonymous2023autort,
    title={Auto{RT}: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents},
    author={Anonymous},
    booktitle={Submitted to The Twelfth International Conference on Learning Representations},
    year={2023},
    url={https://openreview.net/forum?id=xVlcbh0poD},
    note={under review}
}

```


# License
MIT



