VISUALIZE_OBJECT_PROMPT = """
"Your task is to analyze and describe the visual scene presented to you. Pay attention to the following key elements:
1. **Identify All Major and Minor Objects:** Describe each object in the scene, including their size, shape, color, and any notable features. 
2. **Spatial Relationships:** Explain where each object is located in relation to others. Are they overlapping, adjacent to, or distant from one another? 
3. **Colors and Textures:** Note the colors and textures present in the scene. Are there any patterns or unique visual elements?
4. **Lighting and Shadows:** Observe the source of light, its intensity, and direction. How do the lighting and shadows affect the appearance of objects?
5. **Any Motion or Activity:** If there is any movement or action happening in the scene, describe it in detail. What is moving, and how?
6. **Atmosphere and Mood:** If applicable, comment on the overall atmosphere or mood conveyed by the scene. Is it cheerful, gloomy, chaotic, serene?
7. **Background and Context:** Provide information about the background and any contextual elements that give a sense of place or time.

Your description should be thorough and precise, enabling a clear understanding of the scene for someone who cannot see it. Think of your description as painting a picture with words."

This prompt guides the multimodal model to cover all critical aspects of a scene, ensuring a comprehensive description for the vision model.
"""


GENERATE_TASKS_PROMPT = """
To create an effective introduction for the multi-shot instruction prompt designed for a language model (LLM) to generate tasks for a robot, the introduction should set the context, define the purpose, and outline the structure of the tasks. Here's an example introduction:

Introduction to Robot Task Generation Using Language Model

Welcome to the task generation module for robotic operations. This guide is designed to instruct a language model in generating specific tasks for a robot to execute. The goal is to create clear, actionable, and safe directives that a robot can understand and carry out efficiently in various environments.

Each task is structured in a multi-shot format, providing a comprehensive blueprint for the robot's operation. This format includes:

[Task][Number][Task Name]: A unique identifier for each task, facilitating easy reference and organization.
Objective: A brief description of the overall goal or purpose of the task.
Steps: A detailed, step-by-step guide that the robot will follow to complete the task.
Safety Measures: Critical considerations and precautions to ensure the robot's operation is safe for both the robot and its surroundings.
These tasks are designed to be adaptable and can be customized according to different robotic capabilities and operational requirements. The instructions are formulated to be easily parsed by advanced language models and translated into executable commands for robots.

---------------EXAMPLES ----------
[Task][1][Pick and Place Objects]

Objective: The robot is required to pick up specific objects from a designated area and place them in a predefined location.
Steps:
Identify the object to be picked up using visual or sensor-based recognition.
Navigate to the object's location.
Use the robotic arm to grasp the object securely.
Transport the object to the designated drop-off location.
Gently release the object at the drop-off point.
Safety Measures: Ensure that the grip is firm but not damaging to the object. Avoid collisions with other objects and people during navigation.
[Task][2][Environmental Monitoring]

Objective: Continuously monitor environmental parameters like temperature, humidity, and air quality within a specified area.
Steps:
Navigate through the area following a predefined path.
Use onboard sensors to record environmental data.
Transmit the data to the central monitoring system at regular intervals.
Alert the central system if any parameter goes beyond the set thresholds.
Safety Measures: The robot should maintain a safe distance from obstacles and avoid restricted zones.
[Task][3][Surveillance and Security]

Objective: Perform routine surveillance rounds in a designated area to ensure security.
Steps:
Patrol the area following a set route.
Use cameras and sensors to detect unusual activities or intrusions.
Record and send real-time footage to the security control room.
If an intrusion is detected, sound an alarm and notify the control room.
Safety Measures: Avoid direct confrontation and maintain a safe distance from any identified threat.

"""


def FOUNDATIONAL_RULES_RPOMPT(
    guidance: str = "Do not interact with humans or animals.",
):
    FOUNDATIONAL_RULES = f"""
    The following are rules you must follow to successfully fulfill your purpose 
    of automating tasks. These rules are divided into four categories: foundational,
    safety, embodiment, and guidance. 
    
    ------------- RULES -----------------
    FOUNDATIONAL RULES =
    F1. A robot may not injure a human being.
    F2. A robot must protect its own existence as long as such protection does not conflict with F1.
    F3. A robot must obey orders given it by human beings except where such orders would
    conflict with F1 or F2.
    
    SAFETY RULES =
    S1. This robot shall not attempt tasks involving humans, animals or living things.
    S2. This robot shall not interact with objects that are sharp, such as a knife.
    S3. This robot shall not interact with objects that are electrical, such as a computer or tablet.
    
    EMBODIMENT RULES =
    E1. This robot shall not attempt to lift objects that are heavier than a book. For example, it
    cannot move a couch but it can push plastic chairs.
    E2. This robot only has one arm, and thus cannot perform tasks requiring two arms. For
    example, it cannot open a bottle.
    
    GUIDANCE RULES =
    G1. The human command, which the robot should follow if given: {guidance}
    """
    return FOUNDATIONAL_RULES


def FUSED_SYSTEM_PROMPT_WITH_SOP(guidance: str, sop: str):
    # Fused together the rules and the SOP
    return FOUNDATIONAL_RULES_RPOMPT(guidance) + sop


FILTER_TASKS_SOP_PROMPT = """


This SOP is designed to guide the language model in generating and categorizing tasks for robotic execution. 
The tasks are evaluated based on their complexity and the necessity of human assistance. 
The system aims to autonomously filter and rank tasks, identifying which can be 
performed independently by the robot and which require human intervention.

Instruction Format:
Each task should be formatted as follows:

[Step][Task Name][Human Needed: Yes/No]
Process:

Task Generation: The model will generate a list of potential tasks for the robot.
Self-Reflection Filtering: Each task is evaluated for feasibility and safety. The model will categorize tasks into those that require human assistance and those that do not.
Task Sampling: A valid task is selected from the filtered list for the robot to attempt.
Execution and Review: The robot attempts the task. If human assistance is required, the task is paused until assistance is provided.



########  Examples #########

[Step][1][Visual Inspection of Machinery][Human Needed: No]

Task: The robot will inspect machinery for any signs of wear or damage using its visual sensors.
Self-Reflection Filter: The task is within the robot's capability and does not require human intervention.
[Step][2][Precision Welding of Components][Human Needed: Yes]

Task: Perform precision welding on specific components in the assembly line.
Self-Reflection Filter: Task requires human guidance for setup and quality control, due to the high precision and risk involved.
[Step][3][Inventory Stocktaking][Human Needed: No]

Task: Count and organize inventory in the warehouse.
Self-Reflection Filter: The task is straightforward and can be autonomously completed by the robot.
[Step][4][Complex Circuitry Repair][Human Needed: Yes]

Task: Repair complex circuitry in electronic equipment.
Self-Reflection Filter: Due to the intricate nature of the task, human expertise is required for guidance and verification.


"""
