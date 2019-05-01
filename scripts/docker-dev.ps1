Push-Location $PSScriptRoot
$depsFile = Resolve-Path -Path ../Pipfile
$hashFile = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath("../Pipfile.hash")
Pop-Location

function WriteHash($hash) {
    Write-Host -fore yellow "Writing hash..."
    Out-File -FilePath $hashFile -InputObject $hash
}

function UpdateDeps {
    Write-Host -fore yellow "Updating dependencies..."
    Push-Location ($PSScriptRoot + "\..")
    docker build -f Dockerfile.dev -t lensor .
    Pop-Location
}

function RunApp {
    Write-Host -fore yellow "Running app..."
    Push-Location ($PSScriptRoot + "\..")
    docker run --rm -w "/app" -v ${PWD}:/app lensor python init.py
    Pop-Location
}

function CheckDepsAndRun {
    $depsHash = (Get-FileHash -Path $depsFile -Algorithm MD5).Hash
    
    if([System.IO.File]::Exists($hashFile)) {
        Write-Host -fore green "Hash exists, comparing hashes"
        $readHash = Get-Content -Path $hashFile
    
        if($readHash -eq $depsHash) {
            Write-Host -fore green "Hashes are equal"
            RunApp;
        } else {
            Write-Host -fore red "Hashes are NOT equal"
            UpdateDeps;
            WriteHash($depsHash);
            RunApp;
        }
    } else {
        Write-Host -fore red "Hash doesnt exist"
    
        UpdateDeps;
        WriteHash($depsHash);
        RunApp;
    }
}

CheckDepsAndRun;