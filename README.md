# Build an Agent - Agent Development Example

This repository demonstrates how to build and run custom AI agents using the OpenCode framework. It includes a working example of a coding partner agent similar to the one you've been interacting with.

## What Is an Agent?

An agent in OpenCode is an AI assistant with specialized capabilities, configuration, and tools designed for specific tasks. Agents can be customized with:

- **Specialized instructions** (how the agent should behave)
- **Tool access** (what capabilities the agent has)
- **Model selection** (which AI model to use)
- **Custom skills** (domain-specific knowledge and workflows)

## Repository Contents

This repository contains:
- A working **coding partner agent** configuration (`.opencode/agent/coding-partner.md`)
- **Agent configuration** (`opencode.json`)
- **Example project files** (the calculator demo) showing what an agent can help build
- Documentation on how to create and run your own agents

## How Agents Like This Work

When you interact with an agent like me, here's what happens behind the scenes:

1. **Configuration Loading**: OpenCode loads the agent's configuration from `.opencode/agent/*` files
2. **Tool Setup**: The agent is granted access to specific tools (bash, edit, read, write, etc.)
3. **Model Initialization**: The specified AI model is initialized with the provider settings
4. **Instruction Following**: The agent follows its built-in instructions plus any custom instructions in its config
5. **Tool Execution**: When needed, the agent uses its available tools to accomplish tasks

## Key Configuration Files

### 1. Agent Definition (`.opencode/agent/coding-partner.md`)
```yaml
---
description: A friendly general-purpose coding partner
mode: primary
model: navigator/nemotron-3-super-120b-a12b
tools:
  write: true
  edit: true
  bash: true
  # ... other tools
---
```
This file defines:
- What the agent does (description)
- How it operates (mode)
- Which AI model to use
- What tools it has access to

### 2. Main Configuration (`opencode.json`)
```json
{
  "provider": {
    "navigator": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "UF NaviGator",
      "options": {
        "baseURL": "https://api.ai.it.ufl.edu/v1",
        "apiKey": "{env:NAVIGATOR_API_KEY}"
      },
      "models": {
        "nemotron-3-super-120b-a12b": { "name": "Nemotron 3 Super 120B" },
        "nemotron-3-nano-30b-a3b": { "name": "Nemotron 3 Nano 30B" }
      }
    }
  },
  "model": "navigator/nemotron-3-super-120b-a12b"
}
```
This file configures:
- Which AI providers are available
- API endpoints and authentication
- Available models
- Default model selection

## How to Build Your Own Agent

### Step 1: Set Up the Directory Structure
```bash
mkdir -p .opencode/agent
```

### Step 2: Create Your Agent Configuration
Create `.opencode/agent/your-agent-name.md`:
```yaml
---
description: [What your agent does]
mode: primary  # or "agent" or "orchestrator"
model: [your-provider/your-model]
tools:
  read: true
  write: true
  edit: true
  bash: true
  # Add other tools your agent needs
---
[Your agent's instructions here]
```

### Step 3: Configure Provider and Models
Edit `opencode.json` to add your AI provider:
```json
{
  "provider": {
    "your-provider-name": {
      "npm": "[the-npm-package]",
      "name": "[Display Name]",
      "options": {
        "baseURL": "[API endpoint]",
        "apiKey": "{env:YOUR_API_KEY_ENV_VAR}"
      },
      "models": {
        "your-provider/your-model": { "name": "[Model Display Name]" }
      }
    }
  },
  "model": "your-provider/your-model"
}
```

### Step 4: Set Environment Variables
Set required API keys as environment variables:
```bash
export YOUR_API_KEY_ENV_VAR="your-actual-api-key"
```

### Step 5: Run Your Agent
Start OpenCode and select your agent:
```bash
opencode
```
Then choose your agent from the agent selection menu.

## Available Tools

Agents can be granted access to various tools:
- **File operations**: `read`, `write`, `edit`, `glob`, `grep`
- **System operations**: `bash` (for running commands)
- **Development aids**: `task` (for spawning subagents), `todowrite` (for task management)
- **Integrations**: `webfetch`, `skill` (for loading specialized skills)

## Modes Explained

- **`primary`**: The main agent that interacts directly with the user
- **`agent`**: Standard subagents that can be spawned for specific tasks
- **`orchestrator`**: Agents that manage and coordinate other agents

## Customizing Agent Behavior

You can customize your agent by:

1. **Modifying instructions**: Edit the text after the YAML frontmatter in your agent's `.md` file
2. **Adjusting tool access**: Add or remove tools in the `tools:` section
3. **Changing models**: Update the `model:` field to use different AI models
4. **Adding skills**: Use the `skill` tool to load specialized capabilities

## Example: Creating a Specialized Agent

To create a data analysis agent:

1. Create `.opencode/agent/data-analyst.md`:
```yaml
---
description: A data analysis specialist
mode: primary
model: navigator/nemotron-3-super-120b-a12b
tools:
  read: true
  write: true
  edit: true
  bash: true
  webfetch: true
  # Add data-specific tools if available
---
You are a data analysis expert. Help users:
- Clean and preprocess datasets
- Perform statistical analysis
- Create data visualizations
- Interpret results and draw conclusions
- Explain statistical concepts in simple terms
```

2. Add any required provider/model configuration to `opencode.json`
3. Set environment variables for API keys
4. Run and select your new agent

## Best Practices

1. **Start Simple**: Begin with a basic agent and gradually add capabilities
2. **Be Specific**: Clear instructions lead to better performance
3. **Limit Tools**: Only grant tools your agent actually needs
4. **Test Iteratively**: Try your agent with simple tasks first
5. **Document**: Keep track of what works well for your specific use case

## Extending with Skills

Agents can load specialized skills for domains like:
- Web browsing (`built-in-browser`, `chrome-browser`)
- File operations (`pdf`, `xlsx`, `docx`, `pptx`)
- Data analysis and visualization
- Specific frameworks or languages

Use the `skill` tool within your agent's instructions or load them automatically based on context.

## Troubleshooting

**Agent not responding?**
- Check that your API key is set correctly
- Verify the model name matches exactly what's in your provider configuration
- Ensure the agent file has valid YAML frontmatter

**Tools not working?**
- Confirm the tool is listed in your agent's `tools:` section
- Check that any required dependencies are installed
- Verify file permissions for bash operations

**Model errors?**
- Ensure the provider is correctly configured
- Check that the model exists for that provider
- Verify API credentials and quotas

## Learning More

To explore advanced agent capabilities:
1. Look at the skills directory for pre-built capabilities
2. Experiment with different model providers
3. Try creating subagents for complex tasks using the `task` tool
4. Use `todowrite` for managing multi-step workflows

This repository serves as a starting point—you can use the calculator project as a testbed for developing and refining your own agents.

---

*Built with OpenCode - Customize, extend, and create AI agents tailored to your specific needs.*