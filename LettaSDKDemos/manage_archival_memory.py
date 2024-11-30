"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/manage_archival_memory.py

This script demonstrates how to manage an agent's archival memory.

Related scripts:
- manage_data_sources.py: For managing data sources
- update_core_memory.py: For managing core memory

Memory Operations:
1. List all memories
2. View specific memory details
3. Add new memories
4. Delete memories

Note: Archival memories are stored with unique IDs in the format 'passage-xxxx'.
These IDs must be used when viewing or deleting specific memories.
"""

from letta import create_client
from colorama import init, Fore, Style
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_memory(memory, title="Memory Contents"):
    """Display a single memory entry with nice formatting"""
    print(f"\n{Fore.BLUE}{title}:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{memory.id}")
    print(f"{Fore.GREEN}Content: {Style.RESET_ALL}{memory.text}")
    print(f"{Fore.GREEN}Created At: {Style.RESET_ALL}{memory.created_at}")

def display_memory_list(memories):
    """Display a list of memories with nice formatting"""
    print(f"\n{Fore.BLUE}Found {len(memories)} memories:{Style.RESET_ALL}")
    for i, memory in enumerate(memories, 1):
        print(f"\n{Fore.YELLOW}Memory {i}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{memory.id}")
        print(f"{Fore.GREEN}Content: {Style.RESET_ALL}{memory.text[:100]}...")
        print(f"{Fore.GREEN}Created At: {Style.RESET_ALL}{memory.created_at}")

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
                selection = int(input("\nEnter the number of the agent to manage: ")) - 1
                if 0 <= selection < len(agents):
                    break
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        selected_agent = agents[selection]
        
        while True:
            # Display menu
            print(f"\n{Fore.BLUE}Archival Memory Management for {selected_agent.name}{Style.RESET_ALL}")
            print("1. List all memories")
            print("2. View specific memory")
            print("3. Add new memory")
            print("4. Delete memory")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                # List all memories
                print("\nRetrieving archival memories...")
                memories = client.get_archival_memory(agent_id=selected_agent.id, limit=50)
                display_memory_list(memories)
                
            elif choice == "2":
                # View specific memory
                memory_id = input("\nEnter full memory ID (e.g. passage-xxxx): ")
                try:
                    memories = client.get_archival_memory(agent_id=selected_agent.id, limit=50)
                    memory = next((m for m in memories if m.id == memory_id), None)
                    if memory:
                        display_memory(memory)
                    else:
                        print(f"{Fore.RED}Error: Memory not found{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error: Memory not found - {str(e)}{Style.RESET_ALL}")
                
            elif choice == "3":
                # Add new memory
                content = input("\nEnter memory content: ")
                try:
                    # Use memory parameter
                    client.insert_archival_memory(
                        agent_id=selected_agent.id,
                        memory=content
                    )
                    print(f"{Fore.GREEN}Memory added successfully!{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error adding memory: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "4":
                # Delete memory
                memory_id = input("\nEnter full memory ID (e.g. passage-xxxx): ")
                try:
                    # First verify the memory exists
                    memories = client.get_archival_memory(agent_id=selected_agent.id, limit=50)
                    if not any(m.id == memory_id for m in memories):
                        print(f"{Fore.RED}Error: Memory not found{Style.RESET_ALL}")
                        continue
                        
                    client.delete_archival_memory(
                        agent_id=selected_agent.id,
                        memory_id=memory_id
                    )
                    print(f"{Fore.GREEN}Memory deleted successfully!{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error deleting memory: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "5":
                print("\nExiting...")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 