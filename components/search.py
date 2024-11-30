def get_search_html():
    return """
    <input type="text" 
           class="search-box" 
           placeholder="Search"
           aria-label="Search agents">
    """

def get_search_styles():
    return """
    .search-box {
        background-color: #0D1117;
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 8px 12px;
        color: #ffffff;
        width: 300px;
        margin-bottom: 20px;
        font-size: 14px;
    }
    
    .search-box::placeholder {
        color: #8b949e;
    }
    """ 