# guardian/cli/commands.py

import typer
from guardian.cli.main import run_guardian
from guardian.data import history_reader

app = typer.Typer(help="🛡️ Pre-Deploy Guardian – DevOps Helper Agent")

@app.command()
def check():
    """Run pre-deploy checks (no deploy)"""
    run_guardian(deploy=False)

@app.command()
def deploy():
    """Run full pipeline and deploy if allowed"""
    run_guardian(deploy=True)

@app.command()
def history():
    """Show deployment history"""
    history_reader.show_history()

def start():
    app()
