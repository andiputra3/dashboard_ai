"""
AI Software Engineering Dashboard - Main Flask Application
"""

import json
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Import local modules
from lib.storage import init_db, create_project, get_project, get_all_projects, add_test_result, get_test_results
from lib.validator import validate_blueprint
from lib.compiler import compile_to_markdown
from lib.mindmap_generator import generate_mindmap
from lib.stack_adapter import get_test_command
from lib.mock_ai_planner import generate_blueprint

app = Flask(__name__)

# Initialize database on startup
init_db()


@app.route('/')
def index():
    """Render the project hub homepage."""
    projects = get_all_projects()
    return render_template('index.html', projects=projects)


@app.route('/create_project', methods=['POST'])
def create_project_route():
    """
    Create a new project from user input.
    Mocks AI planner, validates, compiles, and saves to DB.
    """
    name = request.form.get('name', '').strip()
    stack = request.form.get('stack', '').strip()
    idea = request.form.get('idea', '').strip()
    
    if not name or not stack or not idea:
        return redirect(url_for('index'))
    
    # Generate mock AI blueprint
    blueprint_json = generate_blueprint(name, stack, idea)
    
    # Validate the blueprint
    validation_result = validate_blueprint(blueprint_json)
    validation_status = 'valid' if validation_result['is_valid'] else 'invalid'
    
    # Compile to markdown
    markdown_content = compile_to_markdown(name, blueprint_json)
    
    # Generate mindmap
    mindmap_content = generate_mindmap(name, blueprint_json)
    
    # Save to database
    project_id = create_project(
        name=name,
        stack=stack,
        idea=idea,
        blueprint_json=json.dumps(blueprint_json),
        markdown_content=markdown_content,
        mindmap_content=mindmap_content,
        validation_status=validation_status
    )
    
    return redirect(url_for('project_detail', project_id=project_id))


@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Render the project dashboard."""
    project = get_project(project_id)
    
    if not project:
        return redirect(url_for('index'))
    
    test_results = get_test_results(project_id)
    
    return render_template('project.html', project=project, test_results=test_results)


@app.route('/run_tests/<int:project_id>', methods=['POST'])
def run_tests(project_id):
    """
    Run tests for a project using the stack adapter.
    Returns mock success JSON for demo purposes.
    """
    project = get_project(project_id)
    
    if not project:
        return jsonify({'success': False, 'error': 'Project not found'}), 404
    
    # Get test command from stack adapter
    stack = project['stack']
    test_command = get_test_command(stack)
    
    # Mock test execution output
    mock_output = f"""Running tests for {project['name']}...
=====================================
Test Suite: {stack}
Command: {test_command}

test_auth_login ... PASSED
test_auth_logout ... PASSED
test_api_get_users ... PASSED
test_api_create_user ... PASSED
test_utils_validate_input ... PASSED

-------------------------------------
Ran 5 tests in 0.123s

OK
All tests passed successfully!
"""
    
    # Save test result to database
    add_test_result(
        project_id=project_id,
        test_command=test_command,
        output=mock_output,
        success=True
    )
    
    return jsonify({
        'success': True,
        'test_command': test_command,
        'output': mock_output
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=False)
