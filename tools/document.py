from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field


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
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content
