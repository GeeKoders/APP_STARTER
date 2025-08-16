import pytest
from tools.math import add


class TestAdd:
    """Test cases for the add function."""

    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        result = add(2, 3)
        assert result == 5
        assert isinstance(result, (int, float))

    def test_add_positive_floats(self):
        """Test adding two positive floats."""
        result = add(2.5, 3.5)
        assert result == 6.0
        assert isinstance(result, float)

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add(-2, -3)
        assert result == -5
        assert isinstance(result, (int, float))

    def test_add_mixed_positive_negative(self):
        """Test adding positive and negative numbers."""
        result = add(5, -3)
        assert result == 2
        assert isinstance(result, (int, float))

    def test_add_with_zero(self):
        """Test adding zero to a number."""
        result = add(5, 0)
        assert result == 5
        assert isinstance(result, (int, float))

    def test_add_zero_to_zero(self):
        """Test adding zero to zero."""
        result = add(0, 0)
        assert result == 0
        assert isinstance(result, (int, float))

    def test_add_large_numbers(self):
        """Test adding large numbers."""
        result = add(1000000, 2000000)
        assert result == 3000000
        assert isinstance(result, (int, float))

    def test_add_small_decimals(self):
        """Test adding small decimal numbers."""
        result = add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10  # Account for floating point precision
        assert isinstance(result, float)

    def test_add_very_small_numbers(self):
        """Test adding very small numbers."""
        result = add(1e-10, 2e-10)
        assert result == 3e-10
        assert isinstance(result, float)

    def test_add_integer_and_float(self):
        """Test adding integer and float."""
        result = add(5, 2.5)
        assert result == 7.5
        assert isinstance(result, float)