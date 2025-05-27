import os
from typing_extensions import Unpack
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from lab45_autogen_extension.lab45aiplatform_autogen_extension import Lab45AIPlatformCompletionClient
from lab45_autogen_extension.utils import Lab45AIPlatformStateStoreConfiguration
from config import CONFIG_DATA

BASE_URL = os.getenv("API_BASE_URL") or CONFIG_DATA.get("api_base_url")

async def _get_model_client(api_key):

    # Initialize LAIP extension model client

    lab45_client = Lab45AIPlatformCompletionClient(
        model_name='gpt-4o',
        base_url=BASE_URL,
        api_key=api_key, 
        enable_state_storage=True  # enable this in order to save and load states to the extension sqlite DB
    )
    return lab45_client

async def _load_team_state(team, lab45_client, tenant_id, session_id, user_id):
    # Load team state from sqlite 
    state = lab45_client.load_state(tenant_id=tenant_id, session_id=session_id, user_id=user_id)
    if state: 
        await team.load_state(state)
    
    return team

async def _save_team_state(team, lab45_client, tenant_id, session_id, user_id):
    # Save team state to sqlite 
    state = await team.save_state()
    lab45_client.save_state(tenant_id=tenant_id, session_id=session_id, user_id=user_id, state=state)
    

async def get_team(lab45_client) -> RoundRobinGroupChat:
    """Define your team with the group of agents"""
    
    # Create the assistant agent.
    primary_agent = AssistantAgent(
        name="assistant",
        model_client=lab45_client,
        model_client_stream=False,
        system_message="Your name is AutogenAssist, you are a general purpose AI assistant which can help with user queries",
    )

    critic_agent = AssistantAgent(
        "critic",
        model_client=lab45_client,
        system_message="Provide constructive feedback. Respond with 'APPROVE' to when your feedbacks are addressed.",
    )

    text_termination = TextMentionTermination("APPROVE")
    max_messages_termination = MaxMessageTermination(max_messages=3)
    termination = text_termination | max_messages_termination

    team = RoundRobinGroupChat([primary_agent, critic_agent], termination_condition=termination)

    return team

# Do not change the method name
async def execute_workflow(**kwargs: Unpack[Lab45AIPlatformStateStoreConfiguration]):
    query = kwargs.get("query")
    tenant_id = kwargs.get("tenant_id")
    user_id = kwargs.get("user_id")
    session_id = kwargs.get("session_id")
    api_key = kwargs.get("api_key") or CONFIG_DATA.get("api_key")
    ## Use dataset_id or files from kwargs if needed

    # Initialize extension client
    laip_model_client = await _get_model_client(api_key)

    team = await get_team(laip_model_client) # Overwirte ony this method with your team

    # Get the team state
    team = await _load_team_state(team, laip_model_client, tenant_id, session_id, user_id)

    response:TaskResult = await team.run(task=query)
    result = []
    for message in response.messages:
        result.append({'source':message.source, 'content': message.content})

    #Save team state
    await _save_team_state(team, laip_model_client, tenant_id, session_id, user_id)

    return result