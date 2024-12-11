param (
    [Parameter(Mandatory=$true, HelpMessage="Path to file to run")][string]$ScriptPath,
    [Parameter(Mandatory=$true, HelpMessage="Path to input data")][string]$InputData,
	[Parameter(Mandatory=$false, HelpMessage="Build the runner image")][switch]$BuildContainer = $false
)

Clear-Host

If ($BuildContainer) {
	docker build -t python-script-runner .
	Write-Host "Image built"
	PAUSE
}

docker run --rm -v "$($ScriptPath):/app/script.py" -v "$($InputData):/app/input.txt" python-script-runner
