# Repository & GitHub Username anpassen
$User = "lukas69571"
$Repo = "website"

# GitHub API URL für Pages
$ApiUrl = "https://api.github.com/repos/$User/$Repo/pages"

try {
    $response = Invoke-RestMethod -Uri $ApiUrl -Method Get -UseBasicParsing
    if ($response.status -eq "built") {
        Write-Host "✅ GitHub Pages ist aktiviert!"
        Write-Host "🌐 Live-URL: $($response.html_url)"
        Write-Host "Branch: $($response.source.branch), Ordner: $($response.source.path)"
    } else {
        Write-Host "⚠️ GitHub Pages ist aktiviert, wird aber noch gebaut..."
    }
} catch {
    Write-Host "❌ GitHub Pages ist wahrscheinlich nicht aktiviert oder Repository nicht gefunden."
}
