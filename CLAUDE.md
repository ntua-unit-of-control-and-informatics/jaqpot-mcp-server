# Jaqpot MCP Server - Claude Development Context

This document provides context for Claude/AI assistants working on the Jaqpot MCP Server project.

## Project Overview

The Jaqpot MCP Server is a Model Context Protocol (MCP) server that enables Large Language Models (LLMs) to interact with the Jaqpot platform for machine learning model predictions and discovery. This server acts as a bridge between LLMs and the Jaqpot API, providing structured access to model predictions, search, and metadata.

## Architecture

### Core Components

1. **MCP Server** (`src/jaqpot_mcp_server/server.py`)
   - Main server implementation using the MCP protocol
   - Handles tool registration and execution
   - Manages authentication with Jaqpot API
   - Provides error handling and logging

2. **Jaqpot Integration**
   - Uses `jaqpot-python-sdk` for API communication
   - Authenticates using API key and secret
   - Supports synchronous predictions
   - Handles model discovery and metadata retrieval

3. **MCP Tools**
   - `jaqpot_predict`: Execute model predictions
   - `jaqpot_search_models`: Search for available models
   - `jaqpot_get_model_info`: Get detailed model information
   - `jaqpot_get_model_summary`: Get model summary with features

## Key Files and Their Purpose

### Source Code
- `src/jaqpot_mcp_server/__init__.py` - Package initialization
- `src/jaqpot_mcp_server/__main__.py` - Module entry point
- `src/jaqpot_mcp_server/server.py` - Main MCP server implementation

### Configuration
- `pyproject.toml` - Python project configuration and dependencies
- `requirements.txt` - Python dependencies for Docker
- `docker-compose.yml` - Docker composition for easy deployment
- `Dockerfile` - Container configuration

### Documentation
- `README.md` - User-facing documentation
- `CLAUDE.md` - This file, AI assistant context
- `LICENSE` - MIT license
- `examples/usage_example.py` - Example client usage

## Dependencies

### Core Dependencies
- `mcp>=1.0.0` - Model Context Protocol framework
- `jaqpot-python-sdk>=0.1.0` - Jaqpot platform integration
- `pydantic>=2.0.0` - Data validation and settings management
- `uvicorn>=0.20.0` - ASGI server (optional, for HTTP deployment)
- `fastapi>=0.100.0` - Web framework (optional, for HTTP endpoints)

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-asyncio>=0.21.0` - Async testing support
- `black>=23.0.0` - Code formatting
- `isort>=5.12.0` - Import sorting
- `mypy>=1.0.0` - Type checking

## Environment Variables

Required for operation:
- `JAQPOT_API_KEY` - Jaqpot client API key
- `JAQPOT_API_SECRET` - Jaqpot API secret

Optional:
- `PYTHONPATH` - Set to `/app/src` in containerized environments
- `PYTHONUNBUFFERED=1` - For better logging in containers

## API Integration

### Jaqpot Python SDK Usage

The server uses the following key methods from the Jaqpot SDK:

```python
# Client initialization
client = JaqpotApiClient(api_key=key, api_secret=secret)

# Model operations
model = client.get_model_by_id(model_id)
summary = client.get_model_summary(model_id)
models = client.get_shared_models(page=0, size=20)

# Predictions
result = client.predict_sync(model_id, dataset)
```

### MCP Tool Schemas

Each tool has a defined JSON schema for input validation:

1. **jaqpot_predict**
   - `model_id` (integer, required) - Jaqpot model ID
   - `dataset` (array, required) - Input data as list of objects

2. **jaqpot_search_models**
   - `page` (integer, optional) - Page number for pagination
   - `size` (integer, optional) - Results per page
   - `organization_id` (integer, optional) - Filter by organization

3. **jaqpot_get_model_info**
   - `model_id` (integer, required) - Jaqpot model ID

4. **jaqpot_get_model_summary**
   - `model_id` (integer, required) - Jaqpot model ID

## Error Handling

The server handles several types of errors:

- `JaqpotApiException` - General API errors
- `JaqpotPredictionFailureException` - Prediction-specific failures
- `JaqpotPredictionTimeoutException` - Prediction timeouts
- General `Exception` - Catch-all for unexpected errors

All errors are logged and returned as user-friendly error messages through the MCP protocol.

## Development Guidelines

### Code Style
- Use Black for code formatting (line length: 88)
- Use isort for import organization
- Follow type hints with mypy checking
- Use descriptive variable and function names

### Testing
- Write async tests using pytest-asyncio
- Test both success and error cases
- Mock external API calls when appropriate
- Include integration tests with real API (when safe)

### Logging
- Use Python's logging module
- Log at appropriate levels (INFO for operations, ERROR for failures)
- Include contextual information in log messages

## Common Tasks

### Adding New MCP Tools

1. Add tool definition in `_register_tools()` method
2. Create handler method (e.g., `_handle_new_tool()`)
3. Add tool call routing in `call_tool()` method
4. Update documentation

### Modifying API Integration

1. Check jaqpot-python-sdk documentation for new methods
2. Update error handling for new exception types
3. Test with different data formats
4. Update tool schemas if input/output changes

### Deployment Updates

1. Update version in `pyproject.toml` and `__init__.py`
2. Test Docker build locally
3. Verify environment variable handling
4. Check resource requirements

## Security Considerations

- API keys are handled securely via environment variables
- No sensitive data should be logged
- Input validation prevents injection attacks
- Error messages don't expose sensitive system information

## Performance Notes

- Predictions use synchronous API calls (blocking)
- Consider timeout handling for long-running predictions
- Memory usage depends on dataset size for predictions
- Connection pooling handled by jaqpot-python-sdk

## Troubleshooting

### Common Issues

1. **Authentication failures**: Check API key/secret configuration
2. **Model not found**: Verify model ID and permissions
3. **Prediction failures**: Check input data format and model requirements
4. **Connection errors**: Verify network connectivity to Jaqpot API

### Debugging

- Enable detailed logging by setting appropriate log levels
- Use the example client for testing server functionality
- Check Docker logs for containerized deployments
- Verify environment variables are set correctly

## Future Enhancements

Potential areas for improvement:
- Asynchronous prediction support
- Batch prediction capabilities
- Model deployment functionality
- Enhanced search and filtering options
- Caching for frequently accessed models
- WebSocket support for real-time updates

## Related Documentation

- [Jaqpot Platform Documentation](https://docs.jaqpot.org)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Jaqpot Python SDK](https://github.com/ntua-unit-of-control-and-informatics/jaqpot-python-sdk)
- [FastAPI Documentation](https://fastapi.tiangolo.com) (for HTTP extensions)

## Testing Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python -m jaqpot_mcp_server

# Run example client
python examples/usage_example.py

# Run tests (when implemented)
pytest

# Format code
black src/ examples/
isort src/ examples/

# Type checking
mypy src/

# Build Docker image
docker build -t jaqpot-mcp-server .

# Run with Docker Compose
docker-compose up
```