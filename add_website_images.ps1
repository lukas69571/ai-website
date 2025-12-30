# ----------------- Ordner für Bilder öffnen -----------------
$ImageFolder = "C:\Users\lukas\website\assets\images"

# Ordner erstellen, falls er nicht existiert
if (-not (Test-Path $ImageFolder)) {
    New-Item -ItemType Directory -Path $ImageFolder -Force
    Write-Host "📁 Ordner erstellt: $ImageFolder"
} else {
    Write-Host "📁 Ordner existiert bereits: $ImageFolder"
}

# Öffnet den Ordner im Windows Explorer, damit du die Bilder hineinziehen kannst
Start-Process $ImageFolder
Write-Host "➡️ Ziehe jetzt deine Bilder in den geöffneten Ordner."
