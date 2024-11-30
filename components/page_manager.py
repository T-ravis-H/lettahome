def get_page_manager_js():
    return """
    class PageManager {
        constructor() {
            this.currentPage = 'agents';
            this.currentAgentId = null;
        }
        
        async navigateToChat(agentId) {
            this.currentPage = 'chat';
            this.currentAgentId = agentId;
            await this.renderCurrentPage();
        }
        
        async navigateToAgents() {
            this.currentPage = 'agents';
            this.currentAgentId = null;
            await this.renderCurrentPage();
        }
        
        async renderCurrentPage() {
            const mainContent = document.querySelector('.main-content');
            
            if (this.currentPage === 'agents') {
                mainContent.innerHTML = `
                    ${window.components.header}
                    ${window.components.search}
                    ${window.components.agentsTable}
                `;
                await loadAgents();
            } else if (this.currentPage === 'chat') {
                mainContent.innerHTML = window.components.chatConfig;
                await loadChatConfig(this.currentAgentId);
            }
        }
    }
    
    window.pageManager = new PageManager();
    """ 