"""
Compiler module for AI Software Engineering Dashboard.
Compiles JSON artifacts to a final_spec_{project}.md markdown file.
"""


def compile_to_markdown(project_name, json_data):
    """
    Generates a clean Markdown string with all 13 sections formatted nicely.
    
    Args:
        project_name (str): The name of the project.
        json_data (dict): The JSON data containing all 13 artifacts.
        
    Returns:
        str: The compiled markdown content.
    """
    md = f"# {project_name} - Final Specification\n\n"
    md += "---\n\n"
    md += f"**Project:** {project_name}\n"
    if "stack" in json_data:
        md += f"**Stack:** {json_data['stack']}\n"
    if "idea" in json_data:
        md += f"**Idea:** {json_data['idea']}\n"
    md += "\n---\n\n"
    
    # 1. Requirements (REQ-xxx)
    if "requirements" in json_data:
        md += "## 1. Requirements (REQ-xxx)\n\n"
        reqs = json_data["requirements"]
        if isinstance(reqs, list):
            for req in reqs:
                if isinstance(req, dict):
                    md += f"### {req.get('id', 'REQ')}: {req.get('title', 'Untitled')}\n\n"
                    md += f"- **Description:** {req.get('description', '')}\n"
                    md += f"- **Sprint:** {req.get('sprint', '')}\n"
                    md += f"- **Status:** {req.get('status', '')}\n"
                    trace = req.get('trace', {})
                    if trace:
                        md += f"- **Trace:** modules={trace.get('modules', [])}, files={trace.get('files', [])}\n"
                    md += "\n"
                else:
                    md += f"- {req}\n"
        md += "\n"
    
    # 2. Variables (VAR-xxx)
    if "variables" in json_data:
        md += "## 2. Variables (VAR-xxx)\n\n"
        vars_data = json_data["variables"]
        if isinstance(vars_data, list):
            md += "| ID | Name | Type | Value | Scope |\n"
            md += "|----|------|------|-------|-------|\n"
            for var in vars_data:
                if isinstance(var, dict):
                    md += f"| {var.get('id', '')} | {var.get('name', '')} | {var.get('type', '')} | {var.get('value', '')} | {var.get('scope', '')} |\n"
        elif isinstance(vars_data, dict):
            for key, value in vars_data.items():
                md += f"- `{key}`: {value}\n"
        md += "\n"
    
    # 3. Functions (FN-xxx)
    if "functions" in json_data:
        md += "## 3. Functions (FN-xxx)\n\n"
        funcs = json_data["functions"]
        if isinstance(funcs, list):
            md += "| ID | Name | Module | File | Description |\n"
            md += "|----|------|--------|------|-------------|\n"
            for fn in funcs:
                if isinstance(fn, dict):
                    md += f"| {fn.get('id', '')} | {fn.get('name', '')} | {fn.get('module', '')} | {fn.get('file', '')} | {fn.get('description', '')} |\n"
        elif isinstance(funcs, dict):
            for module, func_list in funcs.items():
                md += f"### Module: {module}\n\n"
                if isinstance(func_list, list):
                    for fn in func_list:
                        md += f"- `{fn}`\n"
                md += "\n"
        md += "\n"
    
    # 4. Pipeline (STAGE-xxx)
    if "pipeline" in json_data:
        md += "## 4. Pipeline (STAGE-xxx)\n\n"
        pipeline = json_data["pipeline"]
        if isinstance(pipeline, list):
            for stage in pipeline:
                if isinstance(stage, dict):
                    md += f"### {stage.get('id', 'STAGE')}: {stage.get('name', '')}\n\n"
                    md += f"- **Order:** {stage.get('order', '')}\n"
                    md += f"- **Functions:** {stage.get('functions', [])}\n"
                    md += f"- **On Error:** {stage.get('on_error', '')}\n\n"
        md += "\n"
    
    # 5. Build Checklist (CHK-xxx)
    if "build_checklist" in json_data:
        md += "## 5. Build Checklist (CHK-xxx)\n\n"
        checklist = json_data["build_checklist"]
        if isinstance(checklist, list):
            md += "| ID | Description | Linked REQ | Priority | Status |\n"
            md += "|----|-------------|------------|----------|--------|\n"
            for item in checklist:
                if isinstance(item, dict):
                    md += f"| {item.get('id', '')} | {item.get('description', '')} | {item.get('linked_req', '')} | {item.get('priority', '')} | {item.get('status', '')} |\n"
        md += "\n"
    
    # 6. Project Blueprint (DIR-xxx)
    if "project_blueprint" in json_data:
        md += "## 6. Project Blueprint (DIR-xxx)\n\n"
        blueprint = json_data["project_blueprint"]
        if isinstance(blueprint, dict):
            dirs = blueprint.get('directories', [])
            if dirs:
                md += "### Directory Structure\n\n"
                for d in dirs:
                    if isinstance(d, dict):
                        md += f"- **{d.get('id', 'DIR')}**: `{d.get('path', '')}` ({d.get('type', '')})\n"
                        allowed = d.get('allowed_files', [])
                        if allowed:
                            md += f"  - Allowed files: {', '.join(allowed)}\n"
            root_files = blueprint.get('root_files', [])
            if root_files:
                md += f"\n### Root Files\n\n"
                for f in root_files:
                    md += f"- `{f}`\n"
        md += "\n"
    
    # 7. Data Contracts (DC-xxx)
    if "data_contracts" in json_data:
        md += "## 7. Data Contracts (DC-xxx)\n\n"
        contracts = json_data["data_contracts"]
        if isinstance(contracts, list):
            for contract in contracts:
                if isinstance(contract, dict):
                    md += f"### {contract.get('id', 'DC')}: {contract.get('name', '')}\n\n"
                    md += f"- **Type:** {contract.get('type', '')}\n"
                    if contract.get('table'):
                        md += f"- **Table:** `{contract.get('table', '')}`\n"
                    fields = contract.get('fields', [])
                    if fields:
                        md += "- **Fields:**\n"
                        for field in fields:
                            if isinstance(field, dict):
                                md += f"  - `{field.get('name', '')}` ({field.get('type', '')}) - {field.get('constraints', [])}\n"
                    md += "\n"
        md += "\n"
    
    # 8. State Machines (SM-xxx)
    if "state_machines" in json_data:
        md += "## 8. State Machines (SM-xxx)\n\n"
        machines = json_data["state_machines"]
        if isinstance(machines, list):
            for machine in machines:
                if isinstance(machine, dict):
                    md += f"### {machine.get('id', 'SM')}: {machine.get('entity', '')} ({machine.get('module', '')})\n\n"
                    states = machine.get('states', [])
                    md += f"- **States:** {' → '.join(states)}\n"
                    transitions = machine.get('transitions', [])
                    if transitions:
                        md += "- **Transitions:**\n"
                        for t in transitions:
                            md += f"  - {t.get('from', '')} → {t.get('to', '')} (trigger: {t.get('trigger', '')}, condition: {t.get('condition', '')})\n"
                    md += "\n"
        md += "\n"
    
    # 9. Dependency Matrix (DEP-xxx)
    if "dependency_matrix" in json_data:
        md += "## 9. Dependency Matrix (DEP-xxx)\n\n"
        matrix = json_data["dependency_matrix"]
        if isinstance(matrix, list):
            md += "| ID | Caller | Target | Allowed | Forbidden |\n"
            md += "|----|--------|--------|---------|-----------|\n"
            for row in matrix:
                if isinstance(row, dict):
                    allowed = ', '.join(row.get('allowed_functions', [])) or 'None'
                    forbidden = ', '.join(row.get('forbidden_functions', [])) or 'None'
                    md += f"| {row.get('id', '')} | {row.get('caller_module', '')} | {row.get('target_module', '')} | {allowed} | {forbidden} |\n"
        md += "\n"
    
    # 10. Business Rules (BR-xxx)
    if "business_rules" in json_data:
        md += "## 10. Business Rules (BR-xxx)\n\n"
        rules = json_data["business_rules"]
        if isinstance(rules, list):
            for rule in rules:
                if isinstance(rule, dict):
                    md += f"### {rule.get('id', 'BR')}: {rule.get('name', '')}\n\n"
                    md += f"- **Formula:** `{rule.get('formula', '')}`\n"
                    constraints = rule.get('constraints', [])
                    if constraints:
                        md += f"- **Constraints:** {', '.join(constraints)}\n"
                    md += f"- **Linked Function:** {rule.get('linked_fn', '')}\n\n"
        md += "\n"
    
    # 11. Test Cases (TC-xxx)
    if "test_cases" in json_data:
        md += "## 11. Test Cases (TC-xxx)\n\n"
        cases = json_data["test_cases"]
        if isinstance(cases, list):
            for case in cases:
                if isinstance(case, dict):
                    md += f"### {case.get('id', 'TC')}: {case.get('title', '')}\n\n"
                    md += f"- **Type:** {case.get('type', '')}\n"
                    md += f"- **Linked Function:** {case.get('linked_fn', '')}\n"
                    md += f"- **Linked Requirement:** {case.get('linked_req', '')}\n"
                    steps = case.get('steps', [])
                    if steps:
                        md += "- **Steps:**\n"
                        for step in steps:
                            md += f"  - {step}\n"
                    md += f"- **Expected Result:** {case.get('expected_result', '')}\n\n"
        md += "\n"
    
    # 12. Forbidden Rules (FR-xxx)
    if "forbidden_rules" in json_data:
        md += "## 12. Forbidden Rules (FR-xxx)\n\n"
        forbidden = json_data["forbidden_rules"]
        if isinstance(forbidden, list):
            md += "| ID | Rule | Scope | Severity |\n"
            md += "|----|------|-------|----------|\n"
            for rule in forbidden:
                if isinstance(rule, dict):
                    md += f"| {rule.get('id', '')} | ❌ {rule.get('rule', '')} | {rule.get('scope', '')} | {rule.get('severity', '')} |\n"
        md += "\n"
    
    # 13. ID Tracking
    if "id_tracking" in json_data:
        md += "## 13. ID Tracking\n\n"
        tracking = json_data["id_tracking"]
        if isinstance(tracking, dict):
            md += f"- **Rule:** {tracking.get('rule', '')}\n"
            md += f"- **Enforcement:** {tracking.get('enforcement', '')}\n"
            md += f"- **Action on Violation:** {tracking.get('action_on_violation', '')}\n"
            patterns = tracking.get('id_patterns', {})
            if patterns:
                md += "\n### ID Patterns\n\n"
                for artifact_type, pattern in patterns.items():
                    md += f"- **{artifact_type}:** `{pattern}`\n"
        md += "\n"
    
    md += "---\n\n"
    md += "*Generated by AI Software Engineering Dashboard*\n"
    
    return md
