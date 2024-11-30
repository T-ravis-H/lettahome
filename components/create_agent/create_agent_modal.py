def get_create_agent_modal_html():
    return """
    <div id="create-agent-modal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Create Agent</h2>
                <button class="close-button" id="modal-close">×</button>
            </div>
            
            <div class="modal-body">
                <!-- Agent Name -->
                <div class="form-group">
                    <label for="agent-name">Agent Name</label>
                    <input type="text" id="agent-name" class="form-input">
                    <div class="help-text">This is your agent's display name. It can be a real name or a pseudonym.</div>
                </div>

                <!-- Model Selection -->
                <div class="form-group">
                    <label for="model-select">Model</label>
                    <select id="model-select" class="form-select">
                        <option value="">Select a model</option>
                        <option value="gpt-4">GPT-4</option>
                        <option value="claude-3">Claude-3</option>
                        <option value="letta-free">Letta-free</option>
                    </select>
                    <div class="help-text">Select the model to be used with this agent.</div>
                </div>

                <!-- Embedding Config -->
                <div class="form-group">
                    <label for="embedding-select">Embedding Config</label>
                    <select id="embedding-select" class="form-select">
                        <option value="">Select a model</option>
                        <option value="openai">OpenAI</option>
                        <option value="letta-free">Letta-free</option>
                    </select>
                </div>

                <!-- Core Memory -->
                <div class="form-group">
                    <h3>Core Memory</h3>
                    <div class="help-text">Agent's core memory about itself (agent persona) and the user (human persona).</div>
                    
                    <label for="agent-persona">Agent Persona</label>
                    <textarea id="agent-persona" class="form-textarea" 
                              placeholder="Enter agent persona..."></textarea>

                    <label for="human-persona">Human Persona</label>
                    <textarea id="human-persona" class="form-textarea"
                              placeholder="Enter human persona..."></textarea>
                </div>
            </div>

            <div class="modal-footer">
                <button id="cancel-create" class="button button-secondary">Cancel</button>
                <button id="submit-create" class="button button-primary">Create Agent</button>
            </div>
        </div>
    </div>
    """ 