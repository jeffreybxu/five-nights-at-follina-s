$Yesterday = (Get-Date) - (New-TimeSpan -Day 1)
$events=Get-WinEvent -LogName "microsoft-Windows-sysmon/operational" | where {$_.id -eq1} | Where-Object { $_.TimeCreated -ge $Yesterday }

for ($i = 1; $i -le 100; $i++ ) {
    Write-Progress -Activity "Searching for Follina artifacts..." -Status "$i% Complete:" -PercentComplete $i
    Start-Sleep -Milliseconds 40
}

$test = foreach ($event in $events)
{
if ($event.message | select-string -Pattern ".*msdt.exe.*" | select-string -Pattern ".*WINWORD.EXE.*")
{echo y | reg export HKEY_CLASSES_ROOT\ms-msdt C:\ms-msdt.reg
echo y | reg delete HKEY_CLASSES_ROOT\ms-msdt /f
break}
}

for ($i = 1; $i -le 100; $i++ ) {
    Write-Progress -Activity "Backing up registry..." -Status "$i% Complete:" -PercentComplete $i
    Start-Sleep -Milliseconds 40
}

for ($i = 1; $i -le 100; $i++ ) {
    Write-Progress -Activity "Removing ms-msdt protocol..." -Status "$i% Complete:" -PercentComplete $i
    Start-Sleep -Milliseconds 40
}

powershell -WindowStyle hidden -Command "& {[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.Messagebox]::Show('Follina Attack Vector has been neutralized.', 'SUCCESS')}"
#echo "Follina Attack Vector Neutralized"