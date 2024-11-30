def get_create_agent_modal_js():
    return """
    console.log('=== Create Agent Modal Script Loading ===');

    // Debug click handler
    function debugButtonClick(e) {
        console.log('=== Create Agent Button Click Debug ===');
        console.log('Click event:', e);
        console.log('Button element:', e.target);
        console.log('Button classes:', e.target.classList);
        console.log('Button text:', e.target.textContent);
        console.log('Event timestamp:', new Date().toISOString());
    }

    // Add global click debugging
    document.addEventListener('click', (e) => {
        if (e.target.matches('.create-agent-btn')) {
            console.log('Create Agent button clicked via global handler');
            debugButtonClick(e);
        }
    });

    class CreateAgentModal {
        constructor() {
            console.log('=== CreateAgentModal Constructor Start ===');
            this.initializeElements();
            this.attachEventListeners();
            console.log('=== CreateAgentModal Constructor End ===');
        }

        initializeElements() {
            console.log('=== Finding Modal Elements ===');
            
            // Modal elements
            this.modal = document.getElementById('create-agent-modal');
            this.submitBtn = document.getElementById('submit-create');
            this.closeBtn = document.getElementById('modal-close');
            this.cancelBtn = document.getElementById('cancel-create');
            this.createAgentBtn = document.querySelector('.create-agent-btn');

            // Form elements
            this.form = {
                name: document.getElementById('agent-name'),
                model: document.getElementById('model-select'),
                embedding: document.getElementById('embedding-select'),
                agentPersona: document.getElementById('agent-persona'),
                humanPersona: document.getElementById('human-persona')
            };

            // Log element status
            console.log('Form elements found:', {
                modal: !!this.modal,
                submitBtn: !!this.submitBtn,
                closeBtn: !!this.closeBtn,
                cancelBtn: !!this.cancelBtn,
                createAgentBtn: !!this.createAgentBtn,
                form: {
                    name: !!this.form.name,
                    model: !!this.form.model,
                    embedding: !!this.form.embedding,
                    agentPersona: !!this.form.agentPersona,
                    humanPersona: !!this.form.humanPersona
                }
            });
        }

        attachEventListeners() {
            console.log('=== Attaching Event Listeners ===');
            
            // Show modal
            if (this.createAgentBtn) {
                console.log('Adding click listener to create button');
                this.createAgentBtn.addEventListener('click', () => {
                    console.log('=== Create Button Clicked ===');
                    this.showModal();
                });
            }

            // Submit form
            if (this.submitBtn) {
                console.log('Adding click listener to submit button');
                this.submitBtn.addEventListener('click', async () => {
                    console.log('=== Submit Button Clicked ===');
                    await this.handleSubmit();
                });
            }

            // Close modal
            if (this.closeBtn) {
                console.log('Adding click listener to close button');
                this.closeBtn.addEventListener('click', () => {
                    console.log('Close button clicked');
                    this.hideModal();
                });
            }

            if (this.cancelBtn) {
                console.log('Adding click listener to cancel button');
                this.cancelBtn.addEventListener('click', () => {
                    console.log('Cancel button clicked');
                    this.hideModal();
                });
            }
        }

        showModal() {
            console.log('=== Showing Modal ===');
            console.log('Modal element exists:', !!this.modal);
            if (this.modal) {
                console.log('Modal before display:', {
                    display: this.modal.style.display,
                    visibility: this.modal.style.visibility
                });
                
                this.modal.style.display = 'block';
                
                console.log('Modal after display:', {
                    display: this.modal.style.display,
                    visibility: this.modal.style.visibility
                });
            }
        }

        hideModal() {
            console.log('Hiding modal');
            this.modal.style.display = 'none';
        }

        resetForm() {
            console.log('Resetting form fields');
            this.nameInput.value = '';
            this.modelSelect.selectedIndex = 0;
            this.embedSelect.selectedIndex = 0;
            this.agentPersona.value = '';
            this.humanPersona.value = '';
        }

        validateForm() {
            console.log('=== Validating Form ===');
            const errors = [];

            // Check required fields
            if (!this.form.name?.value?.trim()) {
                console.error('Name validation failed: empty or missing');
                errors.push('Agent name is required');
            }

            if (!this.form.model?.value) {
                console.error('Model validation failed: no selection');
                errors.push('Please select a model');
            }

            if (!this.form.embedding?.value) {
                console.error('Embedding validation failed: no selection');
                errors.push('Please select an embedding model');
            }

            console.log(`Validation complete: ${errors.length} errors found`);
            if (errors.length > 0) {
                console.error('Validation errors:', errors);
            }

            return errors;
        }

        async handleSubmit() {
            console.log('=== Handling Create Agent Submit ===');
            
            const errors = this.validateForm();
            if (errors.length > 0) {
                console.error('Form validation failed:', errors);
                // TODO: Show errors to user
                return;
            }

            const formData = {
                name: this.form.name.value.trim(),
                model: this.form.model.value,
                embedding: this.form.embedding.value,
                agentPersona: this.form.agentPersona.value.trim(),
                humanPersona: this.form.humanPersona.value.trim()
            };
            
            console.log('Submitting form data:', formData);

            try {
                console.log('Making create_agent API call...');
                const response = await window.pywebview.api.create_agent(formData);
                console.log('Create agent response:', response);
                
                if (response.error) {
                    console.error('API returned error:', response.error);
                    // TODO: Show error to user
                    return;
                }
                
                console.log('Agent created successfully:', response.agent);
                this.hideModal();
                
                // Refresh agent list
                console.log('Refreshing agent list...');
                window.loadAgents();
                
            } catch (error) {
                console.error('Failed to create agent:', error);
                // TODO: Show error to user
            }
        }

        getLLMConfig() {
            const model = this.modelSelect.value;
            switch (model) {
                case 'gpt-4':
                    return {
                        model: 'gpt-4',
                        model_endpoint_type: 'openai',
                        model_endpoint: 'https://api.openai.com/v1',
                        context_window: 8192
                    };
                case 'claude-3':
                    return {
                        model: 'claude-3-opus-20240229',
                        model_endpoint_type: 'anthropic',
                        model_endpoint: 'https://api.anthropic.com/v1',
                        context_window: 200000
                    };
                default:
                    return {
                        model: 'letta-free',
                        model_endpoint_type: 'openai',
                        model_endpoint: 'https://inference.memgpt.ai',
                        context_window: 16384
                    };
            }
        }

        getEmbeddingConfig() {
            return this.embedSelect.value === 'openai' 
                ? {
                    embedding_endpoint_type: 'openai',
                    embedding_endpoint: 'https://api.openai.com/v1',
                    embedding_model: 'text-embedding-ada-002',
                    embedding_dim: 1536,
                    embedding_chunk_size: 300
                }
                : {
                    embedding_endpoint_type: 'hugging-face',
                    embedding_endpoint: 'https://embeddings.memgpt.ai',
                    embedding_model: 'letta-free',
                    embedding_dim: 1024,
                    embedding_chunk_size: 300
                };
        }
    }

    // Initialize with logging
    console.log('=== Create Agent Modal Script Start ===');
    if (document.readyState === 'loading') {
        console.log('Document loading - waiting for DOMContentLoaded');
        document.addEventListener('DOMContentLoaded', () => {
            console.log('DOMContentLoaded fired - initializing modal');
            new CreateAgentModal();
        });
    } else {
        console.log('Document ready - initializing modal immediately');
        new CreateAgentModal();
    }
    console.log('=== Create Agent Modal Script End ===');
    """ 