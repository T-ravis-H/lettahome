"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/manage_agent_tools.py

This script demonstrates how to manage tools attached to agents.

Related scripts:
- create_agent.py: For creating agents with specific tools
- get_agent_info.py: For viewing agent details

Available Tools:
- send_message: Send messages to users
- conversation_search: Search conversation history
- archival_memory_insert: Add to archival memory
- archival_memory_search: Search archival memory
- core_memory_append: Add to core memory
- core_memory_replace: Replace core memory

Note: Tools can be added or removed at any time, and changes take effect immediately.
"""

from letta import create_client
from colorama import init, Fore, Style
import requests
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def list_agent_tools(base_url, agent_id):
    """List all tools attached to an agent"""
    try:
        response = requests.get(f"{base_url}/v1/agents/{agent_id}/tools")
        
        if response.status_code == 200:
            tools = response.json()
            if tools:
                print(f"\n{Fore.BLUE}Found {len(tools)} tools:{Style.RESET_ALL}")
                for i, tool in enumerate(tools, 1):
                    print(f"\n{Fore.YELLOW}Tool {i}:{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{tool.get('id')}")
                    print(f"{Fore.GREEN}Name: {Style.RESET_ALL}{tool.get('name')}")
                    print(f"{Fore.GREEN}Type: {Style.RESET_ALL}{tool.get('type')}")
                    if 'configuration' in tool:
                        print(f"{Fore.GREEN}Configuration:{Style.RESET_ALL}")
                        for key, value in tool['configuration'].items():
                            print(f"  - {key}: {value}")
            else:
                print(f"{Fore.YELLOW}No tools found for this agent{Style.RESET_ALL}")
            return tools
        else:
            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
            return []
            
    except Exception as e:
        print(f"{Fore.RED}Error listing tools: {str(e)}{Style.RESET_ALL}")
        return []

def add_tool_to_agent(base_url, agent_id, tool_name):
    """Add a tool to an agent using agent update"""
    try:
        # Get current agent state first
        response = requests.get(f"{base_url}/v1/agents/{agent_id}")
        if response.status_code != 200:
            print(f"{Fore.RED}Error getting agent: {response.status_code}{Style.RESET_ALL}")
            return False
            
        agent = response.json()
        current_tools = agent.get('tools', [])
        
        # Add new tool to list if it's not already there
        if tool_name not in current_tools:
            current_tools.append(tool_name)
            
            # Update agent with new tool list
            client = create_client(base_url=base_url)
            updated_agent = client.update_agent(
                agent_id=agent_id,
                tools=current_tools
            )
            
            print(f"{Fore.GREEN}Tool added successfully!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.YELLOW}Tool already attached to agent{Style.RESET_ALL}")
            return False
            
    except Exception as e:
        print(f"{Fore.RED}Error adding tool: {str(e)}{Style.RESET_ALL}")
        return False

def remove_tool_from_agent(base_url, agent_id, tool_name):
    """Remove a tool from an agent using agent update"""
    try:
        # Get current agent state first
        response = requests.get(f"{base_url}/v1/agents/{agent_id}")
        if response.status_code != 200:
            print(f"{Fore.RED}Error getting agent: {response.status_code}{Style.RESET_ALL}")
            return False
            
        agent = response.json()
        current_tools = agent.get('tools', [])
        
        # Remove tool from list if it exists
        if tool_name in current_tools:
            current_tools.remove(tool_name)
            
            # Update agent with new tool list
            client = create_client(base_url=base_url)
            updated_agent = client.update_agent(
                agent_id=agent_id,
                tools=current_tools
            )
            
            print(f"{Fore.GREEN}Tool '{tool_name}' removed successfully!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.YELLOW}Tool '{tool_name}' not found on agent{Style.RESET_ALL}")
            return False
            
    except Exception as e:
        print(f"{Fore.RED}Error removing tool: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    # Connect to the Letta server
    base_url = "http://localhost:8283"
    client = create_client(base_url=base_url)
    
    try:
        while True:
            # Display menu
            print(f"\n{Fore.BLUE}Agent Tool Management{Style.RESET_ALL}")
            print("1. List agent tools")
            print("2. Add tool to agent")
            print("3. Remove tool from agent")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                # List agent tools
                try:
                    # Get agents
                    agents = client.list_agents()
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent.name} (ID: {agent.id})")
                    
                    agent_sel = int(input("\nEnter number of agent: ")) - 1
                    if 0 <= agent_sel < len(agents):
                        list_agent_tools(
                            base_url=base_url,
                            agent_id=agents[agent_sel].id
                        )
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error listing tools: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "2":
                # Add tool to agent
                try:
                    # Get agents
                    agents = client.list_agents()
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent.name} (ID: {agent.id})")
                    
                    agent_sel = int(input("\nEnter number of agent: ")) - 1
                    if 0 <= agent_sel < len(agents):
                        tool_name = input("Tool name: ")
                        add_tool_to_agent(
                            base_url=base_url,
                            agent_id=agents[agent_sel].id,
                            tool_name=tool_name
                        )
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error adding tool: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "3":
                # Remove tool from agent
                try:
                    # Get agents
                    agents = client.list_agents()
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent.name} (ID: {agent.id})")
                    
                    agent_sel = int(input("\nEnter number of agent: ")) - 1
                    if 0 <= agent_sel < len(agents):
                        # List tools for selected agent
                        tools = list_agent_tools(
                            base_url=base_url,
                            agent_id=agents[agent_sel].id
                        )
                        
                        if tools:
                            print(f"\n{Fore.YELLOW}Enter the name of the tool to remove (e.g. 'core_memory_replace'){Style.RESET_ALL}")
                            tool_name = input("Tool name: ")
                            remove_tool_from_agent(
                                base_url=base_url,
                                agent_id=agents[agent_sel].id,
                                tool_name=tool_name
                            )
                        else:
                            print("No tools found for this agent")
                    else:
                        print("Invalid agent selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error removing tool: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "4":
                print("\nExiting...")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 