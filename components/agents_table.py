"""
Confirmed functionality against LettaSDKDemos:
- Agent listing format from list_agents.py
- Agent details retrieval from get_agent_info.py
- Error handling patterns from both demos
"""

def get_agents_table_html():
    return """
    <table class="agents-table">
        <thead>
            <tr>
                <th class="agent-name">Agent Name</th>
                <th class="numeric">
                    <svg class="header-icon" viewBox="0 0 16 16">
                        <path d="M0 2.5A1.5 1.5 0 0 1 1.5 1h11A1.5 1.5 0 0 1 14 2.5v10a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 0 12.5v-10zm1.5-.5a.5.5 0 0 0-.5.5v10a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 .5-.5v-10a.5.5 0 0 0-.5-.5h-11z"/>
                        <path d="M3.5 6.5A.5.5 0 0 1 4 6h8a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.5-.5zm0 3A.5.5 0 0 1 4 9h8a.5.5 0 0 1 0 1H4a.5.5 0 0 1-.5-.5z"/>
                    </svg>
                </th>
                <th class="numeric">
                    <svg class="header-icon" viewBox="0 0 16 16">
                        <path d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"/>
                    </svg>
                </th>
                <th class="numeric">
                    <svg class="header-icon" viewBox="0 0 16 16">
                        <path d="M1.5 0A1.5 1.5 0 0 0 0 1.5v13A1.5 1.5 0 0 0 1.5 16h13a1.5 1.5 0 0 0 1.5-1.5v-13A1.5 1.5 0 0 0 14.5 0h-13zm1 2h3v3h-3V2zm0 4h3v3h-3V6zm0 4h3v3h-3v-3zm4-8h3v3h-3V2zm0 4h3v3h-3V6zm0 4h3v3h-3v-3zm4-8h3v3h-3V2zm0 4h3v3h-3V6zm0 4h3v3h-3v-3z"/>
                    </svg>
                </th>
                <th class="numeric">
                    <svg class="header-icon" viewBox="0 0 16 16">
                        <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                    </svg>
                </th>
                <th>Last Run</th>
                <th>Lifespan</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody id="agents-list"></tbody>
    </table>
    """

def get_agents_table_styles():
    return """
    .agents-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .agents-table th {
        text-align: left;
        padding: 12px 16px;
        border-bottom: 1px solid #30363d;
        color: #8b949e;
        font-weight: normal;
        font-size: 14px;
    }
    
    .agents-table td {
        padding: 12px 16px;
        border-bottom: 1px solid #21262d;
        font-size: 14px;
    }
    
    .agents-table th.numeric,
    .agents-table td.numeric {
        text-align: center;
    }
    
    .header-icon {
        width: 16px;
        height: 16px;
        fill: currentColor;
    }
    
    .agent-name {
        color: #58a6ff;
    }
    
    .date {
        color: #8b949e;
    }
    
    .chat-button {
        background-color: #21262d;
        color: #ffffff;
        border: none;
        padding: 6px 12px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        margin-right: 8px;
    }
    
    .chat-button:hover {
        background-color: #30363d;
    }
    
    .actions-menu {
        background: none;
        border: none;
        color: #8b949e;
        cursor: pointer;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 16px;
    }
    
    .actions-menu:hover {
        background-color: #21262d;
        color: #ffffff;
    }
    
    .loading, .error {
        text-align: center;
        padding: 20px;
        color: #8b949e;
    }
    
    .error {
        color: #f85149;
    }
    
    /* Add loading animation */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    
    .loading {
        animation: pulse 1.5s infinite;
    }
    """

