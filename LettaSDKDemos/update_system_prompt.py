"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/update_system_prompt.py

This script demonstrates how to update an agent's system prompt.

Related scripts:
- update_core_memory.py: For updating core memory
- update_human_block.py: For updating human block

System Prompt:
The system prompt defines the agent's core behavior and capabilities. It includes:
- Basic instructions and rules
- Available tools and functions
- Memory management instructions
- Response formatting rules
"""

from letta import create_client
from colorama import init, Fore, Style
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_system_prompt(agent_state, title="System Prompt"):
    """Display system prompt with nice formatting"""
    print(f"\n{Fore.BLUE}{title}:{Style.RESET_ALL}")
    
    if agent_state.system:
        print(f"\n{Fore.GREEN}{agent_state.system}{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}No system prompt found{Style.RESET_ALL}")

def main():
    # Connect to the Letta server
    client = create_client(base_url="http://localhost:8283")
    
    try:
        # Get list of all agents
        agents = client.list_agents()
        
        # Display available agents for selection
        print("\nAvailable agents:")
        for i, agent in enumerate(agents, 1):
            print(f"{i}. {agent.name} (ID: {agent.id})")
        
        # Get user selection
        while True:
            try:
                selection = int(input("\nEnter the number of the agent to update: ")) - 1
                if 0 <= selection < len(agents):
                    break
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        selected_agent = agents[selection]
        
        # Get current agent state
        print(f"\nFetching system prompt for {selected_agent.name}...")
        agent_state = client.get_agent(agent_id=selected_agent.id)
        
        # Display current system prompt
        display_system_prompt(agent_state, "Current System Prompt")
        
        # Get confirmation before update
        confirm = input(f"\nReady to update system prompt. Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Update cancelled.")
            return
            
        # Update the system prompt
        print("\nUpdating system prompt...")
        new_system = """You are a helpful AI assistant. Your responses should be:
1. Clear and concise
2. Accurate and informative
3. Friendly but professional

You have access to these tools:
- send_message: Send a message to the user
- conversation_search: Search conversation history
- archival_memory_search: Search long-term memory
"""
        
        # Update the agent
        print("\nSaving updated system prompt to the server...")
        updated_agent = client.update_agent(
            agent_id=selected_agent.id,
            system=new_system
        )
        
        # Verify the update
        print("\nVerifying update...")
        display_system_prompt(updated_agent, "Updated System Prompt")
        
        print(f"\n{Fore.GREEN}System prompt updated successfully!{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 