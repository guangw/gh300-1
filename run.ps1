# run.ps1 - activate venv (if present) and run the FastAPI app via uvicorn
# Usage: Open PowerShell in the repo root and run: .\run.ps1

$venvPath = Join-Path -Path $PSScriptRoot -ChildPath '.venv\Scripts\Activate.ps1'
if (Test-Path $venvPath) {
    Write-Host "Activating virtual environment..."
    & $venvPath
} else {
    Write-Host "No .venv found. Continuing without activating a venv."
}

# Run the server
Write-Host "Starting uvicorn server on http://127.0.0.1:8000 ..."
# Use python -m uvicorn to ensure the venv python is used if activated
python -m uvicorn src.app:app --reload --host 127.0.0.1 --port 8000
