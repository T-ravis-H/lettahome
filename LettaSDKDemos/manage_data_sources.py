"""
This script is part of the LettaSDKDemos collection.
Location: LettaSDKDemos/manage_data_sources.py

This script demonstrates how to manage data sources and their files.

Related scripts:
- manage_archival_memory.py: For managing archival memories
- manage_embedding_models.py: For managing embedding models

Key Features:
1. Source Management:
   - List all sources
   - Create new sources
   - Delete sources
   - View source details

2. File Operations:
   - Upload files to sources
   - List files in sources
   - Delete files from sources

3. Agent Attachments:
   - Attach sources to agents
   - Detach sources from agents
   - View attached agents
"""

from letta import create_client, RESTClient
from colorama import init, Fore, Style
import json
import requests
import os
from pathlib import Path

# Initialize colorama
init(autoreset=True)

def display_source(source, title="Source Details"):
    """Display a single source with nice formatting"""
    print(f"\n{Fore.BLUE}{title}:{Style.RESET_ALL}")
    
    # Handle any fields that come back from the server
    try:
        for key, value in source.items():
            if key != 'user_id':  # Skip user_id to avoid validation errors
                print(f"{Fore.GREEN}{key.capitalize()}: {Style.RESET_ALL}{value}")
    except Exception as e:
        print(f"{Fore.RED}Error displaying source: {str(e)}{Style.RESET_ALL}")

def get_attached_agents(base_url, source_id):
    """Get list of agents attached to a source using raw requests"""
    try:
        # Get all agents
        response = requests.get(f"{base_url}/v1/agents/")
        if response.status_code != 200:
            print(f"{Fore.RED}Error getting agents: {response.status_code}{Style.RESET_ALL}")
            return []
            
        agents = response.json()
        attached_agents = []
        
        # Check each agent's sources
        for agent in agents:
            response = requests.get(f"{base_url}/v1/agents/{agent['id']}/sources")
            if response.status_code == 200:
                agent_sources = response.json()
                if any(s['id'] == source_id for s in agent_sources):
                    attached_agents.append(agent)
        
        if attached_agents:
            print(f"\n{Fore.YELLOW}Attached Agents:{Style.RESET_ALL}")
            for agent in attached_agents:
                print(f"- {agent['name']} (ID: {agent['id']})")
        else:
            print(f"\n{Fore.YELLOW}No agents attached to this source{Style.RESET_ALL}")
            
        return attached_agents
    except Exception as e:
        print(f"{Fore.RED}Error listing attached agents: {str(e)}{Style.RESET_ALL}")
        return []

def upload_file_to_source(base_url, source_id, file_path):
    """Upload a file to a source"""
    try:
        # First verify the file exists
        if not os.path.exists(file_path):
            print(f"{Fore.RED}Error: File not found at {file_path}{Style.RESET_ALL}")
            return False
            
        # Try direct file upload using requests
        print(f"\n{Fore.YELLOW}Uploading file...{Style.RESET_ALL}")
        
        # Open file in binary mode
        with open(file_path, 'rb') as file:
            files = {'file': file}
            
            # Make the request to the correct endpoint
            response = requests.post(
                f"{base_url}/v1/sources/{source_id}/upload",
                files=files
            )
            
            if response.status_code == 200:
                print(f"{Fore.GREEN}File uploaded successfully!{Style.RESET_ALL}")
                job = response.json()
                if 'id' in job:
                    print(f"Job ID: {job['id']}")
                return True
            else:
                print(f"{Fore.RED}Upload failed - Server returned {response.status_code}{Style.RESET_ALL}")
                if response.text:
                    print(f"Error: {response.text}")
                return False
            
    except Exception as e:
        print(f"{Fore.RED}Error uploading file: {str(e)}{Style.RESET_ALL}")
        return False

