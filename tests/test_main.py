import pytest
from mcp.server.fastmcp import FastMCP


class TestMain:
    """Test cases for the main.py MCP server setup."""

    def test_mcp_server_creation(self):
        """Test that FastMCP server is created with correct name."""
        # Import here to avoid running main code during import
        import main
        
        assert isinstance(main.mcp, FastMCP)
        # Check that the server has the expected name
        assert main.mcp.name == "docs"

    def test_tools_registration(self):
        """Test that all tools are properly registered with the MCP server."""
        # Import here to avoid running main code during import
        import main
        
        # Get the registered tool names
        tool_names = list(main.mcp._tool_manager._tools.keys())
        
        # Check that all expected tools are registered
        expected_tools = ["add", "binary_document_to_markdown", "document_path_to_markdown"]
        for tool_name in expected_tools:
            assert tool_name in tool_names, f"Tool '{tool_name}' is not registered"

    def test_add_tool_function(self):
        """Test that the add tool function is accessible through the server."""
        import main
        
        # Check that the add tool is registered
        assert "add" in main.mcp._tool_manager._tools
        
        # Get the tool function
        add_tool = main.mcp._tool_manager._tools["add"]
        
        # Test the function works
        result = add_tool.fn(2, 3)
        assert result == 5

    def test_binary_document_tool_function(self):
        """Test that the binary_document_to_markdown tool is accessible."""
        import main
        
        # Check that the tool is registered
        assert "binary_document_to_markdown" in main.mcp._tool_manager._tools
        
        # Verify the tool exists and has the expected function
        tool = main.mcp._tool_manager._tools["binary_document_to_markdown"]
        assert tool.fn is not None

    def test_document_path_tool_function(self):
        """Test that the document_path_to_markdown tool is accessible."""
        import main
        
        # Check that the tool is registered
        assert "document_path_to_markdown" in main.mcp._tool_manager._tools
        
        # Verify the tool exists and has the expected function
        tool = main.mcp._tool_manager._tools["document_path_to_markdown"]
        assert tool.fn is not None

    def test_main_module_has_run_capability(self):
        """Test that the main module has the capability to run the server."""
        import main
        
        # Verify that the mcp object has a run method
        assert hasattr(main.mcp, 'run')
        assert callable(main.mcp.run)