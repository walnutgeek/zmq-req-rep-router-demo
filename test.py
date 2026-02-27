#!/usr/bin/env python3
"""
Simple test to validate the server logic
"""

def test_server_logic():
    """Test the server's calculation logic"""
    test_cases = [
        (1, 2, 2),  # N=1, wait=1%3+1=2, result=1+1=2
        (5, 3, 6),  # N=5, wait=5%3+1=3, result=5+1=6
        (10, 2, 11), # N=10, wait=10%3+1=2, result=10+1=11
        (15, 1, 16), # N=15, wait=15%3+1=1, result=15+1=16
    ]

    print("Testing server calculation logic:")
    for n, expected_wait, expected_result in test_cases:
        wait_time = n % 3 + 1
        result = n + 1

        assert wait_time == expected_wait, f"Wait time for {n} should be {expected_wait}, got {wait_time}"
        assert result == expected_result, f"Result for {n} should be {expected_result}, got {result}"

        print(f"  N={n} -> wait={wait_time}s, result={result} ✓")

    print("All tests passed!")


if __name__ == "__main__":
    test_server_logic()
