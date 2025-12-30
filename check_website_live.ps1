$Url = "https://lukas69571.github.io/website/"

try {
    $resp = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 10
    if ($resp.StatusCode -eq 200) {
        Write-Host "✅ Website ist live: $Url"
    } else {
        Write-Host "⚠️ Website erreichbar, StatusCode: $($resp.StatusCode)"
    }
} catch {
    Write-Host "❌ Website ist noch nicht live oder URL falsch."
}
