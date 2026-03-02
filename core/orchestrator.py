from core.ai_engine.factory import get_ai_engine

class Orchestrator:
    
    def __init__(self):
        self.engine = get_ai_engine()
    
    def process(self, request: str) -> dict:
        intent = self._detect_intent(request)
        prompt = self._build_prompt(intent, request)
        response = self.engine.generate(prompt)
        
        return {
            "intent": intent,
            "request": request,
            "response": response
        }
    
    def _detect_intent(self, request: str) -> str:
        request_lower = request.lower()
        
        if any(word in request_lower for word in ["fix", "bug", "error", "issue"]):
            return "bug_fix"
        elif any(word in request_lower for word in ["review", "check", "analyze"]):
            return "code_review"
        elif any(word in request_lower for word in ["create", "build", "generate", "add"]):
            return "code_generation"
        else:
            return "general"
    
    def _build_prompt(self, intent: str, request: str) -> str:
        prompts = {
            "bug_fix": f"""You are an expert software engineer.
A developer needs help fixing a bug.
Request: {request}
Provide a clear fix with explanation. Format your response with:
1. Root cause
2. Fixed code
3. Explanation of the fix""",

            "code_review": f"""You are an expert software engineer.
A developer wants you to review their code.
Request: {request}
Provide a thorough review with:
1. Issues found
2. Suggested improvements
3. Corrected code if needed""",

            "code_generation": f"""You are an expert software engineer.
A developer needs new code generated.
Request: {request}
Provide:
1. The complete code
2. How to use it
3. Any important notes""",

            "general": f"""You are an expert software engineer.
A developer has the following request: {request}
Provide the most helpful response possible."""
        }
        
        return prompts[intent]