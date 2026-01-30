# guardian/engine/decision_engine.py

class DecisionEngine:
    def __init__(self, context: dict):
        self.context = context
        self.decision = "ALLOW"
        self.reasons = []

    def check_tests(self):
        if self.context.get("tests_detected") and not self.context.get("tests_passed"):
            self.decision = "BLOCK"
            self.reasons.append("Tests detected but not passed")

    def check_security(self):
        if self.context.get("critical_vulnerabilities", 0) > 0:
            self.decision = "BLOCK"
            self.reasons.append("Critical security vulnerabilities found")

    def check_risk_policy(self):
        if self.context.get("risk_level") == "low" and self.context.get("tests_detected"):
            if not self.context.get("tests_passed"):
                self.decision = "BLOCK"
                self.reasons.append(
                    "Low-risk policy requires passing tests when tests exist"
                )

    def run(self):
        self.check_tests()
        self.check_security()
        self.check_risk_policy()

        return {
            "decision": self.decision,
            "reasons": self.reasons
        }
