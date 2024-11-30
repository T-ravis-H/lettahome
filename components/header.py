def get_header_html():
    return """
    <div class="header">
        <h1 class="page-title">Agents</h1>
        <button class="create-agent-btn">+ Create Agent</button>
    </div>
    """

def get_header_styles():
    return """
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .page-title {
        font-size: 24px;
        font-weight: 600;
        margin: 0;
    }
    
    .create-agent-btn {
        background-color: #238636;
        color: #ffffff;
        border: none;
        padding: 6px 16px;
        border-radius: 6px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 14px;
    }
    
    .create-agent-btn:hover {
        background-color: #2ea043;
    }
    """ 