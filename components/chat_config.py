"""
Confirmed functionality against LettaSDKDemos:
- Agent configuration retrieval from get_agent_info.py
- Memory management patterns from update_core_memory.py
- Persona handling from update_human_block.py
"""

def get_chat_config_html():
    return """
    <div class="chat-config">
        <header class="chat-header">
            <button class="back-button">
                <span>←</span>
            </button>
            <div class="agent-info">
                <h1 class="agent-name">Agent Chat</h1>
                <div class="agent-id"></div>
            </div>
            <div class="settings-button">⚙️</div>
        </header>
        
        <div class="config-layout">
            <aside class="config-sidebar">
                <div class="model-info">
                    <h3>MODEL</h3>
                    <div class="model-name">gpt-4o</div>
                </div>
                
                <div class="embedding-info">
                    <h3>EMBEDDING MODEL</h3>
                    <div class="model-name">letta-free</div>
                </div>
                
                <div class="core-memory">
                    <h3>CORE MEMORY</h3>
                    <div class="memory-content"></div>
                </div>
                
                <div class="agent-persona">
                    <h3>Agent Persona</h3>
                    <div class="persona-content"></div>
                </div>
                
                <div class="human-persona">
                    <h3>Human Persona</h3>
                    <div class="persona-content"></div>
                </div>
            </aside>
            
            <main class="chat-area">
                <!-- Chat interface will go here -->
            </main>
        </div>
    </div>
    """

def get_chat_config_styles():
    return """
    .chat-config {
        height: 100vh;
        display: flex;
        flex-direction: column;
    }
    
    .chat-header {
        display: flex;
        align-items: center;
        padding: 16px;
        border-bottom: 1px solid #21262d;
    }
    
    .back-button {
        background: none;
        border: none;
        color: #8b949e;
        font-size: 20px;
        cursor: pointer;
        padding: 8px;
        margin-right: 16px;
    }
    
    .back-button:hover {
        color: #ffffff;
    }
    
    .agent-info {
        flex: 1;
    }
    
    .agent-name {
        margin: 0;
        font-size: 20px;
        font-weight: 600;
    }
    
    .agent-id {
        color: #8b949e;
        font-size: 12px;
    }
    
    .config-layout {
        display: flex;
        flex: 1;
        overflow: hidden;
    }
    
    .config-sidebar {
        width: 300px;
        background-color: #0D1117;
        border-right: 1px solid #21262d;
        padding: 20px;
        overflow-y: auto;
    }
    
    .config-sidebar h3 {
        color: #8b949e;
        font-size: 12px;
        margin: 0 0 8px 0;
        font-weight: normal;
    }
    
    .model-info,
    .embedding-info,
    .core-memory,
    .agent-persona,
    .human-persona {
        margin-bottom: 24px;
    }
    
    .model-name {
        color: #ffffff;
        font-size: 14px;
    }
    """

def get_chat_config_js():
    return """
    async function loadChatConfig(agentId) {
        try {
            const agent = await window.pywebview.api.get_agent_config(agentId);
            
            document.querySelector('.agent-name').textContent = agent.name;
            document.querySelector('.agent-id').textContent = `Agent ID: ${agent.id}`;
            
            // Load core memory
            document.querySelector('.core-memory .memory-content').innerHTML = 
                `<pre>${agent.core_memory || 'No core memory'}</pre>`;
                
            // Load personas
            document.querySelector('.agent-persona .persona-content').innerHTML = 
                `<pre>${agent.agent_persona || 'No agent persona'}</pre>`;
            document.querySelector('.human-persona .persona-content').innerHTML = 
                `<pre>${agent.human_persona || 'No human persona'}</pre>`;
                
        } catch (error) {
            console.error('Error loading chat config:', error);
        }
    }
    
    document.querySelector('.back-button').addEventListener('click', () => {
        window.pywebview.api.navigate_to_agents();
    });
    """ 