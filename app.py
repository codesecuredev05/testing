import os
import sqlite3
import subprocess
import hashlib
import yaml

# 1. Hardcoded Secret (CWE-798)
API_SECRET_KEY = "sk_live_51H9x82kL90pQwErTyUiOpAsDfGhJkLzXcVbNm"

def get_user_by_name(username: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 2. SQL Injection via string formatting (CWE-89)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def ping_host(host: str):
    # 3. OS Command Injection via shell=True (CWE-78)
    command = f"ping -c 1 {host}"
    subprocess.Popen(command, shell=True)

def hash_password(password: str) -> str:
    # 4. Weak Cryptographic Hash Function (CWE-328)
    return hashlib.md5(password.encode()).hexdigest()

def parse_config(raw_yaml: str):
    # 5. Unsafe YAML Deserialization (CWE-502)
    return yaml.load(raw_yaml)
