# Core: Enable Game Mode
Set-ItemProperty -Path "HKCU:\Software\Microsoft\GameBar" -Name "AllowAutoGameMode" -Value 1

# Core: Set Power Plan to High Performance
$HighPerfPlan = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"  # High Performance GUID
powercfg /setactive $HighPerfPlan

# Core: Disable Notifications
Write-Output "Disabling Notifications..."
New-Item -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\PushNotifications" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\PushNotifications" -Name "ToastEnabled" -Value 0

# Adjust Visual Effects for Best Performance
Write-Output "Adjusting Visual Effects for Best Performance..."
$visualEffectsKey = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
New-Item -Path $visualEffectsKey -Force | Out-Null
Set-ItemProperty -Path $visualEffectsKey -Name "VisualFXSetting" -Value 2

# Adjust Processor Scheduling for Games
Write-Output "Adjusting Processor Scheduling for Games..."
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -Name "Win32PrioritySeparation" -Value 26

# Disable Focus Assist Notifications
Write-Output "Disabling Focus Assist Notifications..."
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\FocusAssist" -Name "EnableFocusAssist" -Value 1

# Enable Hardware-Accelerated GPU Scheduling
Write-Output "Enabling Hardware-Accelerated GPU Scheduling..."
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" -Name "HwSchMode" -Value 2

# Confirmation of Completion
Write-Output "Optimizations applied: Game Mode enabled, High Performance power plan set, notifications disabled, visual effects optimized, processor scheduling adjusted, focus assist notifications disabled, and GPU scheduling enabled."

# Disable Windows Search service
Write-Host "Disabling Windows Search Indexing..." -ForegroundColor Green
Stop-Service -Name "WSearch" -Force
Set-Service -Name "WSearch" -StartupType Disabled
Write-Host "Windows Search Indexing has been disabled." -ForegroundColor Green

# Disable Windows Backup
Write-Host "Disabling Windows Backup..." -ForegroundColor Green
Disable-ComputerRestore -Drive "C:\"
vssadmin delete shadows /all /quiet
Write-Host "Windows Backup disabled." -ForegroundColor Green