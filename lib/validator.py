"""
Validator module for AI Software Engineering Dashboard.
Validates the 20 artifact keys from the AI planner JSON.
"""

REQUIRED_KEYS = [
    # Original 13 Artifacts
    "variables",
    "functions",
    "pipeline",
    "build_checklist",
    "project_blueprint",
    "data_contracts",
    "state_machines",
    "dependency_matrix",
    "business_rules",
    "test_cases",
    "forbidden_rules",
    "requirements",
    "id_tracking",
    # NEW 7 Artifacts
    "object_dictionary",
    "event_dictionary",
    "state_dictionary",
    "pattern_dictionary",
    "feature_registry",
    "interaction_matrix",
    "ai_build_guard"
]


def validate_blueprint(json_data):
    """
    Validates that the JSON data contains all 20 required artifact keys.
    
    Args:
        json_data (dict): The JSON data from the AI planner.
        
    Returns:
        dict: {"is_valid": bool, "missing_keys": list, "total_artifacts": int, "found_artifacts": int}
    """
    if not isinstance(json_data, dict):
        return {
            "is_valid": False, 
            "missing_keys": REQUIRED_KEYS,
            "total_artifacts": len(REQUIRED_KEYS),
            "found_artifacts": 0
        }
    
    missing_keys = []
    for key in REQUIRED_KEYS:
        if key not in json_data:
            missing_keys.append(key)
    
    return {
        "is_valid": len(missing_keys) == 0,
        "missing_keys": missing_keys,
        "total_artifacts": len(REQUIRED_KEYS),
        "found_artifacts": len(REQUIRED_KEYS) - len(missing_keys)
    }
