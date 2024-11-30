"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/create_agent.py

This script demonstrates how to create new agents in Letta with both basic 
and advanced configurations.

Related scripts:
- manage_embedding_models.py: For managing agent embedding models
- manage_agent_tools.py: For managing agent tools
- update_system_prompt.py: For updating system prompts

Configuration Options:
1. LLM Models:
   - GPT-4 (OpenAI)
   - Claude-3 (Anthropic)
   - Letta-free

2. Embedding Models:
   - OpenAI (text-embedding-ada-002)
   - Letta-free

3. Available Tools:
   - send_message
   - conversation_search
   - archival_memory_insert
   - archival_memory_search
   - core_memory_append
   - core_memory_replace
"""

from letta import create_client, LLMConfig, EmbeddingConfig
from colorama import init, Fore, Style
import json
import requests
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def create_basic_agent(client, name, description=None):
    """Create a basic agent with minimal configuration"""
    try:
        print(f"\n{Fore.YELLOW}Creating basic agent '{name}'...{Style.RESET_ALL}")
        
        # Create default LLM config
        llm_config = LLMConfig(
            model="letta-free",
            model_endpoint_type="openai",
            model_endpoint="https://inference.memgpt.ai",
            context_window=16384,
            put_inner_thoughts_in_kwargs=True
        ).dict(exclude_none=True)
        
        # Create default embedding config
        embedding_config = EmbeddingConfig(
            embedding_endpoint_type="hugging-face",
            embedding_endpoint="https://embeddings.memgpt.ai",
            embedding_model="letta-free",
            embedding_dim=1024,
            embedding_chunk_size=300
        ).dict(exclude_none=True)
        
        # Create default memory config with blocks
        memory_config = {
            "memory": {
                "persona": {
                    "label": "persona",
                    "value": "I am a helpful AI assistant.",
                    "limit": 2000
                },
                "human": {
                    "label": "human", 
                    "value": "The human I am talking to.",
                    "limit": 2000
                }
            }
        }
        
        # Create minimal agent payload
        agent_payload = {
            "name": name,
            "description": description,
            "llm_config": llm_config,
            "embedding_config": embedding_config,
            "tools": ["send_message", "conversation_search"],
            "system": "You are a helpful AI assistant.",
            "memory": memory_config
        }
        
        # Create the agent directly with the payload
        response = requests.post(
            f"{client.base_url}/v1/agents/",
            json=agent_payload
        )
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}Agent created successfully!{Style.RESET_ALL}")
            return response.json()
        else:
            print(f"{Fore.RED}Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
            return None
            
    except Exception as e:
        print(f"{Fore.RED}Error creating basic agent: {str(e)}{Style.RESET_ALL}")
        return None

def create_advanced_agent(client, name, description=None):
    """Create an agent with advanced configuration"""
    try:
        print(f"\n{Fore.YELLOW}Creating advanced agent '{name}'...{Style.RESET_ALL}")
        
        # Get LLM config
        print("\nSelect LLM model:")
        print("1. GPT-4")
        print("2. Claude-3")
        print("3. Letta-free")
        
        model_choice = input("Enter choice (1-3): ")
        if model_choice == "1":
            llm_config = LLMConfig(
                model="gpt-4",
                model_endpoint_type="openai",
                model_endpoint="https://api.openai.com/v1",
                context_window=8192,
                put_inner_thoughts_in_kwargs=False
            ).dict(exclude_none=True)
        elif model_choice == "2":
            llm_config = LLMConfig(
                model="claude-3-opus-20240229",
                model_endpoint_type="anthropic",
                model_endpoint="https://api.anthropic.com/v1",
                context_window=200000,
                put_inner_thoughts_in_kwargs=True
            ).dict(exclude_none=True)
        else:
            llm_config = LLMConfig(
                model="letta-free",
                model_endpoint_type="openai",
                model_endpoint="https://inference.memgpt.ai",
                context_window=16384,
                put_inner_thoughts_in_kwargs=True
            ).dict(exclude_none=True)
            
        # Get embedding config
        print("\nSelect embedding model:")
        print("1. OpenAI")
        print("2. Letta-free")
        
        embed_choice = input("Enter choice (1-2): ")
        if embed_choice == "1":
            embedding_config = EmbeddingConfig(
                embedding_endpoint_type="openai",
                embedding_endpoint="https://api.openai.com/v1",
                embedding_model="text-embedding-ada-002",
                embedding_dim=1536,
                embedding_chunk_size=300
            ).dict(exclude_none=True)
        else:
            embedding_config = EmbeddingConfig(
                embedding_endpoint_type="hugging-face",
                embedding_endpoint="https://embeddings.memgpt.ai",
                embedding_model="letta-free",
                embedding_dim=1024,
                embedding_chunk_size=300
            ).dict(exclude_none=True)
            
        # Get tools
        print("\nSelect tools (comma-separated):")
        print("Available tools:")
        print("- send_message")
        print("- conversation_search")
        print("- archival_memory_insert")
        print("- archival_memory_search")
        print("- core_memory_append")
        print("- core_memory_replace")
        
        tools_input = input("Enter tool names: ")
        tools = [t.strip() for t in tools_input.split(",") if t.strip()]
        
        # Validate tool names
        valid_tools = {
            "send_message",
            "conversation_search",
            "archival_memory_insert",
            "archival_memory_search",
            "core_memory_append",
            "core_memory_replace"
        }
        
        if not all(tool in valid_tools for tool in tools):
            raise ValueError("Invalid tool name(s). Please check spelling.")
        
        # Get system prompt
        print("\nEnter system prompt (or press Enter for default):")
        system = input() or "You are a helpful AI assistant."
        
        # Create memory config with blocks
        memory_config = {
            "memory": {
                "persona": {
                    "label": "persona",
                    "value": "I am a helpful AI assistant.",
                    "limit": 2000
                },
                "human": {
                    "label": "human", 
                    "value": "The human I am talking to.",
                    "limit": 2000
                }
            }
        }
        
        # Create agent payload
        agent_payload = {
            "name": name,
            "description": description,
            "llm_config": llm_config,
            "embedding_config": embedding_config,
            "tools": tools,
            "system": system,
            "memory": memory_config
        }
        
        # Create the agent directly with the payload
        response = requests.post(
            f"{client.base_url}/v1/agents/",
            json=agent_payload
        )
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}Agent created successfully!{Style.RESET_ALL}")
            return response.json()
        else:
            print(f"{Fore.RED}Error: {response.status_code} - {response.text}{Style.RESET_ALL}")
            return None
            
    except Exception as e:
        print(f"{Fore.RED}Error creating advanced agent: {str(e)}{Style.RESET_ALL}")
        return None

def display_agent(agent_dict):
    """Display agent details with nice formatting"""
    print(f"\n{Fore.BLUE}Agent Details:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{agent_dict.get('id')}")
    print(f"{Fore.GREEN}Name: {Style.RESET_ALL}{agent_dict.get('name')}")
    print(f"{Fore.GREEN}Description: {Style.RESET_ALL}{agent_dict.get('description')}")
    print(f"{Fore.GREEN}Created At: {Style.RESET_ALL}{agent_dict.get('created_at')}")
    
    if 'tools' in agent_dict:
        print(f"\n{Fore.YELLOW}Tools:{Style.RESET_ALL}")
        for tool in agent_dict['tools']:
            print(f"- {tool}")
            
    if 'system' in agent_dict:
        print(f"\n{Fore.YELLOW}System Prompt:{Style.RESET_ALL}")
        print(agent_dict['system'])

def main():
    # Connect to the Letta server
    base_url = "http://localhost:8283"
    client = create_client(base_url=base_url)
    
    try:
        while True:
            # Display menu
            print(f"\n{Fore.BLUE}Agent Creation{Style.RESET_ALL}")
            print("1. Create basic agent")
            print("2. Create advanced agent")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                # Basic agent creation
                name = input("\nEnter agent name: ")
                description = input("Enter description (optional): ")
                
                agent = create_basic_agent(
                    client=client,
                    name=name,
                    description=description
                )
                
                if agent:
                    display_agent(agent)
                
            elif choice == "2":
                # Advanced agent creation
                name = input("\nEnter agent name: ")
                description = input("Enter description (optional): ")
                
                agent = create_advanced_agent(
                    client=client,
                    name=name,
                    description=description
                )
                
                if agent:
                    display_agent(agent)
                
            elif choice == "3":
                print("\nExiting...")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 