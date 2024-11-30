"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/view_messages.py

This script demonstrates how to retrieve and display agent messages.

Related scripts:
- view_colored_messages.py: For colored message display
- get_agent_info.py: For detailed agent information
"""

from letta import create_client
from colorama import init, Fore, Style
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_message(message):
    """Format and display a single message with all available details"""
    print(f"\n{Fore.BLUE}Message Details:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{message.id}")
    print(f"{Fore.GREEN}Role: {Style.RESET_ALL}{message.role}")
    print(f"{Fore.GREEN}Content: {Style.RESET_ALL}{message.text}")
    print(f"{Fore.GREEN}Created At: {Style.RESET_ALL}{message.created_at}")
    if hasattr(message, 'tool_calls'):
        print(f"{Fore.GREEN}Tool Calls: {Style.RESET_ALL}{message.tool_calls}")
    if hasattr(message, 'tool_call_id'):
        print(f"{Fore.GREEN}Tool Call ID: {Style.RESET_ALL}{message.tool_call_id}")
    print("---")

def main():
    # Connect to the running Letta server
    client = create_client(base_url="http://localhost:8283")
    
    try:
        # Get list of all agents
        agents = client.list_agents()
        
        # Display available agents for selection
        print("\nAvailable agents:")
        for i, agent in enumerate(agents, 1):
            print(f"{i}. {agent.name} (ID: {agent.id})")
        
        # Get user selection for agent
        while True:
            try:
                selection = int(input("\nEnter the number of the agent to view messages: ")) - 1
                if 0 <= selection < len(agents):
                    break
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        selected_agent = agents[selection]
        
        # Get messages for the selected agent
        messages = client.get_messages(agent_id=selected_agent.id, limit=50)
        
        if not messages:
            print("\nNo messages found for this agent.")
            return
            
        # Display message list
        print("\nMessage history:")
        for i, message in enumerate(messages, 1):
            print(f"{i}. [{message.role}] {message.text[:50]}...")
        
        # Let user view individual messages
        while True:
            try:
                msg_selection = int(input("\nEnter the number of the message to view details (0 to exit): ")) - 1
                if msg_selection == -1:
                    break
                if 0 <= msg_selection < len(messages):
                    display_message(messages[msg_selection])
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 