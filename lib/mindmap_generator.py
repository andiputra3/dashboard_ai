"""
Mindmap Generator module for AI Software Engineering Dashboard.
Converts JSON artifacts to Mermaid.js mindmap syntax.
"""


def generate_mindmap(project_name, json_data):
    """
    Generates valid Mermaid.js mindmap syntax from the project JSON data.
    
    Args:
        project_name (str): The name of the project.
        json_data (dict): The JSON data containing artifacts.
        
    Returns:
        str: The Mermaid mindmap syntax.
    """
    mm = "mindmap\n"
    mm += f"  root(({project_name}))\n"
    
    # Requirements section
    if "requirements" in json_data:
        mm += "      Requirements\n"
        reqs = json_data["requirements"]
        if isinstance(reqs, list):
            for i, req in enumerate(reqs[:10], 1):  # Limit to 10 for readability
                req_str = str(req)[:50]  # Truncate long strings
                mm += f"        REQ-{i:03d} {req_str}\n"
        elif isinstance(reqs, dict):
            for key, value in list(reqs.items())[:10]:
                mm += f"        {key}: {str(value)[:30]}\n"
    
    # Functions section (grouped by module)
    if "functions" in json_data:
        mm += "      Modules\n"
        funcs = json_data["functions"]
        if isinstance(funcs, dict):
            for module, func_list in list(funcs.items())[:8]:
                mm += f"        {module}\n"
                if isinstance(func_list, list):
                    for fn in func_list[:5]:  # Limit functions per module
                        fn_str = str(fn)[:40]
                        mm += f"          {fn_str}\n"
                else:
                    mm += f"          {str(func_list)[:40]}\n"
        elif isinstance(funcs, list):
            for fn in funcs[:15]:
                fn_str = str(fn)[:40]
                mm += f"        {fn_str}\n"
    
    # Pipeline section
    if "pipeline" in json_data:
        mm += "      Pipeline\n"
        pipeline = json_data["pipeline"]
        if isinstance(pipeline, list):
            for i, stage in enumerate(pipeline[:10], 1):
                stage_str = str(stage)[:40]
                mm += f"        Stage {i} {stage_str}\n"
        elif isinstance(pipeline, dict):
            for key, value in list(pipeline.items())[:10]:
                mm += f"        {key}: {str(value)[:30]}\n"
    
    # Build Checklist summary
    if "build_checklist" in json_data:
        checklist = json_data["build_checklist"]
        if isinstance(checklist, list):
            mm += "      Build Checklist\n"
            mm += f"        {len(checklist)} items to complete\n"
    
    # Business Rules summary
    if "business_rules" in json_data:
        rules = json_data["business_rules"]
        if isinstance(rules, list) and len(rules) > 0:
            mm += "      Business Rules\n"
            mm += f"        {len(rules)} rules defined\n"
    
    # Test Cases summary
    if "test_cases" in json_data:
        cases = json_data["test_cases"]
        if isinstance(cases, list):
            mm += "      Test Cases\n"
            mm += f"        {len(cases)} test cases\n"
    
    return mm
