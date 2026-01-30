# guardian/cli/main.py

from guardian.engine.decision_engine import DecisionEngine
from guardian.engine.repo_analyzer import RepoAnalyzer
from guardian.engine.test_executor import TestExecutor
from guardian.engine.deploy_executor import DeployExecutor
from guardian.rules.context import DEFAULT_CONTEXT
from guardian.utils.audit_logger import log_event

def run_guardian(deploy: bool = False):
    print("🛡️  Pre-Deploy Guardian\n")

    repo_path = "examples/sample_app"

    # PLAN
    analyzer = RepoAnalyzer(repo_path)
    repo_context = analyzer.analyze()

    context = DEFAULT_CONTEXT.copy()
    context.update(repo_context)

    # TEST
    if context.get("tests_detected") and context.get("language") == "python":
        executor = TestExecutor(repo_path)
        context["tests_passed"] = executor.run_python_tests()

    engine = DecisionEngine(context)
    result = engine.run()

    print("Repository analysis:")
    print("- Language:", context["language"])
    print("- Tests detected:", context["tests_detected"])
    print("- Tests passed:", context["tests_passed"])

    print("\nDecision:", result["decision"])

    event = {
        "repo": repo_path,
        "decision": result["decision"],
        "reasons": result["reasons"]
    }

    if deploy and result["decision"] == "ALLOW":
        print("\n🚀 Deploying application...")
        deployer = DeployExecutor(repo_path)

        if deployer.build_image() and deployer.run_container():
            print("Deployment successful ✅")
            event["status"] = "DEPLOYED"
        else:
            print("Deployment failed ❌ — rolling back")
            deployer.rollback()
            event["status"] = "ROLLED_BACK"

    elif deploy:
        print("\n🚫 Deployment blocked by Pre-Deploy Guardian")
        for r in result["reasons"]:
            print("-", r)
        event["status"] = "BLOCKED"
    else:
        event["status"] = "CHECK_ONLY"

    log_event(event)
