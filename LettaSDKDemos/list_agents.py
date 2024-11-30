"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/list_agents.py

This script demonstrates how to list all available agents and their basic information.

Related scripts:
- get_agent_info.py: For detailed agent information
- delete_agent.py: For removing agents
- create_agent.py: For creating new agents

IMPLEMENTATION STATUS:
✅ Used in: components/agents_table.py
- Confirmed agent listing works (screenshot shows NiceGiraffe, Wave, etc.)
- Confirmed data structure matches (shows message counts, tools, etc.)
- Confirmed error handling (datetime serialization error caught and fixed)

✅ Used in: main.py
- Confirmed server connection at localhost:8283
- Confirmed basic agent data retrieval
"""

from letta import create_client
from colorama import init, Fore, Style
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def main():
    # Connect to the running Letta server
    client = create_client(base_url="http://localhost:8283")
    
    try:
        # Get list of all agents
        agents = client.list_agents()
        
        print(f"\n{Fore.BLUE}Available agents:{Style.RESET_ALL}")
        for agent in agents:
            print(f"\n{Fore.GREEN}Agent:{Style.RESET_ALL}")
            print(f"- ID: {agent.id}")
            print(f"- Name: {agent.name}")
            print(f"- Description: {agent.description}")
            print("---")
            
    except Exception as e:
        print(f"{Fore.RED}Error listing agents: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 