def list_files_in_source(base_url, source_id):
    """List all files in a source"""
    try:
        # Get files from source
        response = requests.get(f"{base_url}/v1/sources/{source_id}/files")
        
        if response.status_code == 200:
            files = response.json()
            if files:
                print(f"\n{Fore.BLUE}Found {len(files)} files:{Style.RESET_ALL}")
                for i, file in enumerate(files, 1):
                    print(f"\n{Fore.YELLOW}File {i}:{Style.RESET_ALL}")
                    print(f"{Fore.GREEN}ID: {Style.RESET_ALL}{file.get('id')}")
                    print(f"{Fore.GREEN}Name: {Style.RESET_ALL}{file.get('file_name')}")
                    print(f"{Fore.GREEN}Type: {Style.RESET_ALL}{file.get('file_type')}")
                    print(f"{Fore.GREEN}Size: {Style.RESET_ALL}{file.get('file_size')} bytes")
                    print(f"{Fore.GREEN}Created: {Style.RESET_ALL}{file.get('created_at')}")
            else:
                print(f"{Fore.YELLOW}No files found in this source{Style.RESET_ALL}")
            return files
        else:
            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
            return []
            
    except Exception as e:
        print(f"{Fore.RED}Error listing files: {str(e)}{Style.RESET_ALL}")
        return []

def delete_file_from_source(base_url, source_id, file_id):
    """Delete a file from a source"""
    try:
        # Make the delete request
        response = requests.delete(
            f"{base_url}/v1/sources/{source_id}/{file_id}"
        )
        
        if response.status_code in [200, 204]:  # Both are success codes
            print(f"{Fore.GREEN}File deleted successfully!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}Delete failed - Server returned {response.status_code}{Style.RESET_ALL}")
            if response.text:
                print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"{Fore.RED}Error deleting file: {str(e)}{Style.RESET_ALL}")
        return False

