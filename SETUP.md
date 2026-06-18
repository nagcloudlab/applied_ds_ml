# Setup Guide (Windows)

## Prerequisites

- Windows 10 or 11
- Internet connection
- Admin access (for first-time Python install)

## Step 1: Install Python 3.11

Open **PowerShell** and run:

```powershell
winget install Python.Python.3.11
```

Close and reopen PowerShell, then verify:

```powershell
python --version
```

Expected output: `Python 3.11.x`

If `python` is not recognized, check that Python is added to your system PATH. You can reinstall Python from https://www.python.org/downloads/ and check "Add Python to PATH" during installation.

## Step 2: Clone or Download the Repo

If using git:

```powershell
git clone <repo-url>
cd applied_ds_ml
```

Or download the ZIP and extract it. Open PowerShell inside the `applied_ds_ml` folder.

## Step 3: Create Virtual Environment

```powershell
python -m venv .venv
```

## Step 4: Activate Virtual Environment

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your prompt. This means the environment is active.

If you get a permission error, run PowerShell as Administrator for the `Set-ExecutionPolicy` command once, then switch back to normal PowerShell.

## Step 5: Install Packages

```powershell
pip install -r requirements.txt
```

This installs: numpy, pandas, matplotlib, seaborn, scikit-learn, jupyterlab, and notebook.

## Step 6: Launch Jupyter

```powershell
jupyter notebook
```

Or if you prefer JupyterLab:

```powershell
jupyter lab
```

A browser tab will open. Navigate to `notebooks/` and open `day_01_data_science_lifecycle_demo.ipynb`.

## Step 7: Verify Everything Works

In the notebook, run the first code cell (Step 0: Setup). If all imports succeed and you see "Libraries ready.", your setup is complete.

## Troubleshooting

| Problem | Fix |
|---|---|
| `python` not recognized | Reinstall Python with "Add to PATH" checked |
| `pip` not recognized | Use `python -m pip install -r requirements.txt` |
| Activation fails | Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first |
| Jupyter opens wrong Python | Run `python -m jupyter notebook` instead |
| Import error in notebook | Make sure you activated `.venv` before launching Jupyter |
| `(.venv)` not showing | You forgot to activate. Run `.\.venv\Scripts\Activate.ps1` again |

## Daily Workflow

Every time you open a new PowerShell window:

```powershell
cd applied_ds_ml
.\.venv\Scripts\Activate.ps1
jupyter notebook
```
