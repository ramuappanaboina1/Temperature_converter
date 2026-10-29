from app import celsius_to_fahrenheit, fahrenheit_to_celsius, main
from unittest.mock import patch

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

@patch('builtins.input', side_effect=['1', '0'])
def test_main_celsius_flow(mock_input):
    try:
        main()
    except Exception as e:
        assert False, f"Main function failed: {e}"

@patch('builtins.input', side_effect=['2', '32'])
def test_main_fahrenheit_flow(mock_input):
    try:
        main()
    except Exception as e:
        assert False, f"Main function failed: {e}"
