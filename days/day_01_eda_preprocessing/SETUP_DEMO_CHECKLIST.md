# Setup Demo Checklist

Use this as a trainer checklist before opening Notebook 01.

This is not a slide deck. It is a live demo flow.

**How this differs from SETUP.md:** SETUP.md is the full student setup reference (all platforms, troubleshooting). This checklist is a streamlined trainer script for the live classroom demo. For detailed troubleshooting, refer students to SETUP.md.

**Estimated demo time:** 20-40 minutes (depending on classroom network speed and student questions).

## Demo Goal

Help learners confirm that their environment is ready for hands-on notebooks.

By the end of the demo, learners should have:

- Python available
- A virtual environment created
- The environment activated
- Required libraries installed
- Jupyter Notebook running
- The correct notebook kernel selected
- Notebook 01 opened

## Live Demo Flow

### 1. Open Terminal

Open PowerShell inside the project folder.

Trainer line:

```text
All setup commands should run from the project folder.
```

### 2. Check Python 3.11

```powershell
py -3.11 --version
```

Expected result:

```text
Python 3.11.x
```

### 3. If Python 3.11 Is Not Found

Check detected Python versions:

```powershell
py -0p
```

Install Python 3.11 if needed:

```powershell
winget install Python.Python.3.11
```

After installation:

- Close PowerShell.
- Open PowerShell again.
- Return to the project folder.
- Run the version check again.

### 4. Create Virtual Environment

```powershell
py -3.11 -m venv .venv
```

Trainer line:

```text
This creates a separate Python workspace for this training.
```

### 5. Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

Expected sign:

```text
(.venv)
```

### 6. If Activation Is Blocked

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 7. Upgrade Packaging Tools

```powershell
python -m pip install --upgrade pip setuptools wheel
```

### 8. Install Required Libraries

```powershell
pip install -r requirements.txt
```

### 9. Register Jupyter Kernel

```powershell
python -m ipykernel install --user --name applied_ds_ml --display-name "Python (applied_ds_ml)"
```

Trainer line:

```text
The kernel connects Jupyter Notebook to this virtual environment.
```

### 10. Start Jupyter

```powershell
jupyter notebook
```

Open:

```text
days/day_01_eda_preprocessing/notebooks/01_data_science_ecosystem_and_setup.ipynb
```

Select kernel:

```text
Python (applied_ds_ml)
```

## Quick Notebook Check

Run the environment check cell in Notebook 01.

Learners should verify:

- Python version is visible.
- Python executable points to the project environment.
- Imports work without error.

## Teaching Rhythm

For each command:

1. Explain why the command is needed.
2. Run the command.
3. Read the output.
4. Ask learners what the output confirms.
5. Let learners repeat.

## Common Problems

| Problem | Likely Cause | Fix |
|---|---|---|
| `No suitable Python runtime found` | Python 3.11 missing | Install Python 3.11 |
| Activation blocked | PowerShell policy | Run execution policy command |
| Package missing in notebook | Wrong kernel | Select `Python (applied_ds_ml)` |
| `jupyter` not found | Requirements not installed | Run `pip install -r requirements.txt` |
| Import error | Package install failed | Re-run requirements install after activation |

## Trainer Reminder

Do not turn setup into a long lecture.

Use this pattern:

```text
Show command
    -> Explain purpose
    -> Run command
    -> Read output
    -> Learners repeat
```
