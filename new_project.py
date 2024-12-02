import streamlit as st
import mysql.connector
from datetime import datetime

# Database connection function (adjust it according to your database)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Update with your DB host if it's not local
        user="root",       # Replace with your DB username
        password="",       # Replace with your DB password
        database="parametres_du_projet"  # Replace with your database name
    )

# Function to insert project data into the database and return the project_id
def insert_project_data(project_title, scorecard_type, client_category, product_type, instructions, business_plan, project_plan):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insert project data into the table (ensure the table has appropriate columns)
    insert_query = """
    INSERT INTO projects (project_title, scorecard_type, client_category, product_type, instructions, business_plan, project_plan, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Execute the query
    cursor.execute(insert_query, (project_title, scorecard_type, client_category, product_type, instructions, business_plan, project_plan, datetime.now()))
    
    # Commit and close connection
    conn.commit()

    # Get the auto-generated project ID
    project_id = cursor.lastrowid  # This retrieves the last inserted ID
    cursor.close()
    conn.close()

    return project_id


