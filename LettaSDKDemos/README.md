# Letta SDK Demo Scripts

This repository contains demo scripts showing how to use the Letta SDK in Python.

## Implementation Status

The following demos have been verified in the Letta Desktop implementation:

### list_agents.py
✅ Used in: components/agents_table.py
- Confirmed agent listing works
- Confirmed data structure matches
- Confirmed error handling

✅ Used in: main.py
- Confirmed server connection at localhost:8283
- Confirmed basic agent data retrieval

### get_agent_info.py
✅ Used for:
- Detailed agent information retrieval
- Configuration data structure
- Memory management patterns

### update_core_memory.py
✅ Used for:
- Memory block structure
- Memory update patterns
- Error handling for memory operations

### update_human_block.py
✅ Used for:
- Human persona management
- Memory block updates
- Data validation patterns

## Directory Structure
All demos are located in the `LettaSDKDemos` directory:
```
LettaSDKDemos/
├── README.md
├── create_agent.py
├── delete_agent.py
├── get_agent_info.py
├── list_agents.py
├── manage_agent_tools.py
├── manage_archival_memory.py
├── manage_data_sources.py
├── manage_embedding_models.py
├── update_core_memory.py
├── update_human_block.py
├── update_system_prompt.py
├── view_colored_messages.py
└── view_messages.py
```

## Prerequisites
- Python 3.x
- A running Letta server instance
- Virtual environment with Letta SDK installed

## Setup
1. Create and activate a virtual environment:
   
   On Windows:
   python -m venv .venv
   .venv\Scripts\activate

   On macOS/Linux:
   python -m venv .venv
   source .venv/bin/activate

2. Install the Letta SDK:
   
   pip install letta

## Demo Scripts

### 1. List Agents (list_agents.py)
This script demonstrates how to:
- Connect to a running Letta server
- Retrieve a list of all available agents
- Display basic information about each agent (ID, Name, Description)

Usage:
   python list_agents.py

Example output:
   Available agents:
   - Agent ID: agent-11567d02-69b7-4376-bba4-ed6c1175dc51
     Name: NiceGiraffe
     Description: None
   ---

### 2. Get Agent Details (get_agent_info.py)
This script demonstrates how to:
- Connect to a running Letta server
- Display a list of available agents for selection
- Retrieve and display detailed information about a selected agent including:
  - Basic properties (ID, Name, Description, Creation date)
  - User ID and Agent Type
  - Message IDs in memory
  - Available tools
  - Agent metadata

Usage:
   python get_agent_info.py

### 3. View Agent Messages (view_messages.py)
This script demonstrates how to:
- Connect to a running Letta server
- Select an agent from the available list
- Retrieve and display the agent's message history
- View detailed information about individual messages including:
  - Message ID and Role
  - Message Content
  - Creation Timestamp
  - Tool Calls and Tool Call IDs (if present)

Usage:
   python view_messages.py

### 4. View Colored Messages (view_colored_messages.py)
This script demonstrates how to:
- Display agent messages with color coding
- Parse different message types
- Handle tool calls and JSON content

Usage:
   python view_colored_messages.py

### 5. Update Core Memory (update_core_memory.py)
This script demonstrates how to:
- Connect to a running Letta server
- Select an agent from the available list
- View and update the agent's core memory blocks:
  - Persona block: Contains the agent's personality
  - Human block: Contains user information

Usage:
   python update_core_memory.py

Memory Structure:
The core memory has two main sections:
   [Persona Block]
   Contains the agent's personality definition, including:
   - Name and identity
   - Personality traits
   - Communication style
   - Goals and motivations

   [Human Block]
   Contains information about the user:
   - First name
   - Last name
   - Other relevant details

Updating Memory:
To update specific sections of memory, use:
   client.update_in_context_memory(
       agent_id=agent.id,
       section="persona",  # or "human"
       value="new content"
   )

Example output:
   Current Memory:
   [Persona Block]
   I am Sam...

   Updated Memory:
   [Persona Block]
   I am Tom...

### 6. Update Human Block (update_human_block.py)
This script demonstrates how to:
- Connect to a running Letta server
- Select an agent from the available list
- View and update the agent's human block in core memory
- Verify the update was successful

Usage:
   python update_human_block.py

Example:
   Current Memory:
   [Human Block]
   First name: Travis
   Last name: Henderson
   Birthdate: August 8th, 1969

   Updated Memory:
   [Human Block]
   The human is human

Memory Updates:
To update the human block, use:
   client.update_in_context_memory(
       agent_id=agent.id,
       section="human",
       value="new content"
   )

