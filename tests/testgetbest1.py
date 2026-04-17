import subprocess
import sys
import os

def run_test(csv_file, expected_output, test_name):
    csv_path = os.path.join(os.path.dirname(__file__), "..", csv_file)
    
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "..", "getbest.py"), csv_path],
        capture_output=True,
        text=True
    )
    
    print(f"\n--- Test: {test_name} ---")
    print(f"Input file: {csv_file}")
    print(f"Expected: {expected_output}")
    print(f"Got: {result.stdout.strip()}")
    
    assert result.returncode == 0, f"Fail: Program crashed"
    assert result.stdout.strip() == expected_output, f"Fail: Output mismatch"
    print(f"Pass: {test_name}")
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("Running tests for getbest.py")
    print("=" * 50)

    # TEST 1: Original data
    run_test("bestdat0.csv", "The top student was student 167381 with 90", "original data")
    
    # TEST 2: Different column order (mark first)
    run_test("testdat1_markfirst.csv", "The top student was student 167381 with 50", "different column order")
    
    # TEST 3: Different number of students (one)
    run_test("testdat2_onestudent.csv", "The top student was student 160001 with 72", "one student")
    
    # TEST 4: Different order of marks (ascending)
    run_test("testdat3_marksascending.csv", "The top student was student 167381 with 99", "marks in ascending order")
    
    # TEST 5: Different order of marks (descending)
    run_test("testdat4_marksdescending.csv", "The top student was student 167381 with 99", "marks in descending order")

    print("\n" + "=" * 50)
    print("All tests passed")
    print("=" * 50)