def main():
    # Connect to the Letta server
    base_url = "http://localhost:8283"
    client = create_client(base_url=base_url)
    
    try:
        while True:
            # Display menu
            print(f"\n{Fore.BLUE}Data Source Management{Style.RESET_ALL}")
            print("1. List all sources")
            print("2. Create new source")
            print("3. Delete source")
            print("4. View source details and attached agents")
            print("5. Attach source to agent")
            print("6. Detach source from agent")
            print("7. Upload file to source")
            print("8. List files in source")
            print("9. Delete file from source")
            print("10. Exit")
            
            choice = input("\nEnter your choice (1-10): ")
            
            if choice == "1":
                # List all sources using raw request
                print("\nRetrieving data sources...")
                try:
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code == 200:
                        sources = response.json()
                        print(f"\n{Fore.BLUE}Found {len(sources)} sources:{Style.RESET_ALL}")
                        for i, source in enumerate(sources, 1):
                            print(f"\n{Fore.YELLOW}Source {i}:{Style.RESET_ALL}")
                            display_source(source)
                    else:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error listing sources: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "2":
                # Create new source using raw request
                name = input("\nEnter name for new source: ")
                try:
                    payload = {"name": name}
                    response = requests.post(f"{base_url}/v1/sources/", json=payload)
                    if response.status_code == 200:
                        source = response.json()
                        print(f"{Fore.GREEN}Source created successfully!{Style.RESET_ALL}")
                        display_source(source, "New Source")
                    else:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}Error creating source: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "3":
                # Delete source using raw request
                try:
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                        
                    sources = response.json()
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                    
                    selection = int(input("\nEnter number of source to delete: ")) - 1
                    if 0 <= selection < len(sources):
                        source = sources[selection]
                        confirm = input(f"Are you sure you want to delete '{source['name']}'? (y/n): ")
                        if confirm.lower() == 'y':
                            response = requests.delete(f"{base_url}/v1/sources/{source['id']}")
                            if response.status_code == 200:
                                print(f"{Fore.GREEN}Source deleted successfully!{Style.RESET_ALL}")
                            else:
                                print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")
                except Exception as e:
                    print(f"{Fore.RED}Error deleting source: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "4":
                # View source details using raw request
                try:
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                        
                    sources = response.json()
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                    
                    selection = int(input("\nEnter number of source to view: ")) - 1
                    if 0 <= selection < len(sources):
                        source = sources[selection]
                        display_source(source)
                        get_attached_agents(base_url, source['id'])
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")
                except Exception as e:
                    print(f"{Fore.RED}Error viewing source: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "5":
                # Attach source to agent
                try:
                    # Get sources
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    sources = response.json()
                    
                    # Get agents
                    response = requests.get(f"{base_url}/v1/agents/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    agents = response.json()
                    
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                        
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent['name']} (ID: {agent['id']})")
                    
                    source_sel = int(input("\nEnter number of source: ")) - 1
                    agent_sel = int(input("Enter number of agent: ")) - 1
                    
                    if 0 <= source_sel < len(sources) and 0 <= agent_sel < len(agents):
                        # Use the correct endpoint: POST /v1/sources/{source_id}/attach?agent_id={agent_id}
                        response = requests.post(
                            f"{base_url}/v1/sources/{sources[source_sel]['id']}/attach",
                            params={"agent_id": agents[agent_sel]['id']}
                        )
                        if response.status_code == 200:
                            print(f"{Fore.GREEN}Source attached successfully!{Style.RESET_ALL}")
                        else:
                            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                            if response.status_code == 405:
                                print("Method not allowed - try using a different HTTP method")
                            elif response.status_code == 404:
                                print("Source or agent not found - check IDs")
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error attaching source: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "6":
                # Detach source from agent
                try:
                    # Get sources
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    sources = response.json()
                    
                    # Get agents
                    response = requests.get(f"{base_url}/v1/agents/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    agents = response.json()
                    
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                        
                    print("\nAvailable agents:")
                    for i, agent in enumerate(agents, 1):
                        print(f"{i}. {agent['name']} (ID: {agent['id']})")
                    
                    source_sel = int(input("\nEnter number of source: ")) - 1
                    agent_sel = int(input("Enter number of agent: ")) - 1
                    
                    if 0 <= source_sel < len(sources) and 0 <= agent_sel < len(agents):
                        # First verify the source is attached
                        response = requests.get(f"{base_url}/v1/agents/{agents[agent_sel]['id']}/sources")
                        if response.status_code != 200:
                            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                            continue
                            
                        agent_sources = response.json()
                        if not any(s['id'] == sources[source_sel]['id'] for s in agent_sources):
                            print(f"{Fore.RED}Error: Source not attached to agent{Style.RESET_ALL}")
                            continue
                        
                        # Try POST to /detach endpoint instead of DELETE
                        response = requests.post(
                            f"{base_url}/v1/sources/{sources[source_sel]['id']}/detach",
                            params={"agent_id": agents[agent_sel]['id']}
                        )
                        if response.status_code == 200:
                            print(f"{Fore.GREEN}Source detached successfully!{Style.RESET_ALL}")
                        else:
                            print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                            if response.status_code == 404:
                                print("Source or agent not found - check IDs")
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error detaching source: {str(e)}{Style.RESET_ALL}")
                
            elif choice == "7":
                # Upload file to source
                try:
                    # Get sources
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    sources = response.json()
                    
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                    
                    source_sel = int(input("\nEnter number of source: ")) - 1
                    if 0 <= source_sel < len(sources):
                        # Get file path
                        file_path = input("\nEnter path to file: ")
                        
                        # Try to upload
                        upload_file_to_source(
                            base_url=base_url,
                            source_id=sources[source_sel]['id'],
                            file_path=file_path
                        )
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error uploading file: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "8":
                # List files in source
                try:
                    # Get sources
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    sources = response.json()
                    
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                    
                    source_sel = int(input("\nEnter number of source: ")) - 1
                    if 0 <= source_sel < len(sources):
                        list_files_in_source(
                            base_url=base_url,
                            source_id=sources[source_sel]['id']
                        )
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error listing files: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "9":
                # Delete file from source
                try:
                    # Get sources
                    response = requests.get(f"{base_url}/v1/sources/")
                    if response.status_code != 200:
                        print(f"{Fore.RED}Error: Server returned {response.status_code}{Style.RESET_ALL}")
                        continue
                    sources = response.json()
                    
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"{i}. {source['name']} (ID: {source['id']})")
                    
                    source_sel = int(input("\nEnter number of source: ")) - 1
                    if 0 <= source_sel < len(sources):
                        # List files in source
                        files = list_files_in_source(
                            base_url=base_url,
                            source_id=sources[source_sel]['id']
                        )
                        
                        if files:
                            file_sel = int(input("\nEnter number of file to delete: ")) - 1
                            if 0 <= file_sel < len(files):
                                # Get confirmation
                                confirm = input(f"Are you sure you want to delete '{files[file_sel].get('file_name')}'? (y/n): ")
                                if confirm.lower() == 'y':
                                    delete_file_from_source(
                                        base_url=base_url,
                                        source_id=sources[source_sel]['id'],
                                        file_id=files[file_sel]['id']
                                    )
                            else:
                                print("Invalid file selection")
                    else:
                        print("Invalid source selection")
                except ValueError:
                    print("Please enter valid numbers")
                except Exception as e:
                    print(f"{Fore.RED}Error deleting file: {str(e)}{Style.RESET_ALL}")
            
            elif choice == "10":
                print("\nExiting...")
                break
                
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main() 