# Jaqpot MCP Server

Model Context Protocol (MCP) server for Jaqpot platform integration. This server allows LLMs to interact with the Jaqpot API for machine learning model predictions and discovery.

## Features

- **Model Predictions**: Execute predictions using Jaqpot models with the jaqpot-python-sdk
- **Model Search**: Search and discover models by description and features
- **Authentication**: Secure API access using client key and secret
- **Docker Support**: Containerized deployment ready for Kubernetes

## Quick Start

### Environment Variables

```bash
export JAQPOT_API_KEY="your-client-key"
export JAQPOT_API_SECRET="your-secret-key"
```

### Running with Docker

```bash
docker build -t jaqpot-mcp-server .
docker run -p 8000:8000 \
  -e JAQPOT_API_KEY="your-client-key" \
  -e JAQPOT_API_SECRET="your-secret-key" \
  jaqpot-mcp-server
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

1. Clone the repository:
```bash
git clone https://github.com/ntua-unit-of-control-and-informatics/jaqpot-mcp-server.git
cd jaqpot-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export JAQPOT_API_KEY="your-client-key"
export JAQPOT_API_SECRET="your-secret-key"
```

4. Run the server:
```bash
python -m jaqpot_mcp_server
```

### Testing

Run the example usage:
```bash
python examples/usage_example.py
```

## License

See [LICENSE](LICENSE) file.