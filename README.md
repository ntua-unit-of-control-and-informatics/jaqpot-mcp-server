# Jaqpot MCP Server

Model Context Protocol (MCP) server for Jaqpot platform integration. This server allows LLMs to interact with the Jaqpot API for machine learning model predictions and discovery.

## Features

- **Model Predictions**: Execute predictions using Jaqpot models with the jaqpot-python-sdk
- **Model Search**: Search and discover models by description and features
- **Authentication**: Secure API access using client key and secret
- **MCP Integration**: Full Model Context Protocol compliance for seamless LLM integration

## Installation

### Prerequisites

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install Python 3.10+ using uv:
   ```bash
   uv python install 3.10
   ```

3. Configure your Jaqpot API credentials:
   - Get your API key and secret from [Jaqpot platform](https://app.jaqpot.org)
   - Set them as environment variables (see Configuration section)

### Install the Server

```bash
# Clone the repository
git clone https://github.com/ntua-unit-of-control-and-informatics/jaqpot-mcp-server.git
cd jaqpot-mcp-server

# Install with uv
uv sync
```

## Configuration

### Environment Variables

Set your Jaqpot API credentials:

```bash
export JAQPOT_API_KEY="your-api-key"
export JAQPOT_API_SECRET="your-api-secret"
```

### MCP Client Configuration

Add the server to your MCP client configuration. For Claude Desktop, add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "jaqpot": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory", "/path/to/jaqpot-mcp-server",
        "run", "server.py"
      ],
      "env": {
        "JAQPOT_API_KEY": "your-api-key",
        "JAQPOT_API_SECRET": "your-api-secret"
      }
    }
  }
}
```

Replace `/path/to/jaqpot-mcp-server` with the actual path to your cloned repository.

### Alternative: Direct Python Execution

```json
{
  "mcpServers": {
    "jaqpot": {
      "type": "stdio",
      "command": "python",
      "args": ["/path/to/jaqpot-mcp-server/server.py"],
      "env": {
        "JAQPOT_API_KEY": "your-api-key",
        "JAQPOT_API_SECRET": "your-api-secret"
      }
    }
  }
}
```

## Usage

### Running the Server

```bash
# With uv (recommended)
uv run server.py

# Or directly with Python
python server.py
```

### Testing the Installation

Run the example usage script:

```bash
uv run python examples/usage_example.py
```

## MCP Tools Available

### 1. `jaqpot_predict`
Make predictions using a Jaqpot model.

**Parameters:**
- `model_id` (int): The ID of the Jaqpot model
- `dataset` (list): Input data for prediction

### 2. `jaqpot_search_models`
Search for models by criteria.

**Parameters:**
- `query` (str): Search query
- `page` (int, optional): Page number for pagination
- `size` (int, optional): Number of results per page

### 3. `jaqpot_get_model_info`
Get detailed information about a specific model.

**Parameters:**
- `model_id` (int): The ID of the Jaqpot model

## Development

### Local Development

1. Clone the repository and install dependencies:
```bash
git clone https://github.com/ntua-unit-of-control-and-informatics/jaqpot-mcp-server.git
cd jaqpot-mcp-server
uv sync --dev
```

2. Set environment variables:
```bash
export JAQPOT_API_KEY="your-api-key"
export JAQPOT_API_SECRET="your-api-secret"
```

3. Run the server:
```bash
uv run server.py
```

### Testing

Run the example usage:
```bash
uv run python examples/usage_example.py
```


## License

See [LICENSE](LICENSE) file.