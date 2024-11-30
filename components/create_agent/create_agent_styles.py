def get_create_agent_modal_styles():
    return """
    /* Modal Base */
    .modal {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        z-index: 1000;
    }

    .modal-content {
        position: relative;
        background-color: #0D1117;
        margin: 5% auto;
        padding: 20px;
        width: 70%;
        max-width: 700px;
        border-radius: 8px;
        border: 1px solid #30363d;
    }

    /* Header */
    .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #30363d;
    }

    .modal-header h2 {
        color: #ffffff;
        margin: 0;
        font-size: 1.5em;
    }

    .close-button {
        background: none;
        border: none;
        color: #8b949e;
        font-size: 24px;
        cursor: pointer;
    }

    /* Form Elements */
    .form-group {
        margin-bottom: 20px;
    }

    .form-group label {
        display: block;
        color: #c9d1d9;
        margin-bottom: 8px;
    }

    .help-text {
        color: #8b949e;
        font-size: 0.9em;
        margin-top: 4px;
    }

    .form-input,
    .form-select,
    .form-textarea {
        width: 100%;
        padding: 8px 12px;
        background-color: #21262d;
        border: 1px solid #30363d;
        border-radius: 6px;
        color: #c9d1d9;
        font-size: 14px;
    }

    .form-textarea {
        min-height: 100px;
        resize: vertical;
    }

    /* Footer */
    .modal-footer {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #30363d;
    }

    /* Buttons */
    .button {
        padding: 8px 16px;
        border-radius: 6px;
        font-size: 14px;
        cursor: pointer;
        border: 1px solid transparent;
    }

    .button-primary {
        background-color: #238636;
        color: #ffffff;
    }

    .button-secondary {
        background-color: #21262d;
        color: #c9d1d9;
        border-color: #30363d;
    }

    .button:hover {
        opacity: 0.9;
    }
    """ 