import subprocess
import sys
import os

def testgetbest(csv_file, expected_output):#Get the absolute path to the csv file
    csv_path = os.path.join(os.path.dirname(__file__), "..", csv_file)
    
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "..", "getbest.py"), csv_path],
        capture_output=True,
        text=True
    )
    
    print(f"STDOUT: '{result.stdout.strip()}'")
    print(f"STDERR: '{result.stderr.strip()}'")
    print(f"Expected: '{expected_output}'")
    print(f"Return code: {result.returncode}")
    
    assert result.returncode == 0, "Program crashed"
    assert result.stdout.strip() == expected_output
    print(f"✓ {csv_file}")

if __name__ == "__main__":
    testgetbest("testdat0.csv", "The top student was student 167381 with 90")
    print("All tests passed")
