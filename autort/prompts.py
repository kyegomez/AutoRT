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