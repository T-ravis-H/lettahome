# Team Rules & Project Guidelines

## Code Organization
- Using component-based architecture with co-located logic
- Each component has its own directory containing both UI and logic files
- Components are modular and reusable

## Logging Standards
We use centralized logging configuration for consistent logging across all components.

### Logging Setup
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file='app.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1024*1024, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatting
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
```

### Usage Example
```python
# In component files:
logger = setup_logger(__name__)

logger.debug("Detailed information for debugging")
logger.info("General information about program execution")
logger.warning("Warning messages for potentially problematic situations")
logger.error("Error messages for serious problems")
```

## Security & Configuration
- API keys and sensitive data are stored as environment variables
- Never commit sensitive data to version control
- Use `.env` files locally (added to .gitignore)

## Project Resources

### Documentation
- [Letta Documentation](https://docs.letta.com/introduction)
- [Letta Python SDK](https://docs.letta.com/python-reference/LocalClient)
- [Letta API Reference](https://docs.letta.com/api-reference/tools/get-tool)
- [Letta GitHub Repository](https://github.com/letta-ai/letta)

### Project Assets
- LettaSDKDemos folder: Contains proven real-world examples of Letta Python SDK implementation
- Lucide icon set for UI components

### Team Resources
- GPT: Our resident Letta expert available for collaboration and mini-guides
- Project tracking in `project_list.md`

## Development Practices
1. Always use the centralized logging system
2. Keep components modular and independent
3. Document any major architectural decisions
4. Update `project_list.md` when priorities change
5. Follow the component-based structure with co-located logic

## Component Structure Example
```
/components
  /navbar
    - NavBar.py (UI Component)
    - navbar_logic.py (Component Logic)
    - __init__.py
```

## Version Control Practices
- Meaningful commit messages
- Regular commits with atomic changes
- Keep feature branches up to date with main

Note: This document will be updated as new decisions are made or practices are refined. 