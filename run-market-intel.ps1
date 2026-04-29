# Market Intel Agent — always runs THIS repo's app (4 tabs: Memo, Follow-ups, Social & Reviews, Sources).
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$launcher = Join-Path $root "app.py"
if (-not (Test-Path $launcher)) {
    Write-Error "Missing repo-root launcher: $launcher"
}
Set-Location $root
Write-Host "Running (repo root -> market-intel-agent): $launcher" -ForegroundColor Cyan
& streamlit run app.py
