import logging
from mcp.server.fastmcp import FastMCP
from tools.math import add
from tools.document import binary_document_to_markdown, document_path_to_markdown

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('mcp_server.log')
    ]
)

logger = logging.getLogger(__name__)

mcp = FastMCP("docs")

mcp.tool()(add)
mcp.tool()(binary_document_to_markdown)
mcp.tool()(document_path_to_markdown)

if __name__ == "__main__":
    logger.info("Starting MCP server")
    try:
        mcp.run()
    except Exception as e:
        logger.error(f"Failed to start MCP server: {e}")
        raise
