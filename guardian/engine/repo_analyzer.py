# guardian/engine/repo_analyzer.py

import os

class RepoAnalyzer:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path

    def is_python_project(self):
        return os.path.exists(os.path.join(self.repo_path, "requirements.txt"))

    def has_tests(self):
        for file in os.listdir(self.repo_path):
            if file.startswith("test_") and file.endswith(".py"):
                return True
        return False

    def analyze(self):
        context = {}

        context["language"] = "python" if self.is_python_project() else "unknown"
        context["tests_detected"] = self.has_tests()

        return context
