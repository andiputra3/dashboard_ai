"""
Storage module for AI Software Engineering Dashboard.
Handles SQLite database setup and CRUD operations.
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dashboard.db")


def get_db_connection():
    """
    Creates and returns a database connection.
    
    Returns:
        sqlite3.Connection: Database connection object.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Initializes the database with required tables.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create projects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stack TEXT NOT NULL,
            idea TEXT NOT NULL,
            blueprint_json TEXT,
            markdown_content TEXT,
            mindmap_content TEXT,
            validation_status TEXT DEFAULT 'pending',
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create test_results table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER NOT NULL,
            test_command TEXT,
            output TEXT,
            success BOOLEAN,
            executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    ''')
    
    conn.commit()
    conn.close()


def create_project(name, stack, idea, blueprint_json, markdown_content, mindmap_content, validation_status):
    """
    Creates a new project in the database.
    
    Args:
        name (str): Project name.
        stack (str): Technology stack.
        idea (str): Project idea/description.
        blueprint_json (str): JSON string of the blueprint.
        markdown_content (str): Compiled markdown content.
        mindmap_content (str): Mermaid mindmap syntax.
        validation_status (str): Validation status ('valid' or 'invalid').
        
    Returns:
        int: The ID of the newly created project.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO projects (name, stack, idea, blueprint_json, markdown_content, mindmap_content, validation_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, stack, idea, blueprint_json, markdown_content, mindmap_content, validation_status))
    
    project_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return project_id


def get_project(project_id):
    """
    Retrieves a project by its ID.
    
    Args:
        project_id (int): The project ID.
        
    Returns:
        dict or None: Project data as a dictionary, or None if not found.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM projects WHERE id = ?', (project_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return dict(row)
    return None


def get_all_projects():
    """
    Retrieves all projects from the database.
    
    Returns:
        list: List of project dictionaries.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def update_project(project_id, **kwargs):
    """
    Updates a project with the given fields.
    
    Args:
        project_id (int): The project ID.
        **kwargs: Fields to update.
        
    Returns:
        bool: True if update was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    fields = []
    values = []
    for key, value in kwargs.items():
        fields.append(f"{key} = ?")
        values.append(value)
    
    if not fields:
        conn.close()
        return False
    
    values.append(project_id)
    query = f"UPDATE projects SET {', '.join(fields)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
    
    cursor.execute(query, values)
    conn.commit()
    
    success = cursor.rowcount > 0
    conn.close()
    
    return success


def add_test_result(project_id, test_command, output, success):
    """
    Adds a test result record to the database.
    
    Args:
        project_id (int): The project ID.
        test_command (str): The test command executed.
        output (str): The test output.
        success (bool): Whether tests passed.
        
    Returns:
        int: The ID of the test result record.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO test_results (project_id, test_command, output, success)
        VALUES (?, ?, ?, ?)
    ''', (project_id, test_command, output, success))
    
    result_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return result_id


def get_test_results(project_id):
    """
    Retrieves all test results for a project.
    
    Args:
        project_id (int): The project ID.
        
    Returns:
        list: List of test result dictionaries.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM test_results 
        WHERE project_id = ? 
        ORDER BY executed_at DESC
    ''', (project_id,))
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def delete_project(project_id):
    """
    Deletes a project from the database.
    
    Args:
        project_id (int): The project ID.
        
    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
    success = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    
    return success
