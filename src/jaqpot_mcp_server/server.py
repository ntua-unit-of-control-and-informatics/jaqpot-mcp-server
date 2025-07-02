"""MCP Server implementation for Jaqpot platform integration using FastMCP."""

import os
import logging
from typing import Any, Dict, List, Optional

from jaqpot_python_sdk.exceptions.exceptions import (
    JaqpotPredictionFailureException,
    JaqpotPredictionTimeoutException,
    JaqpotApiException,
)
from fastmcp import FastMCP
from jaqpot_python_sdk.jaqpot_api_client import JaqpotApiClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP
mcp = FastMCP("jaqpot-mcp-server")

# Initialize Jaqpot API client
api_key = os.getenv("JAQPOT_API_KEY")
api_secret = os.getenv("JAQPOT_API_SECRET")

if not api_key or not api_secret:
    raise ValueError("JAQPOT_API_KEY and JAQPOT_API_SECRET must be provided")

jaqpot_client = JaqpotApiClient(api_key=api_key, api_secret=api_secret)


@mcp.tool
def jaqpot_predict(model_id: int, dataset: List[Dict[str, Any]]) -> str:
    """Make predictions using a Jaqpot model.
    
    Args:
        model_id: The ID of the Jaqpot model
        dataset: Input data for prediction (list of dictionaries)
        
    Returns:
        Prediction results as a string
    """
    if not model_id or not dataset:
        return "Error: model_id and dataset are required"
    
    try:
        result = jaqpot_client.predict_sync(model_id, dataset)
        return f"Prediction successful for model {model_id}:\\n{result}"
    except JaqpotPredictionFailureException as e:
        return f"Prediction failed: {str(e)}"
    except JaqpotPredictionTimeoutException as e:
        return f"Prediction timed out: {str(e)}"
    except JaqpotApiException as e:
        return f"API error: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error in jaqpot_predict: {str(e)}")
        return f"Unexpected error: {str(e)}"


@mcp.tool
def jaqpot_search_models(
    query: str,
    page: int = 0, 
    size: int = 20, 
) -> str:
    """Search for Jaqpot models by criteria.
    
    Args:
        query: Query to search for models
        page: Page number for pagination (default: 0)
        size: Number of results per page (default: 20)

    Returns:
        Search results as a string
    """
    try:
        response = jaqpot_client.search_models(
            query=query,
            page=page,
            size=size,
        )
        
        models = response.data.to_dict() if hasattr(response.data, 'to_dict') else response.data
        return f"Found models:\\n{models}"
    except JaqpotApiException as e:
        return f"Search failed: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error in jaqpot_search_models: {str(e)}")
        return f"Unexpected error: {str(e)}"


@mcp.tool
def jaqpot_get_model_info(model_id: int) -> str:
    """Get detailed information about a specific Jaqpot model.
    
    Args:
        model_id: The ID of the Jaqpot model
        
    Returns:
        Model information as a string
    """
    if not model_id:
        return "Error: model_id is required"
    
    try:
        model = jaqpot_client.get_model_by_id(model_id)
        return f"Model {model_id} info:\\n{model}"
    except JaqpotApiException as e:
        return f"Failed to get model info: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error in jaqpot_get_model_info: {str(e)}")
        return f"Unexpected error: {str(e)}"


@mcp.tool
def jaqpot_get_model_summary(model_id: int) -> str:
    """Get a summary of a Jaqpot model including features and description.
    
    Args:
        model_id: The ID of the Jaqpot model
        
    Returns:
        Model summary as a string
    """
    if not model_id:
        return "Error: model_id is required"
    
    try:
        summary = jaqpot_client.get_model_summary(model_id)
        return f"Model {model_id} summary:\\n{summary}"
    except JaqpotApiException as e:
        return f"Failed to get model summary: {str(e)}"
    except Exception as e:
        logger.error(f"Unexpected error in jaqpot_get_model_summary: {str(e)}")
        return f"Unexpected error: {str(e)}"


def main():
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
