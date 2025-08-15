# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python MCP (Model Context Protocol) server that provides document conversion tools. The server exposes tools through FastMCP for converting various document formats to markdown using the `markitdown` library.

## Key Commands

### Development Environment Setup
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies in development mode
uv pip install -e .
```

### Running the Application
```bash
# Start the MCP server
uv run main.py
```

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_document.py

# Run with verbose output
uv run pytest -v
```

## Architecture

### Core Components

- **main.py**: Entry point that creates a FastMCP server instance and registers tools
- **tools/**: Contains tool implementations that get exposed through the MCP server
  - **math.py**: Simple mathematical operations (currently just addition)
  - **document.py**: Document conversion utilities using MarkItDown
- **tests/**: Test suite with fixtures for document conversion testing

### MCP Server Pattern

The application follows the FastMCP pattern:
1. Tools are defined as Python functions with pydantic Field annotations
2. Tools are registered with the MCP server using the `@mcp.tool()` decorator
3. The server exposes these tools through the MCP protocol

### Tool Development Guidelines

When adding new tools:
- Use pydantic `Field` for parameter descriptions
- Include comprehensive docstrings with:
  - One-line summary
  - Detailed functionality explanation
  - When to use/not use the tool
  - Usage examples with expected input/output
- Register tools in main.py using `mcp.tool()(function_name)`

### Dependencies

- **markitdown**: Document conversion (with docx and pdf support)
- **mcp[cli]**: MCP server framework
- **pydantic**: Data validation and type annotations
- **pytest**: Testing framework

### Test Structure

Tests use fixtures stored in `tests/fixtures/` (mcp_docs.docx, mcp_docs.pdf) to verify document conversion functionality. Each test module should include fixture existence verification.
- Always apply appropriate types to function args