Note: Both update_core_memory.py and update_human_block.py use the same method to update memory, just targeting different sections (persona vs human).

### 7. Update System Prompt (update_system_prompt.py)
This script demonstrates how to:
- Connect to a running Letta server
- Select an agent from the available list
- View and update the agent's system prompt
- Verify the update was successful

Usage:
   python update_system_prompt.py

System Prompt:
The system prompt defines the agent's core behavior and capabilities. It includes:
- Basic instructions and rules
- Available tools and functions
- Memory management instructions
- Response formatting rules

Updating System Prompt:
To update an agent's system prompt, use:
   client.update_agent(
       agent_id=agent.id,
       system="new system prompt"
   )

Note: The system prompt is different from core memory. While core memory contains the agent's persona and human information, the system prompt contains the fundamental instructions that govern how the agent operates.

Example:
   Current System Prompt:
   You are Letta, the latest version...

   Updated System Prompt:
   You are a helpful AI assistant...

### 8. Manage Archival Memory (manage_archival_memory.py)
This script demonstrates how to:
- Connect to a running Letta server
- Select an agent from the available list
- View and manage the agent's archival memories:
  - List all memories
  - View specific memory details
  - Add new memories
  - Delete memories

Usage:
   python manage_archival_memory.py

Memory Operations:
1. Listing Memories:
   ```python
   memories = client.get_archival_memory(agent_id=agent.id, limit=50)
   ```

2. Adding Memory:
   ```python
   client.insert_archival_memory(agent_id=agent.id, memory="memory content")
   ```

3. Deleting Memory:
   ```python
   client.delete_archival_memory(agent_id=agent.id, memory_id="passage-xxxx")
   ```

Example output:
   Found 2 memories:
   Memory 1:
   ID: passage-6faa95ef-1470-4000-a739-2d89fe6b76d1
   Content: Travis explained that his brief responses...
   Created At: 2024-11-25 03:15:04

Note: Archival memories are stored with unique IDs in the format 'passage-xxxx'. These IDs must be used when viewing or deleting specific memories.

### 9. Manage Data Sources (manage_data_sources.py)
This script demonstrates how to manage data sources and their files in Letta.

Key Endpoints:

1. List Sources:
   ```
   GET /v1/sources/
   Response: Array of source objects
   ```

2. Create Source:
   ```
   POST /v1/sources/
   Body: {"name": "source_name"}
   Response: Source object
   ```

3. Delete Source:
   ```
   DELETE /v1/sources/{source_id}
   Response: 200 OK
   ```

4. View Source Details:
   ```
   GET /v1/sources/{source_id}
   Response: Source object with metadata
   ```

5. Attach Source to Agent:
   ```
   POST /v1/sources/{source_id}/attach
   Query Params: agent_id={agent_id}
   Response: 200 OK
   ```

6. Detach Source from Agent:
   ```
   POST /v1/sources/{source_id}/detach
   Query Params: agent_id={agent_id}
   Response: 200 OK
   ```

7. Upload File to Source:
   ```
   POST /v1/sources/{source_id}/upload
   Body: multipart/form-data with 'file' field
   Response: 200 OK with job object
   ```

8. List Files in Source:
   ```
   GET /v1/sources/{source_id}/files
   Response: Array of file objects
   ```

9. Delete File from Source:
   ```
   DELETE /v1/sources/{source_id}/{file_id}
   Response: 204 No Content
   ```

Response Formats:

1. Source Object:
   ```
   {
     "id": "source-xxxx",
     "name": "Source Name",
     "description": null,
     "embedding_config": {
       "embedding_endpoint_type": "hugging-face",
       "embedding_model": "letta-free",
       "embedding_dim": 1024,
       ...
     },
     "metadata_": {
       "num_documents": 0,
       "num_passages": 810,
       "attached_agents": [
         {
           "id": "agent-xxxx",
           "name": "AgentName"
         }
       ]
     },
     "created_at": "2024-11-18T07:07:47.409405"
   }
   ```

2. File Object:
   ```
   {
     "id": "file-xxxx",
     "file_name": "example.txt",
     "file_type": "text/plain",
     "file_size": 1024,
     "created_at": "2024-11-25T12:59:51.110750Z"
   }
   ```

3. Upload Job Response:
   ```
   {
     "id": "job-xxxx",
     "status": "completed",
     ...
   }
   ```

Important Notes:

1. File Upload:
   - Use multipart/form-data format
   - File must be opened in binary mode ('rb')
   - Server returns a job ID for tracking

2. File Deletion:
   - Returns 204 No Content on success
   - File ID must include 'file-' prefix

