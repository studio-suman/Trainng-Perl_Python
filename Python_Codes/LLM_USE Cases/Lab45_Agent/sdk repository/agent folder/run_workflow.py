import os
import json
from typing_extensions import Unpack
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from lab45_autogen_extension.lab45aiplatform_autogen_extension import Lab45AIPlatformCompletionClient
from lab45_autogen_extension.utils import Lab45AIPlatformStateStoreConfiguration
from autogen_core import CancellationToken
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

async def _load_agent_state(agent, laip_client, tenant_id, session_id, user_id):
    # Load agent state from sqlite 
    state = laip_client.load_state(tenant_id=tenant_id, session_id=session_id, user_id=user_id)
    if state: 
        await agent.load_state(state)
    return agent
    
async def _save_agent_state(agent, laip_model_client,tenant_id, session_id, user_id):
    # Save agent state to sqlite for an user
    state = await agent.save_state()
    laip_model_client.save_state(tenant_id=tenant_id, session_id=session_id, user_id=user_id, state=state)



async def get_agent(laip_client) -> AssistantAgent:
    """Get the assistant agent, load state from file.
    Overwrite this method with your agent
    """

    # Create the assistant agent.
    agent = AssistantAgent(
        name="assistant",
        model_client=laip_client,
        system_message="You are a helpful assistant.",
    )

    return agent

# Do not change the method and module name
async def execute_workflow(**kwargs: Unpack[Lab45AIPlatformStateStoreConfiguration]):
    """
    Method for executing the Agent workflow
    """
    query = kwargs.get("query")
    tenant_id = kwargs.get("tenant_id")
    user_id = kwargs.get("user_id")
    session_id = kwargs.get("session_id")
    api_key = kwargs.get("api_key") or CONFIG_DATA.get("api_key")
    #files = kwargs.get("files")
    #party_id = kwargs.get("party_id")
    # Above two lines are required only if user has included files
    ## Use dataset id from kwargs if needed

    laip_model_client = await _get_model_client(api_key=api_key)

    # replace with agent logic, return agent object
    agent = await get_agent(laip_model_client) # Overwrite only this method 

    agent = await _load_agent_state(agent, laip_model_client, tenant_id, session_id, user_id)
    # generate response from agent
    response = await agent.on_messages(messages=[TextMessage(content=query, source="user")], cancellation_token=CancellationToken())

    # Save Agent state
    await _save_agent_state(agent, laip_model_client, tenant_id, session_id, user_id)
    
    return response.chat_message