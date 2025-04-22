# Keystroke Data Processing

This repository contains scripts and data for extracting and processing keystroke events from a structured database.

## Contents

- `action_log_clean.sql`: SQL script to populate the `keystrokes.db` database
- `load_action_log.py`: Loads the SQL data into SQLite
- `process_keystrokes_from_db.py`: Extracts and processes rows with `key_stroke` actions
- `keystroke_parser.py`: Parses raw keystroke JSON into a structured format
- `parsed_keystrokes_final.csv`: Cleaned keystroke output with columns: `user_id`, `task_id`, `timestamp`, `action`