3. Source Attachment:
   - Use query parameters for agent_id
   - Verify source is attached using GET /v1/agents/{agent_id}/sources

4. Error Handling:
   - 404: Source/Agent/File not found
   - 405: Method not allowed (wrong endpoint)
   - 500: Server error (check logs)

Example Usage:

1. Upload File:
   ```python
   with open(file_path, 'rb') as file:
       files = {'file': file}
       response = requests.post(
           f"{base_url}/v1/sources/{source_id}/upload",
           files=files
       )
   ```

2. Attach Source:
   ```python
   response = requests.post(
       f"{base_url}/v1/sources/{source_id}/attach",
       params={"agent_id": agent_id}
   )
   ```

3. Delete File:
   ```python
   response = requests.delete(
       f"{base_url}/v1/sources/{source_id}/{file_id}"
   )
   success = response.status_code in [200, 204]
   ```

### 10. Manage Agent Tools (manage_agent_tools.py)
This script demonstrates how to manage tools attached to agents in Letta.

Key Endpoints:

1. List Agent Tools:
   ```
   GET /v1/agents/{agent_id}/tools
   Response: Array of tool objects
   ```

2. Update Agent Tools:
   ```
   GET /v1/agents/{agent_id}  # First get current agent state
   PATCH /v1/agents/{agent_id}  # Then update with modified tools list
   Body: {"tools": ["tool1", "tool2", ...]}
   Response: Updated agent object
   ```

Response Formats:

1. Tool Object:
   ```
   {
     "id": "tool-xxxx",
     "name": "tool_name",
     "type": "tool_type",
     "configuration": {
       "key": "value",
       ...
     }
   }
   ```

2. Agent Object with Tools:
   ```
   {
     "id": "agent-xxxx",
     "name": "AgentName",
     "tools": ["tool1", "tool2", ...],
     ...
   }
   ```

Important Notes:

1. Tool Management:
   - Tools are managed through the agent's tools list
   - Adding/removing tools requires updating the entire list
   - Use tool names (e.g., "core_memory_append") not IDs

2. Common Tools:
   - send_message: Send messages to users
   - conversation_search: Search conversation history
   - archival_memory_insert: Add to archival memory
   - archival_memory_search: Search archival memory
   - core_memory_append: Add to core memory
   - core_memory_replace: Replace core memory

3. Error Handling:
   - 404: Agent not found
   - 400: Invalid tool name
   - 500: Server error

Example Usage:

1. List Tools:
   ```python
   response = requests.get(f"{base_url}/v1/agents/{agent_id}/tools")
   tools = response.json()
   ```

2. Add Tool:
   ```python
   # Get current tools
   agent = client.get_agent(agent_id=agent_id)
   tools = agent.tools
   
   # Add new tool
   tools.append("new_tool_name")
   
   # Update agent
   client.update_agent(agent_id=agent_id, tools=tools)
   ```

3. Remove Tool:
   ```python
   # Get current tools
   agent = client.get_agent(agent_id=agent_id)
   tools = agent.tools
   
   # Remove tool
   tools.remove("tool_name")
   
   # Update agent
   client.update_agent(agent_id=agent_id, tools=tools)
   ```

### 11. Create Agent (create_agent.py)
This script demonstrates how to create new agents in Letta with both basic and advanced configurations.

Key Features:

1. Basic Agent Creation:
   ```
   client.create_agent(
       name="agent_name",
       description="description"
   )
   ```

2. Advanced Agent Creation:
   ```
   client.create_agent(
       name="agent_name",
       description="description",
       llm_config=LLMConfig(...),
       embedding_config=EmbeddingConfig(...),
       tools=["tool1", "tool2"],
       system="system prompt"
   )
   ```

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

Important Notes:

1. Agent Creation:
   - Names are auto-generated if not provided
   - Default tools are included unless specified
   - System prompt defaults to basic assistant

2. Configuration:
   - LLM config determines the model used for responses
   - Embedding config affects memory and search
   - Tools can be added/removed after creation

3. Error Handling:
   - 400: Invalid configuration
   - 409: Name conflict
   - 500: Server error

Example Usage:

1. Basic Creation:
   ```python
   agent = client.create_agent(name="MyAgent")
   ```

2. Advanced Creation:
   ```python
   agent = client.create_agent(
       name="AdvancedAgent",
       llm_config=LLMConfig(
           model="gpt-4",
           model_endpoint_type="openai"
       ),
       tools=["send_message", "archival_memory_search"]
   )
   ```

