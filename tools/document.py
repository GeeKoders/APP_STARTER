import logging
from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field
import os

logger = logging.getLogger(__name__)


def binary_document_to_markdown(
    binary_data: bytes = Field(description="Raw binary data of the document to convert"),
    file_type: str = Field(description="File extension/type (e.g., 'docx', 'pdf', 'txt')")
) -> str:
    """Convert binary document data to markdown-formatted text.
    
    Takes binary document data and converts it to markdown using the MarkItDown library.
    Supports various document formats including PDF, DOCX, and other common formats.
    
    When to use:
    - When you need to convert document formats to markdown for text processing
    - When working with binary document data that needs to be made readable
    - When you want to extract structured text content from documents
    
    When not to use:
    - For plain text files that don't need conversion
    - For documents that are already in markdown format
    
    Examples:
    >>> with open("document.docx", "rb") as f:
    ...     binary_data = f.read()
    >>> result = binary_document_to_markdown(binary_data, "docx")
    >>> print(result)
    # Document Title
    
    This is the document content...
    """
    logger.info(f"Converting binary document of type: {file_type}, size: {len(binary_data)} bytes")
    
    try:
        md = MarkItDown()
        file_obj = BytesIO(binary_data)
        stream_info = StreamInfo(extension=file_type)
        result = md.convert(file_obj, stream_info=stream_info)
        
        logger.info(f"Successfully converted binary document to markdown, output length: {len(result.text_content)} characters")
        return result.text_content
    except Exception as e:
        logger.error(f"Failed to convert binary document of type {file_type}: {e}")
        raise


def document_path_to_markdown(
    file_path: str = Field(description="Path to the document file (PDF or DOCX) to convert")
) -> str:
    """Convert a document file to markdown-formatted text.
    
    Takes a file path to a document and converts it to markdown using the MarkItDown library.
    Supports PDF and DOCX document formats.
    
    When to use:
    - When you have a file path to a PDF or DOCX document that needs conversion
    - When you want to extract structured text content from local document files
    - When you need to convert document formats to markdown for text processing
    
    When not to use:
    - For documents that are already in markdown format
    - For binary data that you already have in memory (use binary_document_to_markdown instead)
    - For unsupported file formats
    
    Examples:
    >>> result = document_path_to_markdown("/path/to/document.pdf")
    >>> print(result)
    # Document Title
    
    This is the document content...
    
    >>> result = document_path_to_markdown("/path/to/document.docx")
    >>> print(result)
    # Another Document
    
    More content here...
    """
    logger.info(f"Processing document conversion for file: {file_path}")
    
    # Check if file exists
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get file extension to determine type
    _, ext = os.path.splitext(file_path)
    file_type = ext.lower().lstrip('.')
    logger.debug(f"Detected file type: {file_type}")
    
    # Validate supported file types
    supported_types = {'pdf', 'docx'}
    if file_type not in supported_types:
        logger.error(f"Unsupported file type: {file_type}. Supported types: {supported_types}")
        raise ValueError(f"Unsupported file type: {file_type}. Supported types: {supported_types}")
    
    # Read file as binary data
    try:
        with open(file_path, 'rb') as f:
            binary_data = f.read()
        logger.debug(f"Successfully read file: {file_path}, size: {len(binary_data)} bytes")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        raise Exception(f"Error reading file {file_path}: {str(e)}")
    
    # Convert using existing binary_document_to_markdown function
    try:
        result = binary_document_to_markdown(binary_data, file_type)
        logger.info(f"Successfully converted document: {file_path}")
        return result
    except Exception as e:
        logger.error(f"Error converting document {file_path}: {str(e)}")
        raise Exception(f"Error converting document {file_path}: {str(e)}")
