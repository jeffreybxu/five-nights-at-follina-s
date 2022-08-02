$events=Get-WinEvent -LogName "microsoft-Windows-sysmon/operational" | where {$_.id -eq 1}

foreach ($event in $events)
{
if ($event.message | select-string -Pattern ".*winword.*")
{iex -Command ("reg delete HKEY_CLASSES_ROOT\ms-msdt /f")}
}


