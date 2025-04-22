import sqlite3
import json
import csv
from keystroke_parser import parse_keystrokes

def clean_and_parse_keystrokes(raw_string):
    try:
        main_part = raw_string.split('|')[0]
        if main_part.startswith("key_stroke;"):
            main_part = main_part[len("key_stroke;"):]
        unescaped = main_part.encode().decode('unicode_escape')
        parsed = json.loads(unescaped)
        return parsed
    except Exception as e:
        print(f"Error parsing: {e} | Raw: {raw_string[:200]}")
        return None

def process_keystrokes_from_db(db_path, output_csv="parsed_keystrokes_final.csv"):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT user, task, action_type
        FROM action_log
        WHERE action_type LIKE 'key_stroke;%'
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        parsed_rows = []
        for user, task, action_type in rows:
            raw_keystrokes = clean_and_parse_keystrokes(action_type)
            if raw_keystrokes:
                parsed = parse_keystrokes(user, task, raw_keystrokes)
                parsed_rows.extend(parsed)

        if parsed_rows:
            with open(output_csv, "w", newline="") as csvfile:
                fieldnames = ["user_id", "task_id", "timestamp", "action"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(parsed_rows)
            print(f"Wrote {len(parsed_rows)} entries to {output_csv}")
        else:
            print("No keystrokes parsed.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    process_keystrokes_from_db("keystrokes.db")
