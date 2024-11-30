"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/update_human_block.py

This script demonstrates how to update an agent's human memory block.

Related scripts:
- update_core_memory.py: For updating all core memory blocks
- manage_archival_memory.py: For managing long-term memories

Memory Structure:
The human block contains information about the user that the agent interacts with.
This can include preferences, traits, and other relevant details.
"""

from letta import create_client
from colorama import init, Fore, Style
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_memory(memory, title="Memory Contents"):
    """Display memory contents with nice formatting"""
    print(f"\n{Fore.BLUE}{title}:{Style.RESET_ALL}")
    
    # Get the persona and human blocks
    persona_block = memory.memory.get('persona')
    human_block = memory.memory.get('human')
    
    if persona_block:
        print(f"\n{Fore.GREEN}[Persona Block]{Style.RESET_ALL}")
        print(persona_block.value)
        
    if human_block:
        print(f"\n{Fore.YELLOW}[Human Block]{Style.RESET_ALL}")
        print(human_block.value)

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
        
        # Get current core memory
        print(f"\nFetching core memory for {selected_agent.name}...")
        core_memory = client.get_in_context_memory(agent_id=selected_agent.id)
        
        # Display current memory
        display_memory(core_memory)
        
        # Get confirmation before update
        confirm = input(f"\nReady to update human block to 'The human is human'. Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Update cancelled.")
            return
            
        # Update the human section
        print("\nUpdating human section...")
        new_human = "The human is human"
        
        # Update the memory
        print("\nSaving updated memory to the server...")
        client.update_in_context_memory(
            agent_id=selected_agent.id,
            section="human",
            value=new_human
        )
        
        # Verify the update
        print("\nVerifying update...")
        updated_memory = client.get_in_context_memory(agent_id=selected_agent.id)
        display_memory(updated_memory, "Updated Memory")
        
        print(f"\n{Fore.GREEN}Core memory updated successfully!{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 