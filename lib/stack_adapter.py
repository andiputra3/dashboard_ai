"""
Stack Adapter module for AI Software Engineering Dashboard.
Maps programming languages/stacks to their respective test commands.
"""

STACK_TEST_COMMANDS = {
    "python": "pytest",
    "python3": "pytest",
    "django": "python manage.py test",
    "flask": "pytest",
    "fastapi": "pytest",
    "javascript": "npm test",
    "js": "npm test",
    "node": "npm test",
    "nodejs": "npm test",
    "typescript": "npm test",
    "ts": "npm test",
    "react": "npm test",
    "vue": "npm test",
    "angular": "npm test",
    "java": "mvn test",
    "maven": "mvn test",
    "gradle": "./gradlew test",
    "go": "go test ./...",
    "golang": "go test ./...",
    "rust": "cargo test",
    "ruby": "rake test",
    "rails": "rails test",
    "php": "phpunit",
    "laravel": "php artisan test",
    "c#": "dotnet test",
    "csharp": "dotnet test",
    "dotnet": "dotnet test",
    "cpp": "make test",
    "c++": "make test",
    "c": "make test",
    "swift": "swift test",
    "kotlin": "./gradlew test",
    "scala": "sbt test",
    "r": "Rscript -e 'testthat::test_dir(\"tests\")'",
    "bash": "bats tests",
    "shell": "bats tests",
}


def get_test_command(stack):
    """
    Gets the appropriate test command for a given stack/language.
    
    Args:
        stack (str): The programming language or framework.
        
    Returns:
        str: The test command, or a default command if stack not found.
    """
    stack_lower = stack.lower().strip()
    
    # Direct lookup
    if stack_lower in STACK_TEST_COMMANDS:
        return STACK_TEST_COMMANDS[stack_lower]
    
    # Partial match
    for key, command in STACK_TEST_COMMANDS.items():
        if key in stack_lower or stack_lower in key:
            return command
    
    # Default fallback
    return "echo 'No test command configured for this stack'"


def get_available_stacks():
    """
    Returns a list of available stacks with their test commands.
    
    Returns:
        dict: Mapping of stack names to test commands.
    """
    return STACK_TEST_COMMANDS.copy()
