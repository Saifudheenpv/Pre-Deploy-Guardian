# guardian/engine/deploy_executor.py

import subprocess

class DeployExecutor:
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.image_name = "guardian_sample_app"
        self.container_name = "guardian_sample_container"

    def build_image(self):
        result = subprocess.run(
            ["docker", "build", "-t", self.image_name, "."],
            cwd=self.repo_path
        )
        return result.returncode == 0

    def run_container(self):
        subprocess.run(
            ["docker", "rm", "-f", self.container_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        result = subprocess.run(
            ["docker", "run", "--name", self.container_name, self.image_name]
        )
        return result.returncode == 0

    def rollback(self):
        subprocess.run(
            ["docker", "rm", "-f", self.container_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
