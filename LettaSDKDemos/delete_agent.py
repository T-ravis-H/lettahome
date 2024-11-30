"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/delete_agent.py

This script demonstrates how to safely delete agents from Letta.

Related scripts:
- list_agents.py: For listing available agents
- create_agent.py: For creating new agents

Important Notes:
- Deletion is permanent and cannot be undone
- All agent data (memory, tools, etc.) is removed
- Requires confirmation before deletion
"""

from letta import create_client
from colorama import init, Fore, Style
import requests
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def delete_agent(base_url, agent_id):
    """Delete an agent using direct API call"""
    try:
        response = requests.delete(f"{base_url}/v1/agents/{agent_id}")
        
        if response.status_code in [200, 204]:
            print(f"{Fore.GREEN}Agent deleted successfully!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
            if response.text:
                print(f"Details: {response.text}")
            return False
            
    except Exception as e:
        print(f"{Fore.RED}Error deleting agent: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    # Connect to the Letta server
    base_url = "http://localhost:8283"
    client = create_client(base_url=base_url)
    
    try:
        while True:
            # List available agents
            agents = client.list_agents()
            
            if not agents:
                print(f"{Fore.YELLOW}No agents found.{Style.RESET_ALL}")
                break
                
            # Display available agents
            print("\nAvailable agents:")
            for i, agent in enumerate(agents, 1):
                print(f"{i}. {agent.name} (ID: {agent.id})")
            
            # Get user selection
            try:
                print("\nEnter the number of the agent to delete (0 to exit):")
                selection = int(input("> "))
                
                if selection == 0:
                    print("\nExiting...")
                    break
                    
                if 1 <= selection <= len(agents):
                    selected_agent = agents[selection - 1]
                    
                    # Get confirmation
                    print(f"\n{Fore.YELLOW}Warning: This will permanently delete the agent!{Style.RESET_ALL}")
                    confirm = input(f"Are you sure you want to delete '{selected_agent.name}'? (y/n): ")
                    
                    if confirm.lower() == 'y':
                        if delete_agent(base_url, selected_agent.id):
                            # Successful deletion
                            continue
                    else:
                        print("Deletion cancelled.")
                else:
                    print(f"{Fore.RED}Invalid selection. Please try again.{Style.RESET_ALL}")
                    
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
                
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        
    print("\nGoodbye!")

if __name__ == "__main__":
    main() 