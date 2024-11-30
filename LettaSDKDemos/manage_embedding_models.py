"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/manage_embedding_models.py

This script demonstrates how to manage and update embedding models for agents.

Related scripts:
- create_agent.py: For creating agents with specific embedding models
- manage_data_sources.py: For managing data sources that use embeddings

Available Models:
1. Letta-free:
   - Type: hugging-face
   - Endpoint: https://embeddings.memgpt.ai
   - Dimension: 1024
   - Chunk Size: 300

2. OpenAI:
   - Type: openai
   - Endpoint: https://api.openai.com/v1
   - Model: text-embedding-ada-002
   - Dimension: 1536
   - Chunk Size: 300
"""

from letta import create_client, EmbeddingConfig
from colorama import init, Fore, Style
import requests
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_embedding_config(config, title="Embedding Configuration"):
    """Display embedding config with nice formatting"""
    print(f"\n{Fore.BLUE}{title}:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Model: {Style.RESET_ALL}{config.embedding_model}")
    print(f"{Fore.GREEN}Endpoint Type: {Style.RESET_ALL}{config.embedding_endpoint_type}")
    print(f"{Fore.GREEN}Endpoint: {Style.RESET_ALL}{config.embedding_endpoint}")
    print(f"{Fore.GREEN}Dimension: {Style.RESET_ALL}{config.embedding_dim}")
    print(f"{Fore.GREEN}Chunk Size: {Style.RESET_ALL}{config.embedding_chunk_size}")

def list_available_models(base_url):
    """List all available embedding models using direct API call"""
    try:
        response = requests.get(f"{base_url}/v1/models/embedding")
        if response.status_code == 200:
            models = response.json()
            print(f"\n{Fore.BLUE}Available Embedding Models:{Style.RESET_ALL}")
            for i, model in enumerate(models, 1):
                print(f"\n{Fore.YELLOW}Model {i}:{Style.RESET_ALL}")
                display_embedding_config(EmbeddingConfig(**model))
            return models
        else:
            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
            return []
    except Exception as e:
        print(f"{Fore.RED}Error listing models: {str(e)}{Style.RESET_ALL}")
        return []

def update_agent_embedding(client, agent_id, new_config):
    """Update an agent's embedding configuration"""
    try:
        updated_agent = client.update_agent(
            agent_id=agent_id,
            embedding_config=new_config
        )
        print(f"{Fore.GREEN}Embedding configuration updated successfully!{Style.RESET_ALL}")
        return updated_agent
    except Exception as e:
        print(f"{Fore.RED}Error updating embedding config: {str(e)}{Style.RESET_ALL}")
        return None

def main():
    # Connect to the Letta server
    base_url = "http://localhost:8283"
    client = create_client(base_url=base_url)
    
    try:
        while True:
            # Display menu
            print(f"\n{Fore.BLUE}Embedding Model Management{Style.RESET_ALL}")
            print("1. List available embedding models")
            print("2. View agent's current embedding config")
            print("3. Update agent's embedding config")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                # List available models
                list_available_models(base_url)
                
            elif choice == "2":
                # View agent's current config
                try:
                    # Get list of agents
                    agents = client.list_agents()
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent.name} (ID: {agent.id})")
                    
                    selection = int(input("\nEnter the number of the agent to view: ")) - 1
                    if 0 <= selection < len(agents):
                        agent = client.get_agent(agents[selection].id)
                        if hasattr(agent, 'embedding_config'):
                            display_embedding_config(
                                agent.embedding_config,
                                f"Current Embedding Config for {agent.name}"
                            )
                        else:
                            print(f"{Fore.YELLOW}No embedding configuration found{Style.RESET_ALL}")
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")
                except Exception as e:
                    print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "3":
                # Update agent's config
                try:
                    # Get list of agents
                    agents = client.list_agents()
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent.name} (ID: {agent.id})")
                    
                    agent_sel = int(input("\nEnter the number of the agent to update: ")) - 1
                    if 0 <= agent_sel < len(agents):
                        # Get available models
                        models = list_available_models(base_url)
                        if models:
                            model_sel = int(input("\nEnter the number of the model to use: ")) - 1
                            if 0 <= model_sel < len(models):
                                # Create EmbeddingConfig from selected model
                                new_config = EmbeddingConfig(**models[model_sel])
                                
                                # Update the agent
                                updated_agent = update_agent_embedding(
                                    client=client,
                                    agent_id=agents[agent_sel].id,
                                    new_config=new_config
                                )
                                if updated_agent:
                                    display_embedding_config(
                                        updated_agent.embedding_config,
                                        "Updated Configuration"
                                    )
                            else:
                                print("Invalid model selection")
                    else:
                        print("Invalid agent selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "4":
                print("\nExiting...")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 