"""
Mock AI Planner module for AI Software Engineering Dashboard.
Generates realistic mock data for all 13 artifacts.
"""

import json


def generate_mock_blueprint(project_name, stack, idea):
    """
    Generates a complete mock blueprint with all 13 artifacts.
    
    Args:
        project_name (str): Name of the project.
        stack (str): Technology stack.
        idea (str): Project idea/description.
        
    Returns:
        dict: Complete blueprint JSON with all 13 artifacts.
    """
    
    # ARTIFACT 1: Variables (VAR-xxx)
    variables = [
        {"id": "VAR-001", "name": "MAX_UPLOAD_SIZE", "type": "number", "value": 10485760, "scope": "global"},
        {"id": "VAR-002", "name": "API_TIMEOUT", "type": "number", "value": 5000, "scope": "global"},
        {"id": "VAR-003", "name": "DATABASE_URL", "type": "string", "value": "postgresql://localhost:5432/db", "scope": "global"},
        {"id": "VAR-004", "name": "JWT_SECRET", "type": "string", "value": "your-secret-key-here", "scope": "auth"},
        {"id": "VAR-005", "name": "JWT_EXPIRY", "type": "string", "value": "24h", "scope": "auth"},
        {"id": "VAR-006", "name": "PAGE_SIZE", "type": "number", "value": 20, "scope": "pagination"},
        {"id": "VAR-007", "name": "MAX_RETRY_ATTEMPTS", "type": "number", "value": 3, "scope": "global"},
        {"id": "VAR-008", "name": "CACHE_TTL", "type": "number", "value": 3600, "scope": "cache"},
    ]
    
    # ARTIFACT 2: Functions (FN-xxx)
    functions = [
        {"id": "FN-001", "name": "authenticateUser", "module": "auth", "file": "auth.service.ts", "inputs": ["email", "password"], "outputs": ["AuthToken"], "description": "Authenticates user with email and password"},
        {"id": "FN-002", "name": "hashPassword", "module": "auth", "file": "auth.service.ts", "inputs": ["password"], "outputs": ["hashedPassword"], "description": "Hashes password using bcrypt"},
        {"id": "FN-003", "name": "verifyToken", "module": "auth", "file": "auth.service.ts", "inputs": ["token"], "outputs": ["UserPayload"], "description": "Verifies JWT token and returns payload"},
        {"id": "FN-004", "name": "getUserById", "module": "user", "file": "user.service.ts", "inputs": ["userId"], "outputs": ["User"], "description": "Retrieves user by ID"},
        {"id": "FN-005", "name": "createUser", "module": "user", "file": "user.service.ts", "inputs": ["email", "password", "name"], "outputs": ["User"], "description": "Creates a new user account"},
        {"id": "FN-006", "name": "updateUserProfile", "module": "user", "file": "user.service.ts", "inputs": ["userId", "profileData"], "outputs": ["User"], "description": "Updates user profile information"},
        {"id": "FN-007", "name": "createOrder", "module": "order", "file": "order.service.ts", "inputs": ["userId", "items"], "outputs": ["Order"], "description": "Creates a new order"},
        {"id": "FN-008", "name": "getOrderById", "module": "order", "file": "order.service.ts", "inputs": ["orderId"], "outputs": ["Order"], "description": "Retrieves order by ID"},
        {"id": "FN-009", "name": "updateOrderStatus", "module": "order", "file": "order.service.ts", "inputs": ["orderId", "status"], "outputs": ["Order"], "description": "Updates order status"},
        {"id": "FN-010", "name": "calculateTotal", "module": "order", "file": "order.service.ts", "inputs": ["items", "discountCode"], "outputs": ["number"], "description": "Calculates order total with discounts"},
        {"id": "FN-011", "name": "validateInput", "module": "validation", "file": "validation.service.ts", "inputs": ["data", "schema"], "outputs": ["ValidationResult"], "description": "Validates input data against schema"},
        {"id": "FN-012", "name": "sanitizeInput", "module": "validation", "file": "validation.service.ts", "inputs": ["data"], "outputs": ["SanitizedData"], "description": "Sanitizes input data to prevent XSS"},
    ]
    
    # ARTIFACT 3: Pipeline (STAGE-xxx)
    pipeline = [
        {"id": "STAGE-001", "name": "Input Validation", "order": 1, "functions": ["FN-011", "FN-012"], "on_error": "STOP_BUILD"},
        {"id": "STAGE-002", "name": "Authentication", "order": 2, "functions": ["FN-001", "FN-003"], "on_error": "STOP_BUILD"},
        {"id": "STAGE-003", "name": "Business Logic", "order": 3, "functions": ["FN-004", "FN-005", "FN-006", "FN-007", "FN-008", "FN-009", "FN-010"], "on_error": "STOP_BUILD"},
        {"id": "STAGE-004", "name": "Persistence", "order": 4, "functions": [], "on_error": "ROLLBACK"},
        {"id": "STAGE-005", "name": "Response Formatting", "order": 5, "functions": [], "on_error": "LOG_ERROR"},
    ]
    
    # ARTIFACT 4: Build Checklist (CHK-xxx)
    build_checklist = [
        {"id": "CHK-001", "description": "Setup database schema", "linked_req": "REQ-001", "linked_files": ["schema.sql"], "status": "PENDING", "priority": "HIGH"},
        {"id": "CHK-002", "description": "Implement authentication service", "linked_req": "REQ-002", "linked_files": ["auth.service.ts"], "status": "PENDING", "priority": "HIGH"},
        {"id": "CHK-003", "description": "Create user management endpoints", "linked_req": "REQ-003", "linked_files": ["user.controller.ts"], "status": "PENDING", "priority": "MEDIUM"},
        {"id": "CHK-004", "description": "Implement order processing logic", "linked_req": "REQ-004", "linked_files": ["order.service.ts"], "status": "PENDING", "priority": "HIGH"},
        {"id": "CHK-005", "description": "Add input validation middleware", "linked_req": "REQ-005", "linked_files": ["validation.middleware.ts"], "status": "PENDING", "priority": "HIGH"},
        {"id": "CHK-006", "description": "Setup error handling", "linked_req": "REQ-006", "linked_files": ["error.handler.ts"], "status": "PENDING", "priority": "MEDIUM"},
        {"id": "CHK-007", "description": "Write unit tests", "linked_req": "REQ-007", "linked_files": ["*.spec.ts"], "status": "PENDING", "priority": "HIGH"},
        {"id": "CHK-008", "description": "Configure CI/CD pipeline", "linked_req": "REQ-008", "linked_files": [".github/workflows/ci.yml"], "status": "PENDING", "priority": "LOW"},
    ]
    
    # ARTIFACT 5: Project Blueprint (DIR-xxx)
    project_blueprint = {
        "directories": [
            {"id": "DIR-001", "type": "directory", "path": "src/", "allowed_files": [], "children": ["DIR-002", "DIR-003", "DIR-004"]},
            {"id": "DIR-002", "type": "directory", "path": "src/modules/", "allowed_files": [], "children": ["DIR-005", "DIR-006", "DIR-007", "DIR-008"]},
            {"id": "DIR-003", "type": "directory", "path": "src/shared/", "allowed_files": ["index.ts", "types.ts", "utils.ts"], "children": []},
            {"id": "DIR-004", "type": "directory", "path": "src/config/", "allowed_files": ["database.ts", "app.ts", "env.ts"], "children": []},
            {"id": "DIR-005", "type": "directory", "path": "src/modules/auth/", "allowed_files": ["auth.controller.ts", "auth.service.ts", "auth.types.ts"], "children": []},
            {"id": "DIR-006", "type": "directory", "path": "src/modules/user/", "allowed_files": ["user.controller.ts", "user.service.ts", "user.types.ts"], "children": []},
            {"id": "DIR-007", "type": "directory", "path": "src/modules/order/", "allowed_files": ["order.controller.ts", "order.service.ts", "order.types.ts"], "children": []},
            {"id": "DIR-008", "type": "directory", "path": "src/modules/validation/", "allowed_files": ["validation.service.ts", "validation.rules.ts"], "children": []},
        ],
        "root_files": ["package.json", "tsconfig.json", ".env.example", "README.md"]
    }
    
    # ARTIFACT 6: Data Contracts (DC-xxx)
    data_contracts = [
        {
            "id": "DC-001", 
            "name": "UserEntity", 
            "type": "table", 
            "table": "users", 
            "fields": [
                {"name": "id", "type": "uuid", "constraints": ["PRIMARY KEY", "NOT NULL"]},
                {"name": "email", "type": "varchar(255)", "constraints": ["UNIQUE", "NOT NULL"]},
                {"name": "password_hash", "type": "varchar(255)", "constraints": ["NOT NULL"]},
                {"name": "name", "type": "varchar(100)", "constraints": ["NOT NULL"]},
                {"name": "created_at", "type": "timestamp", "constraints": ["DEFAULT CURRENT_TIMESTAMP"]},
                {"name": "updated_at", "type": "timestamp", "constraints": ["DEFAULT CURRENT_TIMESTAMP"]}
            ]
        },
        {
            "id": "DC-002", 
            "name": "OrderEntity", 
            "type": "table", 
            "table": "orders", 
            "fields": [
                {"name": "id", "type": "uuid", "constraints": ["PRIMARY KEY", "NOT NULL"]},
                {"name": "user_id", "type": "uuid", "constraints": ["FOREIGN KEY REFERENCES users(id)", "NOT NULL"]},
                {"name": "status", "type": "varchar(50)", "constraints": ["NOT NULL", "DEFAULT 'DRAFT'"]},
                {"name": "total_amount", "type": "decimal(10,2)", "constraints": ["NOT NULL"]},
                {"name": "created_at", "type": "timestamp", "constraints": ["DEFAULT CURRENT_TIMESTAMP"]},
                {"name": "updated_at", "type": "timestamp", "constraints": ["DEFAULT CURRENT_TIMESTAMP"]}
            ]
        },
        {
            "id": "DC-003", 
            "name": "OrderItemEntity", 
            "type": "table", 
            "table": "order_items", 
            "fields": [
                {"name": "id", "type": "uuid", "constraints": ["PRIMARY KEY", "NOT NULL"]},
                {"name": "order_id", "type": "uuid", "constraints": ["FOREIGN KEY REFERENCES orders(id)", "NOT NULL"]},
                {"name": "product_name", "type": "varchar(255)", "constraints": ["NOT NULL"]},
                {"name": "quantity", "type": "integer", "constraints": ["NOT NULL"]},
                {"name": "unit_price", "type": "decimal(10,2)", "constraints": ["NOT NULL"]}
            ]
        },
        {
            "id": "DC-004", 
            "name": "AuthToken", 
            "type": "interface", 
            "table": None, 
            "fields": [
                {"name": "token", "type": "string", "constraints": []},
                {"name": "expiresAt", "type": "Date", "constraints": []},
                {"name": "userId", "type": "string", "constraints": []}
            ]
        }
    ]
    
    # ARTIFACT 7: State Machines (SM-xxx)
    state_machines = [
        {
            "id": "SM-001",
            "module": "order",
            "entity": "Order",
            "states": ["DRAFT", "CONFIRMED", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"],
            "transitions": [
                {"from": "DRAFT", "to": "CONFIRMED", "trigger": "FN-007", "condition": "stock > 0"},
                {"from": "DRAFT", "to": "CANCELLED", "trigger": "user_request", "condition": "None"},
                {"from": "CONFIRMED", "to": "PROCESSING", "trigger": "payment_confirmed", "condition": "payment_status == 'PAID'"},
                {"from": "PROCESSING", "to": "SHIPPED", "trigger": "FN-009", "condition": "tracking_number != null"},
                {"from": "SHIPPED", "to": "DELIVERED", "trigger": "delivery_confirmed", "condition": "None"},
                {"from": "CONFIRMED", "to": "CANCELLED", "trigger": "refund_processed", "condition": "refund_status == 'APPROVED'"},
            ]
        },
        {
            "id": "SM-002",
            "module": "user",
            "entity": "UserAccount",
            "states": ["PENDING", "ACTIVE", "SUSPENDED", "DELETED"],
            "transitions": [
                {"from": "PENDING", "to": "ACTIVE", "trigger": "email_verified", "condition": "verification_token_valid"},
                {"from": "ACTIVE", "to": "SUSPENDED", "trigger": "admin_action", "condition": "violation_detected"},
                {"from": "SUSPENDED", "to": "ACTIVE", "trigger": "appeal_approved", "condition": "admin_approval"},
                {"from": "ACTIVE", "to": "DELETED", "trigger": "user_request", "condition": "data_retention_period_expired"},
            ]
        }
    ]
    
    # ARTIFACT 8: Dependency Matrix (DEP-xxx)
    dependency_matrix = [
        {"id": "DEP-001", "caller_module": "auth", "target_module": "user", "allowed_functions": ["FN-004"], "forbidden_functions": ["FN-005", "FN-006"]},
        {"id": "DEP-002", "caller_module": "auth", "target_module": "order", "allowed_functions": [], "forbidden_functions": ["FN-007", "FN-008", "FN-009", "FN-010"]},
        {"id": "DEP-003", "caller_module": "order", "target_module": "user", "allowed_functions": ["FN-004"], "forbidden_functions": ["FN-005", "FN-006"]},
        {"id": "DEP-004", "caller_module": "order", "target_module": "auth", "allowed_functions": ["FN-003"], "forbidden_functions": ["FN-001", "FN-002"]},
        {"id": "DEP-005", "caller_module": "user", "target_module": "validation", "allowed_functions": ["FN-011", "FN-012"], "forbidden_functions": []},
        {"id": "DEP-006", "caller_module": "order", "target_module": "validation", "allowed_functions": ["FN-011", "FN-012"], "forbidden_functions": []},
    ]
    
    # ARTIFACT 9: Business Rules (BR-xxx)
    business_rules = [
        {
            "id": "BR-001",
            "name": "Discount Calculation",
            "formula": "final_price = base_price - (base_price * discount_percentage / 100)",
            "constraints": ["discount_percentage <= 50", "final_price >= 0"],
            "linked_fn": "FN-010"
        },
        {
            "id": "BR-002",
            "name": "Minimum Order Value",
            "formula": "order_total >= minimum_order_value",
            "constraints": ["minimum_order_value = 10.00"],
            "linked_fn": "FN-007"
        },
        {
            "id": "BR-003",
            "name": "Stock Availability Check",
            "formula": "requested_quantity <= available_stock",
            "constraints": ["available_stock >= 0"],
            "linked_fn": "FN-007"
        },
        {
            "id": "BR-004",
            "name": "Email Uniqueness",
            "formula": "COUNT(users WHERE email = new_email) == 0",
            "constraints": ["case_insensitive_comparison"],
            "linked_fn": "FN-005"
        },
        {
            "id": "BR-005",
            "name": "Password Strength",
            "formula": "password_length >= 8 AND has_uppercase AND has_lowercase AND has_digit AND has_special",
            "constraints": ["special_chars: !@#$%^&*()_+-=[]{}|;:,.<>?"],
            "linked_fn": "FN-005"
        }
    ]
    
    # ARTIFACT 10: Test Cases (TC-xxx)
    test_cases = [
        {
            "id": "TC-001",
            "title": "Login with valid credentials",
            "linked_fn": "FN-001",
            "linked_req": "REQ-002",
            "steps": ["POST /auth/login with valid email/password"],
            "expected_result": "Return 200 with JWT token",
            "type": "integration"
        },
        {
            "id": "TC-002",
            "title": "Login with invalid credentials",
            "linked_fn": "FN-001",
            "linked_req": "REQ-002",
            "steps": ["POST /auth/login with invalid email/password"],
            "expected_result": "Return 401 with error message",
            "type": "integration"
        },
        {
            "id": "TC-003",
            "title": "Create user with valid data",
            "linked_fn": "FN-005",
            "linked_req": "REQ-003",
            "steps": ["POST /users with valid email, password, name"],
            "expected_result": "Return 201 with user object",
            "type": "integration"
        },
        {
            "id": "TC-004",
            "title": "Create user with duplicate email",
            "linked_fn": "FN-005",
            "linked_req": "REQ-003",
            "steps": ["POST /users with existing email"],
            "expected_result": "Return 409 with conflict error",
            "type": "integration"
        },
        {
            "id": "TC-005",
            "title": "Create order with valid items",
            "linked_fn": "FN-007",
            "linked_req": "REQ-004",
            "steps": ["POST /orders with userId and items array"],
            "expected_result": "Return 201 with order object in DRAFT status",
            "type": "integration"
        },
        {
            "id": "TC-006",
            "title": "Calculate total with discount",
            "linked_fn": "FN-010",
            "linked_req": "REQ-004",
            "steps": ["Call calculateTotal with items and valid discount code"],
            "expected_result": "Return correct discounted total",
            "type": "unit"
        },
        {
            "id": "TC-007",
            "title": "Validate input with missing required field",
            "linked_fn": "FN-011",
            "linked_req": "REQ-005",
            "steps": ["Call validateInput with missing required field"],
            "expected_result": "Return validation error with field details",
            "type": "unit"
        },
        {
            "id": "TC-008",
            "title": "Verify valid JWT token",
            "linked_fn": "FN-003",
            "linked_req": "REQ-002",
            "steps": ["Call verifyToken with valid JWT"],
            "expected_result": "Return decoded user payload",
            "type": "unit"
        }
    ]
    
    # ARTIFACT 11: Forbidden Rules (FR-xxx)
    forbidden_rules = [
        {"id": "FR-001", "rule": "DILARANG menggunakan ORM selain Prisma", "scope": "global", "severity": "CRITICAL"},
        {"id": "FR-002", "rule": "DILARANG mengubah field 'id' pada semua entitas", "scope": "database", "severity": "CRITICAL"},
        {"id": "FR-003", "rule": "DILARANG buat folder di luar src/modules/", "scope": "structure", "severity": "HIGH"},
        {"id": "FR-004", "rule": "DILARANG menyimpan password plain text", "scope": "security", "severity": "CRITICAL"},
        {"id": "FR-005", "rule": "DILARANG melakukan query SQL langsung tanpa parameterized queries", "scope": "security", "severity": "CRITICAL"},
        {"id": "FR-006", "rule": "DILARANG mengembalikan error stack trace ke client", "scope": "api", "severity": "HIGH"},
        {"id": "FR-007", "rule": "DILARANG hardcode secrets atau API keys dalam kode", "scope": "security", "severity": "CRITICAL"},
        {"id": "FR-008", "rule": "DILARANG skip input validation pada public endpoints", "scope": "security", "severity": "HIGH"},
    ]
    
    # ARTIFACT 12: Requirements (REQ-xxx)
    requirements = [
        {
            "id": "REQ-001",
            "title": "Database Schema Setup",
            "description": "Sistem harus memiliki schema database untuk users, orders, dan order_items",
            "sprint": "SPRINT-01",
            "status": "APPROVED",
            "trace": {"modules": ["database"], "files": ["schema.sql"], "functions": [], "tests": []}
        },
        {
            "id": "REQ-002",
            "title": "User Authentication",
            "description": "Sistem harus mampu autentikasi user via email/password dan menghasilkan JWT token",
            "sprint": "SPRINT-01",
            "status": "APPROVED",
            "trace": {"modules": ["auth"], "files": ["auth.service.ts", "auth.controller.ts"], "functions": ["FN-001", "FN-002", "FN-003"], "tests": ["TC-001", "TC-002", "TC-008"]}
        },
        {
            "id": "REQ-003",
            "title": "User Management",
            "description": "Sistem harus mampu membuat, membaca, dan memperbarui profil user",
            "sprint": "SPRINT-01",
            "status": "APPROVED",
            "trace": {"modules": ["user"], "files": ["user.service.ts", "user.controller.ts"], "functions": ["FN-004", "FN-005", "FN-006"], "tests": ["TC-003", "TC-004"]}
        },
        {
            "id": "REQ-004",
            "title": "Order Processing",
            "description": "Sistem harus mampu membuat order, menghitung total, dan mengelola status order",
            "sprint": "SPRINT-02",
            "status": "APPROVED",
            "trace": {"modules": ["order"], "files": ["order.service.ts", "order.controller.ts"], "functions": ["FN-007", "FN-008", "FN-009", "FN-010"], "tests": ["TC-005", "TC-006"]}
        },
        {
            "id": "REQ-005",
            "title": "Input Validation",
            "description": "Sistem harus memvalidasi semua input dari client sebelum diproses",
            "sprint": "SPRINT-01",
            "status": "APPROVED",
            "trace": {"modules": ["validation"], "files": ["validation.service.ts"], "functions": ["FN-011", "FN-012"], "tests": ["TC-007"]}
        },
        {
            "id": "REQ-006",
            "title": "Error Handling",
            "description": "Sistem harus menangani error dengan baik dan mengembalikan response yang sesuai",
            "sprint": "SPRINT-01",
            "status": "APPROVED",
            "trace": {"modules": ["shared"], "files": ["error.handler.ts"], "functions": [], "tests": []}
        },
        {
            "id": "REQ-007",
            "title": "Unit Testing",
            "description": "Semua fungsi bisnis harus memiliki unit test dengan coverage minimal 80%",
            "sprint": "SPRINT-02",
            "status": "APPROVED",
            "trace": {"modules": ["all"], "files": ["*.spec.ts"], "functions": [], "tests": []}
        },
        {
            "id": "REQ-008",
            "title": "CI/CD Pipeline",
            "description": "Sistem harus memiliki pipeline CI/CD untuk automated testing dan deployment",
            "sprint": "SPRINT-03",
            "status": "PLANNED",
            "trace": {"modules": ["infrastructure"], "files": [".github/workflows/ci.yml"], "functions": [], "tests": []}
        }
    ]
    
    # ARTIFACT 13: ID Tracking Rule
    id_tracking = {
        "rule": "Every artifact MUST have unique ID following the pattern XXX-NNN",
        "enforcement": "Builder must include ID in code comments: // REQ-ID: REQ-001",
        "action_on_violation": "STOP_BUILD if code has no matching ID",
        "id_patterns": {
            "variables": "VAR-xxx",
            "functions": "FN-xxx",
            "pipeline": "STAGE-xxx",
            "checklist": "CHK-xxx",
            "blueprint": "DIR-xxx",
            "data_contracts": "DC-xxx",
            "state_machines": "SM-xxx",
            "dependency_matrix": "DEP-xxx",
            "business_rules": "BR-xxx",
            "test_cases": "TC-xxx",
            "forbidden_rules": "FR-xxx",
            "requirements": "REQ-xxx"
        },
        "validation": "All IDs must be unique within their artifact type"
    }
    
    return {
        "project_name": project_name,
        "stack": stack,
        "idea": idea,
        "variables": variables,
        "functions": functions,
        "pipeline": pipeline,
        "build_checklist": build_checklist,
        "project_blueprint": project_blueprint,
        "data_contracts": data_contracts,
        "state_machines": state_machines,
        "dependency_matrix": dependency_matrix,
        "business_rules": business_rules,
        "test_cases": test_cases,
        "forbidden_rules": forbidden_rules,
        "requirements": requirements,
        "id_tracking": id_tracking
    }
