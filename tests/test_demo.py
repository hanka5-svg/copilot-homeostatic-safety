import subprocess
import sys
import os

def test_demo_runs_without_errors():
    """
    Minimal smoke test: verifies that demo.py executes without raising exceptions.
    """
    demo_path = os.path.join(os.path.dirname(__file__), "..", "demo.py")
    result = subprocess.run([sys.executable, demo_path], capture_output=True, text=True)

    # Process should exit with code 0
    assert result.returncode == 0, f"demo.py failed: {result.stderr}"
