# GitHub Actions Workflow - Daily Folder Creator

This directory contains the GitHub Actions workflow for automatically creating daily coding practice folders.

## Workflow: `create-daily-folder.yml`

### Purpose
Automatically creates a new `dayXXX` folder with auto-incrementing day numbers for daily coding practice.

### Features
- ✅ **Auto-incrementing folder numbers**: Detects existing folders (day001, day002, etc.) and creates the next one
- ✅ **Linear numbering**: Ensures sequential folder creation (001 → 002 → 003)
- ✅ **Template support**: Copies template files from `.github/templates/day-template/`
- ✅ **Automatic README**: Creates a README.md in each new folder
- ✅ **Verification**: Runs pre-commit checks to verify folder creation
- ✅ **Auto-commit**: Automatically commits and pushes the new folder to the repository

### How to Use

#### Method 1: From GitHub Web Interface
1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. Select **"Create Daily Folder"** workflow from the left sidebar
4. Click **"Run workflow"** button
5. (Optional) Uncheck "Copy template files" if you don't want template files
6. Click the green **"Run workflow"** button
7. Wait for the workflow to complete
8. Pull the changes: `git pull`

#### Method 2: Using GitHub CLI
```bash
# Trigger the workflow with default settings
gh workflow run "Create Daily Folder"

# Trigger without copying template files
gh workflow run "Create Daily Folder" -f copy_template=false
```

### What Gets Created

Each new day folder includes:
1. **Folder name**: `dayXXX` (e.g., day002, day003, day010)
2. **app.py**: Python file for your coding exercises (from template)
3. **README.md**: Pre-formatted README with sections for problems, notes, and solutions
4. **Template files**: Any additional files from `.github/templates/day-template/`

### Workflow Steps

1. **Checkout repository**: Fetches the latest code
2. **Configure Git**: Sets up Git credentials for the bot
3. **Create next day folder**: 
   - Scans for existing `dayXXX` folders
   - Finds the highest number
   - Creates the next folder with incremented number
4. **Copy template files**: Copies files from the template directory
5. **Create README**: Generates a README.md for the new day
6. **Verify folder creation**: Runs checks to ensure everything was created correctly
7. **Commit and push**: Commits the new folder and pushes to the repository
8. **Create summary**: Displays a summary of what was created

### Customization

#### Adding Custom Template Files
1. Navigate to `.github/templates/day-template/`
2. Add any files you want included in every new day folder
3. These files will be automatically copied when creating new folders

#### Modifying the Workflow
- Edit `.github/workflows/create-daily-folder.yml`
- Common modifications:
  - Change folder naming pattern (currently `dayXXX`)
  - Modify README template
  - Add additional automation steps
  - Change commit message format

### Troubleshooting

**Problem**: Workflow fails with permission error
- **Solution**: Ensure the workflow has `contents: write` permission (already configured)

**Problem**: Folder number doesn't increment correctly
- **Solution**: Check that existing folders follow the `dayXXX` format with 3 digits

**Problem**: Template files not copied
- **Solution**: Verify files exist in `.github/templates/day-template/`

### Requirements

- GitHub repository with Actions enabled
- Write permissions for GitHub Actions
- Existing day folders should follow `dayXXX` naming pattern

### Notes

- The workflow uses `workflow_dispatch` trigger, meaning it runs manually on demand
- Folder numbers are zero-padded to 3 digits (001, 002, ..., 999)
- If no existing folders are found, it starts with `day001`
- The workflow will fail if it tries to create a folder that already exists
