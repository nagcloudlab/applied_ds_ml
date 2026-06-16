

winget install Python.Python.3.11
python --version
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook