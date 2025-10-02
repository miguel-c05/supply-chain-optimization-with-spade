import spade
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour


class MyAgent(Agent):
    """
    A simple SPADE agent that runs a OneShotBehaviour to print "Hello World".
    """

    class MyBehav(OneShotBehaviour):
        async def run(self):
            """
            The main logic of the behavior: prints a message and stops the agent.
            """
            print("Hello World from Agent!")
            
            # Crucial: Stop the agent after the behavior is executed once
            await self.agent.stop()

    async def setup(self):
        """
        Called when the agent is initialized. Adds the behavior.
        """
        print(f"Agent {self.jid} starting up.")
        self.add_behaviour(self.MyBehav())


async def main():
    """
    Initializes and starts the agent instance.
    """
    # NOTE: Ensure you have an XMPP server (like ejabberd or the built-in test server) 
    # running on 'localhost' for this agent to connect.
    agent = MyAgent("agent@localhost", "password")
    
    # Start the agent and wait for it to be ready
    await agent.start()
    
    # The main coroutine can now wait or return. 
    # Since MyBehav stops the agent, the spade runtime will exit shortly.
    

if __name__ == "__main__":
    print("--- Starting SPADE Runtime ---")
    # spade.run() handles initializing the asyncio event loop and running main()
    spade.run(main())
    print("--- SPADE Runtime Finished ---")
