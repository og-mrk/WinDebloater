import os

print("Welcome to WinDebloater! Press Enter to start the debloat...")
input()
def bloatware_uninstall():
    os.system("Get-AppxPackage Microsoft.Microsoft3DViewer | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.BingWeather | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.GetHelp | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.WindowsMaps | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.YourPhone | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.XboxApp | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.MixedReality.Portal | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.SkypeApp | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.WindowsFeedbackHub | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.MicrosoftSolitaireCollection | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage SpotifyAB.SpotifyMusic | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.Getstarted | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.MicrosoftStickyNotes | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.Office.OneNote | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.MicrosoftOfficeHub | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.MSPaint | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.WindowsSoundRecorder | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.People | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.WindowsCalculato | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.Windows.PeopleExperienceHost | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.Todos | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.PowerAutomateDesktop | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Microsoft.BingNews | powershell Remove-AppxPackage")
    os.system("Get-AppxPackage Clipchamp.Clipchamp | powershell Remove-AppxPackage")
bloatware_uninstall()
os.system("power_plan.bat")