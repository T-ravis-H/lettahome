"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/view_colored_messages.py

This script demonstrates how to display agent messages with color coding.

Related scripts:
- view_messages.py: For basic message viewing
- get_agent_info.py: For detailed agent information

Color Coding:
- Blue: User messages
- Yellow: Tool messages and results
- Green: Assistant messages
- Magenta: System messages
- Red: Error messages
- White: Timestamps
"""

from letta import create_client
from colorama import init, Fore, Style
import json
import os
from pathlib import Path

# Initialize colorama and enable ANSI
init(autoreset=True)
os.system("")

def get_message_color(role):
    """Return color for a given role."""
    role = role.replace("MessageRole.", "").lower()
    if role == "user":
        return Fore.BLUE
    if role == "tool":
        return Fore.YELLOW
    if role == "assistant":
        return Fore.GREEN
    if role == "system":
        return Fore.MAGENTA
    return Fore.WHITE  # Default color

def display_messages(messages):
    """Display messages with color coding."""
    for msg in messages:
        print("\n---")

        # Determine message role and content
        try:
            role = msg.role.replace("MessageRole.", "")
            color = get_message_color(msg.role)
            
            if "user" in role.lower():
                try:
                    data = json.loads(msg.text)
                    content = f"{data.get('message', 'No message')} (Time: {data.get('time', 'Unknown')})"
                except:
                    content = msg.text
                    
            elif "tool" in role.lower():
                try:
                    data = json.loads(msg.text)
                    content = f"Status: {data.get('status', 'Unknown')}, Message: {data.get('message', 'None')}"
                except:
                    content = msg.text
                    
            elif "assistant" in role.lower():
                content = msg.text
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    try:
                        tool_call = msg.tool_calls[0]
                        if "send_message" in str(tool_call):
                            args = json.loads(tool_call.function.arguments)
                            content += f"\nResponse: {args.get('message', '')}"
                    except:
                        content += "\n[Tool call parsing failed]"
                        
            elif "system" in role.lower():
                content = f"{msg.text[:100]}..." if len(msg.text) > 100 else msg.text
                
            else:
                content = msg.text

            # Print the message with color
            print(color + f"[{role}] {content}" + Style.RESET_ALL)
            print(Fore.WHITE + f"Timestamp: {msg.created_at}" + Style.RESET_ALL)
            
        except Exception as e:
            print(Fore.RED + f"Error parsing message: {str(e)}" + Style.RESET_ALL)

def main():
    # Test color output
    print(Fore.YELLOW + "Testing color output..." + Style.RESET_ALL)
    print(Fore.GREEN + "If you can see this in green, colors are working!" + Style.RESET_ALL)
    
    # Connect to the Letta server
    client = create_client(base_url="http://localhost:8283")

    try:
        # List agents
        agents = client.list_agents()
        print("\nAvailable agents:")
        for i, agent in enumerate(agents, 1):
            print(f"{i}. {agent.name} (ID: {agent.id})")

        # Select an agent
        while True:
            try:
                selection = int(input("\nEnter the number of the agent to view messages: ")) - 1
                if 0 <= selection < len(agents):
                    break
                print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        selected_agent = agents[selection]

        # Get messages
        messages = client.get_messages(agent_id=selected_agent.id, limit=50)
        if not messages:
            print("\nNo messages found for this agent.")
            return

        # Display messages
        print(f"\nMessage history for {selected_agent.name}:")
        display_messages(messages)

    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    main() 