def get_navbar_html():
    return """
    <nav class="sidebar">
        <div class="logo">Letta</div>
        <div class="nav-item active">
            <span>Agents</span>
        </div>
        <div class="nav-item">
            <span>Data Sources</span>
        </div>
        <div class="nav-item">
            <span>Tool Builder</span>
        </div>
        <div class="nav-item">
            <span>Agent Templates</span>
        </div>
        <div class="nav-item">
            <span>User Templates</span>
        </div>
        <div class="nav-item">
            <span>Settings</span>
        </div>
    </nav>
    """

def get_navbar_styles():
    return """
    .sidebar {
        width: 240px;
        background-color: #0D1117;
        border-right: 1px solid #21262d;
        padding: 20px 0;
        display: flex;
        flex-direction: column;
    }
    
    .logo {
        padding: 0 20px;
        margin-bottom: 20px;
        font-size: 24px;
        font-weight: bold;
    }
    
    .nav-item {
        padding: 10px 20px;
        color: #8b949e;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .nav-item.active {
        background-color: #21262d;
        color: #ffffff;
    }
    """ 