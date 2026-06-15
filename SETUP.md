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
