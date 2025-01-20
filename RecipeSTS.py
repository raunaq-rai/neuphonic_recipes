#Import libraries
from pyneuphonic import Neuphonic, TTSConfig, Agent
from pyneuphonic.player import AudioPlayer
import asyncio
api_key = "" # GET THIS FROM beta.neuphonic.com!!!!!!!!!


async def main():
    client = Neuphonic(api_key=api_key)

    agent_id = client.agents.create(
        name='Recipe Agent',
        prompt="You are a helpful agent. You help users find recipes using the" +
                "ingredients they have in their fridge and cupboard. Provide a " +
                "list of possible recipes using the ingredients given by the user, " +
                "the provide them with a method and ingredients list for the item they choose.",
        greeting='Please speak the ingredients you have:',
    ).data['id']

    agent = Agent(client, agent_id=agent_id, tts_model='neu_hq')

    await agent.start()

asyncio.run(main())