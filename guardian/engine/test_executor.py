# guardian/engine/test_executor.py

import subprocess
import os

class TestExecutor:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def run_python_tests(self):
        try:
            result = subprocess.run(
                ["python3", "-m", "pytest"],
                cwd=self.repo_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return result.returncode == 0
        except Exception:
            return False