def get_agents_table_js():
    return """
    // Global error handler with window check
    if (typeof window !== 'undefined') {
        window.onerror = function(msg, url, lineNo, columnNo, error) {
            console.error('Global error:', {msg, url, lineNo, columnNo, error});
            return false;
        };
    }

    // Utility functions with logging
    function formatDate(dateString) {
        console.log('Formatting date:', dateString);
        const date = new Date(dateString);
        const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const formatted = `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;
        console.log('Formatted date result:', formatted);
        return formatted;
    }
    
    function showLoading() {
        console.log('showLoading called');
        const tbody = document.getElementById('agents-list');
        console.log('agents-list element found:', !!tbody);
        if (!tbody) {
            console.error('agents-list element not found in showLoading');
            return;
        }
        tbody.innerHTML = '<tr><td colspan="8" class="loading">Loading agents...</td></tr>';
        console.log('Loading state displayed');
    }
    
    function showError(error) {
        console.log('showError called with:', error);
        const tbody = document.getElementById('agents-list');
        console.log('agents-list element found:', !!tbody);
        if (!tbody) {
            console.error('agents-list element not found in showError');
            return;
        }
        tbody.innerHTML = `<tr><td colspan="8" class="error">Error loading agents: ${error}</td></tr>`;
        console.log('Error state displayed');
    }

    // Safe event listener attachment
    function attachEventListeners() {
        console.log('Attempting to attach event listeners...');
        const tbody = document.getElementById('agents-list');
        if (!tbody || !window.pywebview) {
            console.log('Not ready for event listeners yet');
            return false;
        }
        
        const buttons = tbody.querySelectorAll('.chat-button');
        console.log(`Found ${buttons.length} chat buttons to attach listeners to`);
        
        buttons.forEach((button, index) => {
            const agentId = button.dataset.agentId;
            button.addEventListener('click', () => {
                console.log(`Chat button clicked for agent: ${agentId}`);
                window.pageManager.navigateToChat(agentId);
            });
        });
        
        return true;
    }

    async function loadAgents() {
        console.log('Starting to load agents...');
        const tbody = document.getElementById('agents-list');
        if (!tbody) {
            throw new Error('Agents list element not found');
        }

        showLoading();
        try {
            const agents = await window.pywebview.api.get_agents();
            if (!agents || agents.error) {
                throw new Error(agents?.error || 'Failed to load agents');
            }
            
            tbody.innerHTML = '';
            agents.forEach(agent => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="agent-name">${agent.name}</td>
                    <td class="numeric">${agent.messageCount}</td>
                    <td class="numeric">${agent.toolCount}</td>
                    <td class="numeric">${agent.memoryCount}</td>
                    <td class="numeric">${agent.toolsEnabled}</td>
                    <td>${agent.lastRun}</td>
                    <td class="date">${formatDate(agent.lifespan)}</td>
                    <td>
                        <button class="chat-button" data-agent-id="${agent.id}">Chat</button>
                        <button class="actions-menu">⋮</button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Wait for next tick before attaching listeners
            setTimeout(() => {
                if (!attachEventListeners()) {
                    console.log('Will retry event listeners in 100ms');
                    setTimeout(attachEventListeners, 100);
                }
            }, 0);
            
        } catch (error) {
            console.error('Error loading agents:', error);
            showError(error.message);
        }
    }

    // Safe initialization with better window/document checks
    function safeInit() {
        console.log('Checking environment readiness...');
        console.log('- window defined:', typeof window !== 'undefined');
        console.log('- document defined:', typeof document !== 'undefined');
        console.log('- document.readyState:', document?.readyState);
        console.log('- pywebview available:', typeof window !== 'undefined' && !!window.pywebview);

        // Wait for window
        if (typeof window === 'undefined') {
            console.log('Window not ready, retrying in 10ms...');
            setTimeout(safeInit, 10);
            return;
        }

        // Wait for document
        if (typeof document === 'undefined' || !document.body) {
            console.log('Document not ready, retrying in 10ms...');
            setTimeout(safeInit, 10);
            return;
        }

        // Wait for pywebview
        if (!window.pywebview) {
            console.log('PyWebview not ready, adding listener...');
            try {
                window.addEventListener('pywebviewready', safeInit);
            } catch (e) {
                console.log('Failed to add pywebviewready listener, retrying in 10ms...', e);
                setTimeout(safeInit, 10);
            }
            return;
        }

        // Everything ready, start loading
        console.log('Environment ready, starting load...');
        loadAgents();
    }

    // Start safe initialization
    safeInit();
    """ 