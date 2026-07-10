"""
Mindmap Generator module for AI Software Engineering Dashboard.
Converts JSON artifacts to Mermaid.js mindmap syntax.
Now supports all 20 artifacts.
"""


def generate_mindmap(project_name, json_data):
    """
    Generates valid Mermaid.js mindmap syntax from the project JSON data.
    
    Args:
        project_name (str): The name of the project.
        json_data (dict): The JSON data containing all 20 artifacts.
        
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
            for i, req in enumerate(reqs[:10], 1):
                if isinstance(req, dict):
                    title = req.get('title', 'Untitled')[:40]
                    mm += f"        {req.get('id', 'REQ')}: {title}\n"
                else:
                    mm += f"        REQ-{i:03d} {str(req)[:50]}\n"
    
    # Variables section
    if "variables" in json_data:
        mm += "      Variables\n"
        vars_data = json_data["variables"]
        if isinstance(vars_data, list):
            for var in vars_data[:8]:
                if isinstance(var, dict):
                    mm += f"        {var.get('id', 'VAR')}: {var.get('name', '')}\n"
    
    # Functions section (grouped by module)
    if "functions" in json_data:
        mm += "      Modules & Functions\n"
        funcs = json_data["functions"]
        if isinstance(funcs, list):
            modules = {}
            for fn in funcs:
                if isinstance(fn, dict):
                    mod = fn.get('module', 'common')
                    if mod not in modules:
                        modules[mod] = []
                    modules[mod].append(fn)
            for module, func_list in list(modules.items())[:8]:
                mm += f"        {module}\n"
                for fn in func_list[:5]:
                    fn_name = fn.get('name', '')[:35]
                    mm += f"          {fn_name}\n"
    
    # Pipeline section
    if "pipeline" in json_data:
        mm += "      Pipeline\n"
        pipeline = json_data["pipeline"]
        if isinstance(pipeline, list):
            for stage in pipeline[:6]:
                if isinstance(stage, dict):
                    name = stage.get('name', 'Stage')[:30]
                    mm += f"        {stage.get('id', 'STAGE')}: {name}\n"
    
    # Data Dictionary section
    if "data_contracts" in json_data:
        mm += "      Data Dictionary\n"
        contracts = json_data["data_contracts"]
        if isinstance(contracts, list):
            for contract in contracts[:6]:
                if isinstance(contract, dict):
                    mm += f"        {contract.get('id', 'DC')}: {contract.get('name', '')}\n"
    
    # State Machines section
    if "state_machines" in json_data:
        mm += "      State Machines\n"
        machines = json_data["state_machines"]
        if isinstance(machines, list):
            for machine in machines[:4]:
                if isinstance(machine, dict):
                    entity = machine.get('entity', 'Entity')
                    states_count = len(machine.get('states', []))
                    mm += f"        {machine.get('id', 'SM')}: {entity} ({states_count} states)\n"
    
    # Object Dictionary section (NEW)
    if "object_dictionary" in json_data:
        mm += "      Object Dictionary\n"
        objects = json_data["object_dictionary"]
        if isinstance(objects, list):
            for obj in objects[:6]:
                if isinstance(obj, dict):
                    mm += f"        {obj.get('id', 'OBJ')}: {obj.get('name', '')} ({obj.get('type', 'entity')})\n"
    
    # Event Dictionary section (NEW)
    if "event_dictionary" in json_data:
        mm += "      Event Dictionary\n"
        events = json_data["event_dictionary"]
        if isinstance(events, list):
            for evt in events[:6]:
                if isinstance(evt, dict):
                    mm += f"        {evt.get('id', 'EVT')}: {evt.get('name', '')}\n"
    
    # State Dictionary section (NEW)
    if "state_dictionary" in json_data:
        mm += "      State Dictionary\n"
        states = json_data["state_dictionary"]
        if isinstance(states, list):
            for state in states[:4]:
                if isinstance(state, dict):
                    entity = state.get('entity', 'Entity')
                    mm += f"        {state.get('id', 'STATE')}: {entity}\n"
    
    # Pattern Dictionary section (NEW)
    if "pattern_dictionary" in json_data:
        mm += "      Pattern Dictionary\n"
        patterns = json_data["pattern_dictionary"]
        if isinstance(patterns, list):
            for pat in patterns[:5]:
                if isinstance(pat, dict):
                    mm += f"        {pat.get('id', 'PAT')}: {pat.get('name', '')}\n"
    
    # Feature Registry section (NEW)
    if "feature_registry" in json_data:
        mm += "      Feature Registry\n"
        features = json_data["feature_registry"]
        if isinstance(features, list):
            for feat in features[:5]:
                if isinstance(feat, dict):
                    mm += f"        {feat.get('id', 'FEAT')}: {feat.get('name', '')}\n"
    
    # Build Checklist summary
    if "build_checklist" in json_data:
        checklist = json_data["build_checklist"]
        if isinstance(checklist, list):
            mm += "      Build Checklist\n"
            pending = sum(1 for item in checklist if isinstance(item, dict) and item.get('status') == 'PENDING')
            mm += f"        {len(checklist)} items ({pending} pending)\n"
    
    # Business Rules summary
    if "business_rules" in json_data:
        rules = json_data["business_rules"]
        if isinstance(rules, list) and len(rules) > 0:
            mm += "      Business Rules\n"
            mm += f"        {len(rules)} rules defined\n"
    
    # Test Registry summary
    if "test_cases" in json_data:
        cases = json_data["test_cases"]
        if isinstance(cases, list):
            mm += "      Test Registry\n"
            unit_tests = sum(1 for c in cases if isinstance(c, dict) and c.get('test_type') == 'unit')
            integration_tests = sum(1 for c in cases if isinstance(c, dict) and c.get('test_type') == 'integration')
            mm += f"        {len(cases)} tests ({unit_tests} unit, {integration_tests} integration)\n"
    
    # Forbidden Rules summary
    if "forbidden_rules" in json_data:
        forbidden = json_data["forbidden_rules"]
        if isinstance(forbidden, list) and len(forbidden) > 0:
            mm += "      Forbidden Rules\n"
            mm += f"        {len(forbidden)} rules enforced\n"
    
    # Interaction Matrix summary (NEW)
    if "interaction_matrix" in json_data:
        interactions = json_data["interaction_matrix"]
        if isinstance(interactions, list):
            mm += "      Interaction Matrix\n"
            mm += f"        {len(interactions)} module interactions\n"
    
    # AI Build Guard summary (NEW)
    if "ai_build_guard" in json_data:
        guards = json_data["ai_build_guard"]
        if isinstance(guards, list):
            critical = sum(1 for g in guards if isinstance(g, dict) and g.get('severity') == 'CRITICAL')
            mm += "      AI Build Guard\n"
            mm += f"        {len(guards)} guards ({critical} critical)\n"
    
    return mm