### 12. Manage Embedding Models (manage_embedding_models.py)
This script demonstrates how to manage and update embedding models for agents in Letta.

Key Features:

1. List Available Models:
   ```python
   response = requests.get(f"{base_url}/v1/models/embedding")
   models = response.json()
   ```

2. View Agent's Current Config:
   ```python
   agent = client.get_agent(agent_id)
   config = agent.embedding_config
   ```

3. Update Agent's Embedding Model:
   ```python
   client.update_agent(
       agent_id=agent_id,
       embedding_config=new_config
   )
   ```

Available Embedding Models:

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

Important Notes:

1. Configuration:
   - Each model has specific dimension requirements
   - Chunk size affects memory segmentation
   - Endpoint type must match the model

2. Updates:
   - Changes take effect immediately
   - Existing embeddings remain unchanged
   - New content uses updated model

3. Error Handling:
   - 400: Invalid configuration
   - 404: Agent not found
   - 500: Server error

Example Usage:

1. List Models:
   ```python
   models = list_available_models(base_url)
   for model in models:
       print(f"Model: {model.embedding_model}")
   ```

2. Update Model:
   ```python
   new_config = EmbeddingConfig(
       embedding_endpoint_type="openai",
       embedding_model="text-embedding-ada-002",
       embedding_dim=1536
   )
   client.update_agent(agent_id=agent_id, embedding_config=new_config)
   ```

3. View Current Config:
   ```python
   agent = client.get_agent(agent_id)
   print(f"Model: {agent.embedding_config.embedding_model}")
   print(f"Dimension: {agent.embedding_config.embedding_dim}")
   ```

### 13. Delete Agent (delete_agent.py)
This script demonstrates how to safely delete agents from Letta.

Key Features:

1. List Available Agents:
   ```python
   agents = client.list_agents()
   for agent in agents:
       print(f"Name: {agent.name}")
       print(f"ID: {agent.id}")
   ```

2. Delete Agent:
   ```python
   response = requests.delete(f"{base_url}/v1/agents/{agent_id}")
   success = response.status_code in [200, 204]
   ```

Important Notes:

1. Safety:
   - Requires confirmation before deletion
   - Operation is permanent and cannot be undone
   - All agent data (memory, tools, etc.) is removed

2. Error Handling:
   - 404: Agent not found
   - 403: Permission denied
   - 500: Server error

Example Usage:

1. Delete by ID:
   ```python
   success = delete_agent(base_url, "agent-xxxx")
   ```

2. Delete with Confirmation:
   ```python
   if confirm("Delete agent?"):
       delete_agent(base_url, agent_id)
   ```

3. Error Handling:
   ```python
   try:
       delete_agent(base_url, agent_id)
   except Exception as e:
       print(f"Error: {str(e)}")
   ```

## Message Types and Parsing

### User Messages
User messages contain JSON-formatted content with event details. Example:
   {
     "type": "user_message",
     "message": "Hey there, can you remember my name is Travis?",
     "time": "2024-11-24 04:54:28 AM Mountain Standard Time-0700"
   }

### Tool Messages
Tool messages contain status information and results. Example:
   {
     "status": "OK",
     "message": "None",
     "time": "2024-11-24 04:46:14 AM Mountain Standard Time-0700"
   }

### Assistant Messages
Assistant messages can be:
1. Plain text responses
2. Messages with tool calls (especially send_message)

Example with tool call:
   ToolCall(
       id='call_id',
       type='function',
       function=ToolCallFunction(
           name='send_message',
           arguments='{"message": "Chatty, welcome!"}'
       )
   )

### System Messages
System messages contain configuration and setup information. These are typically long and can be truncated for display.

## Message Parsing Tips

### Handling JSON Content
User and Tool messages contain JSON that needs to be parsed. Example:
   try:
       data = json.loads(message.text)
       content = data.get('message', 'No message')
   except json.JSONDecodeError:
       content = message.text

### Tool Call Parsing
Check for tool_calls attribute before accessing. Example:
   if hasattr(message, 'tool_calls') and message.tool_calls:
       tool_call = message.tool_calls[0]
       if "send_message" in str(tool_call):
           args = json.loads(tool_call.function.arguments)
           message = args.get('message', '')

### Message Display
For better readability:
- User messages: Show the message content and time
- Tool messages: Show status and any result message
- Assistant messages: Show the text and any tool call responses
- System messages: Truncate long content

## Color Coding
The view_colored_messages.py script uses these colors:
- Blue: User messages
- Yellow: Tool messages and results
- Green: Assistant messages
- Magenta: System messages
- Red: Error messages
- White: Timestamps


