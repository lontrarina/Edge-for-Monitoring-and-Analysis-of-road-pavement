from app.entities.agent_data import AgentData
from app.entities.processed_agent_data import ProcessedAgentData

def process_agent_data(agent_data: AgentData) -> ProcessedAgentData:
    """
    Process agent data and classify the state of the road surface.
    Parameters:
        agent_data (AgentData): Agent data that containing accelerometer, GPS, and timestamp.
    Returns:
        processed_data_batch (ProcessedAgentData): Processed data containing the classified state of the road surface and agent data.
    """
    try:
        # Define thresholds for different road conditions
        normal_threshold = 500
        cracks_threshold = 0

        # Determine the road state based on accelerometer data
        if agent_data.accelerometer.x > normal_threshold:
            road_state = "normal condition"
        elif cracks_threshold < agent_data.accelerometer.x <= normal_threshold:
            road_state = "cracks"
        else:
            road_state = "potholes"

        # Create and return a ProcessedAgentData object
        processed_data = ProcessedAgentData(road_state=road_state, agent_data=agent_data)
        return processed_data
    except Exception as e:
        print(f"Error processing agent data: {e}")
        return None



