import sqlite3

def load_sql_file(db_path, sql_file_path):
    conn = sqlite3.connect(db_path)
    with open(sql_file_path, 'r') as f:
        sql_script = f.read()
    conn.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database loaded successfully.")

if __name__ == "__main__":
    load_sql_file("keystrokes.db", "action_log_clean.sql")
