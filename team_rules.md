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
4. Project List Management:
   - Update `project_list.md` when priorities change
   - Add new ideas to the backlog section
   - Move completed items to the "Completed" section with completion date
   - Use checkmarks [x] for completed items
5. Follow the component-based structure with co-located logic

## Git & GitHub Workflow

### Repository Setup
- Main repository: https://github.com/T-ravis-H/lettahome
- Store GitHub token as environment variable (GH_TOKEN)
- Never commit the token or any sensitive data

### Branch Management
- Main branch: `main` (primary branch)
- Feature branches: `feature/[feature-name]`
- Bug fix branches: `fix/[bug-name]`
- Never commit directly to main branch

### Basic Workflow Commands
1. Clone repository:
   ```bash
   git clone https://github.com/T-ravis-H/lettahome.git
   ```

2. Configure git (one-time setup):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

3. Daily workflow:
   ```bash
   # Get latest changes
   git pull origin main

   # Create new branch
   git checkout -b feature/your-feature

   # Add changes
   git add .

   # Commit changes
   git commit -m "Descriptive message about changes"

   # Push changes
   git push origin feature/your-feature
   ```

4. Merging changes:
   - Create Pull Request on GitHub
   - Review code
   - Merge after approval

### Commit Message Guidelines
- Use clear, descriptive messages
- Start with a verb (Add, Update, Fix, Refactor)
- Keep it concise but informative
- Example: "Add navbar component with theme toggle"

### Common Issues & Solutions
1. Authentication issues:
   - Ensure GH_TOKEN environment variable is set
   - Use token in remote URL: 
     ```bash
     git remote set-url origin https://$GH_TOKEN@github.com/T-ravis-H/lettahome.git
     ```

2. Branch conflicts:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

3. Force push (use cautiously):
   ```bash
   git push -f origin branch-name
   ```

Note: This document will be updated as new decisions are made or practices are refined. 