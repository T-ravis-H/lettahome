"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/get_agent_info.py

This script demonstrates how to retrieve and display detailed information about agents.

Related scripts:
- list_agents.py: For listing all agents
- view_messages.py: For viewing agent messages
- manage_agent_tools.py: For managing agent tools

Information Retrieved:
1. Basic Properties:
   - ID, Name, Description
   - Creation Date
   - User ID and Agent Type

2. Configuration:
   - Tools available
   - Message IDs in memory
   - Agent metadata

IMPLEMENTATION STATUS:
✅ Used in: components/chat_config.py
- Confirmed agent details retrieval
- Verified configuration data structure
- Adapted memory display format

✅ Used in: main.py
- Confirmed detailed agent info retrieval
- Verified error handling patterns
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
        
        # Display available agents for selection
        print(f"\n{Fore.BLUE}Available agents:{Style.RESET_ALL}")
        for i, agent in enumerate(agents, 1):
            print(f"{i}. {Fore.GREEN}{agent.name}{Style.RESET_ALL} (ID: {agent.id})")
        
        # Get user selection
        while True:
            try:
                selection = int(input("\nEnter the number of the agent you want to inspect: ")) - 1
                if 0 <= selection < len(agents):
                    break
                print(f"{Fore.RED}Invalid selection. Please try again.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
        
        selected_agent = agents[selection]
        
        # Get detailed information about the selected agent
        agent_info = client.get_agent(selected_agent.id)
        
        # Display detailed information
        print(f"\n{Fore.BLUE}Detailed Agent Information:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{agent_info.id}")
        print(f"{Fore.GREEN}Name: {Style.RESET_ALL}{agent_info.name}")
        print(f"{Fore.GREEN}Description: {Style.RESET_ALL}{agent_info.description}")
        print(f"{Fore.GREEN}Created: {Style.RESET_ALL}{agent_info.created_at}")
        print(f"{Fore.GREEN}User ID: {Style.RESET_ALL}{agent_info.user_id}")
        print(f"{Fore.GREEN}Agent Type: {Style.RESET_ALL}{agent_info.agent_type}")
        
        # Display message IDs if available
        if hasattr(agent_info, 'message_ids'):
            print(f"\n{Fore.YELLOW}Message IDs in memory:{Style.RESET_ALL}")
            for msg_id in agent_info.message_ids:
                print(f" - {msg_id}")
        
        # Display tools if available
        if hasattr(agent_info, 'tools'):
            print(f"\n{Fore.YELLOW}Tools available:{Style.RESET_ALL}")
            for tool in agent_info.tools:
                print(f" - {tool}")
        
        # Display metadata if available
        if hasattr(agent_info, 'metadata_'):
            print(f"\n{Fore.YELLOW}Metadata:{Style.RESET_ALL}")
            print(f"{agent_info.metadata_}")
        
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 