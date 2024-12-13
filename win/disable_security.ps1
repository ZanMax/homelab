# Disable Windows Defender
Write-Host "Disabling Windows Defender..." -ForegroundColor Green
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableBehaviorMonitoring $true
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisablePrivacyMode $true
Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true
Set-MpPreference -DisableArchiveScanning $true
Write-Host "Windows Defender disabled." -ForegroundColor Green

# Disable UAC
Write-Host "Disabling User Account Control (UAC)..." -ForegroundColor Green
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLUA" -Value 0
Write-Host "UAC disabled." -ForegroundColor Green

Write-Host "All requested features are disabled. A restart may be required for changes to take effect." -ForegroundColor Yellow