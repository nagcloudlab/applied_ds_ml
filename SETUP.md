This project is tested with Python 3.11. Python 3.10 also works. Python 3.12+ may work but is not tested. Python 3.9 or older is not supported.

# Student Environment Setup Guide

Use this guide before running the notebooks.

## Recommended Setup

- Use Python 3.11.
- Create one virtual environment inside the project folder.
- Install libraries from `requirements.txt`.
- Use the same environment as the Jupyter notebook kernel.

## Why Use a Virtual Environment?

- It keeps this training separate from other Python projects.
- All students use the same library versions.
- It reduces "works on my system" problems.
- It is easier to delete and recreate if something breaks.

## Windows PowerShell Setup

Open PowerShell inside the `applied_ds_ml` project folder.

If the project is in your Downloads folder, Desktop, or any other location, first move into that folder. Example:

```powershell
cd path\to\applied_ds_ml
```

Check whether Python 3.11 is installed:

```powershell
py -3.11 --version
```

If Python 3.11 is available, create a virtual environment:

```powershell
py -3.11 -m venv .venv
```

## macOS and Linux Setup

Open a terminal inside the `applied_ds_ml` project folder.

Check whether Python 3.11 is installed:

```bash
python3.11 --version
```

If Python 3.11 is available, create a virtual environment:

```bash
python3.11 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Upgrade packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name applied_ds_ml --display-name "Python (applied_ds_ml)"
```

Start Jupyter:

```bash
jupyter notebook
```

Note: on macOS, use `python3` instead of `py` if `python3.11` is not available on your PATH.

## If Python 3.11 Is Not Found

If you see this error:

```text
No suitable Python runtime found
Pass --list (-0) to see all detected environments on your machine
```

First check detected Python versions:


```powershell
py -0p
```

Then install Python 3.11 using Windows Package Manager:

```powershell
winget install Python.Python.3.11
```

After installation:

- Close PowerShell.
- Open PowerShell again inside the `applied_ds_ml` project folder.
- Run these commands:

```powershell
py -3.11 --version
py -3.11 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade packaging tools:

```powershell
python -m pip install --upgrade pip setuptools wheel
```

Install required libraries:

```powershell
pip install -r requirements.txt
```

Register the environment as a Jupyter kernel:

```powershell
python -m ipykernel install --user --name applied_ds_ml --display-name "Python (applied_ds_ml)"
```

Start Jupyter:

```powershell
jupyter notebook
```

Open the first Day 1 notebook:

```text
days/day_01_eda_preprocessing/notebooks/01_data_science_ecosystem_and_setup.ipynb
```

In Jupyter, select this kernel:

```text
Python (applied_ds_ml)
```

## If Activation Is Blocked

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Quick Verification

After activating the environment, run:

```powershell
python --version
pip list
```

Inside the notebook, the environment check cell should show the virtual environment Python path.

## Optional PyCaret Setup

Do not install PyCaret at the beginning of the course.

Install it only when reaching the optional PyCaret lab:

```powershell
pip install -r requirements-optional-pycaret.txt
```

If PyCaret installation fails in a classroom, skip the PyCaret lab and continue with Scikit-learn.

## Before Class

Complete these checks before starting the first notebook:

- The virtual environment is activated.
- Jupyter opens successfully.
- The kernel `Python (applied_ds_ml)` is available.
- The first Day 1 notebook opens without errors.

## Troubleshooting

### Proxy or SSL errors

If `pip install` fails with SSL or certificate errors behind a corporate proxy:

```bash
pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

### Wrong kernel in notebook

If imports fail inside a notebook but work in the terminal, the notebook may be using the wrong kernel. In Jupyter, click Kernel > Change Kernel and select `Python (applied_ds_ml)`.

### Import errors after install

Make sure the virtual environment is activated before starting Jupyter. The terminal prompt should show `(.venv)`. If it does not, activate the environment first.

### pip install hangs

Check your network connection and proxy settings. Try running `pip install numpy` alone first to confirm connectivity.
