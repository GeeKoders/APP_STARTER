import os
import pytest
import tempfile


class TestDocumentPathToMarkdown:
    # Define fixture paths
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_fixture_files_exist(self):
        """Verify test fixtures exist."""
        assert os.path.exists(self.DOCX_FIXTURE), (
            f"DOCX fixture not found at {self.DOCX_FIXTURE}"
        )
        assert os.path.exists(self.PDF_FIXTURE), (
            f"PDF fixture not found at {self.PDF_FIXTURE}"
        )

    def test_document_path_to_markdown_with_pdf(self):
        """Test converting a PDF document to markdown using file path."""
        # Import here to avoid issues if tool doesn't exist yet
        from tools.document import document_path_to_markdown
        
        # Call function with PDF file path
        result = document_path_to_markdown(self.PDF_FIXTURE)

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_with_docx(self):
        """Test converting a DOCX document to markdown using file path."""
        # Import here to avoid issues if tool doesn't exist yet
        from tools.document import document_path_to_markdown
        
        # Call function with DOCX file path
        result = document_path_to_markdown(self.DOCX_FIXTURE)

        # Basic assertions to check the conversion was successful
        assert isinstance(result, str)
        assert len(result) > 0
        # Check for typical markdown formatting - this will depend on your actual test file
        assert "#" in result or "-" in result or "*" in result

    def test_document_path_to_markdown_file_not_found(self):
        """Test error handling when file does not exist."""
        # Import here to avoid issues if tool doesn't exist yet
        from tools.document import document_path_to_markdown
        
        non_existent_path = "/path/that/does/not/exist.pdf"
        
        with pytest.raises(FileNotFoundError):
            document_path_to_markdown(non_existent_path)

    def test_document_path_to_markdown_invalid_file_type(self):
        """Test error handling for unsupported file types."""
        # Import here to avoid issues if tool doesn't exist yet
        from tools.document import document_path_to_markdown
        
        # Create a temporary text file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
            temp_file.write("This is a plain text file")
            temp_path = temp_file.name
        
        try:
            # Should handle unsupported file type gracefully
            # The exact behavior will depend on implementation - might raise ValueError or return empty string
            with pytest.raises((ValueError, Exception)):
                document_path_to_markdown(temp_path)
        finally:
            # Clean up temporary file
            os.unlink(temp_path)

    def test_document_path_to_markdown_corrupted_file(self):
        """Test behavior with corrupted/malformed files."""
        # Import here to avoid issues if tool doesn't exist yet
        from tools.document import document_path_to_markdown
        
        # Create a temporary file with corrupted PDF content
        with tempfile.NamedTemporaryFile(mode='wb', suffix='.pdf', delete=False) as temp_file:
            temp_file.write(b"This is not a valid PDF file content")
            temp_path = temp_file.name
        
        try:
            # MarkItDown handles corrupted files gracefully by treating them as text
            result = document_path_to_markdown(temp_path)
            assert isinstance(result, str)
            # The corrupted content should be returned as-is
            assert "This is not a valid PDF file content" in result
        finally:
            # Clean up temporary file
            os.unlink(temp_path)