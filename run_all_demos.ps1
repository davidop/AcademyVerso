# run_all_demos.ps1
# Ejecuta todos los scripts de demo secuencialmente. Pausa entre cada demo para revisión.

Write-Host "Run all demos - inicio" -ForegroundColor Cyan

Write-Host "Asegúrate de haber configurado variables de entorno (API_KEY/API_URL) si las demos las requieren." -ForegroundColor Yellow

$scripts = @(
    ".\examples\premium_request_demo.py",
    ".\examples\choose_model_demo.py",
    ".\examples\chat_modes_demo.py",
    ".\examples\ask_demo.py",
    ".\examples\edits_demo.py",
    ".\examples\agent_demo.py",
    ".\examples\plan_demo.py",
    ".\examples\next_edit_suggestions_demo.py",
    ".\examples\code_review_demo.py",
    ".\examples\prompt_files_demo.py",
    ".\examples\custom_chat_modes_demo.py",
    ".\examples\copilot_demo.py",
    ".\examples\mcp_demo.py"
)

foreach ($s in $scripts) {
    Write-Host "`n=== Ejecutando: $s ===" -ForegroundColor Green
    try {
        py $s
    } catch {
        Write-Host ("Error ejecutando {0}: {1}" -f $s, $_) -ForegroundColor Red
    }
    Write-Host "`nPresiona ENTER para continuar al siguiente demo (CTRL+C para abortar)..."
    Read-Host | Out-Null
}

Write-Host "Run all demos - terminado" -ForegroundColor Cyan
