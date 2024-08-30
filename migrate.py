from flask_migrate import upgrade, migrate, init
from main import app
from website import db

with app.app_context():
    # Initialize the migration repository if not already initialized
    try:
        init()
    except Exception as e:
        print(f"Migration repository initialization failed: {e}")
    
    # Generate a new migration script
    try:
        migrate(message="Initial migration.")
    except Exception as e:
        print(f"Migration script generation failed: {e}")
    
    # Apply migrations to the database
    try:
        upgrade()
    except Exception as e:
        print(f"Database upgrade failed: {e}")