# File Organizer

This Python script helps you automatically organize files in any folder by type, date, or custom rules.

## Installation

Make sure you have Python installed. Clone the repository and run:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script with the following command:

```bash
python organizer.py <directory> [options]
```

### Options:
- `--by-date`: Organizes files by their last modified date.
- `--dry-run`: Shows what would happen without making any changes.
- `--undo`: Reverts the last organization.
- `--recursive`: Organizes files in subdirectories as well.

### Examples:

1. **Organize Downloads Folder by Type**:
   ```bash
   python organizer.py ~/Downloads
   ```

2. **Organize Documents by Date**:
   ```bash
   python organizer.py ~/Documents --by-date
   ```

3. **Dry Run on Desktop**:
   ```bash
   python organizer.py ~/Desktop --dry-run
   ```

4. **Undo Last Organization**:
   ```bash
   python organizer.py ~/Downloads --undo
   ```

5. **Custom Rules**: You can define custom rules in `rules.json`. For example, to categorize spreadsheets:
   ```json
   {"custom_rules": {"spreadsheets": [".xls", ".xlsx", ".csv"], "presentations": [".ppt", ".pptx"], "scripts": [".py", ".js"]}}
   ```

## License
This project is licensed under the MIT License.