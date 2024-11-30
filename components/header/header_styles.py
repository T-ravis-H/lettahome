def get_header_styles():
    return """
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .page-title {
        margin: 0;
        font-size: 24px;
        color: #ffffff;
    }

    .create-agent-btn {
        background-color: #238636;
        color: #ffffff;
        border: none;
        padding: 8px 16px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        transition: background-color 0.2s;
    }

    .create-agent-btn:hover {
        background-color: #2ea043;
    }

    .create-agent-btn:active {
        background-color: #ff0000 !important;  /* Red when clicked */
    }
    """ 