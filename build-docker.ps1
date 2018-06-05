#
# This is a workaround for trying to build docker images while in a OneDrive
#  managed folder
#
# See: https://github.com/docker/for-win/issues/1290
#

$buildFolder = "battlestern"
$buildDirectory = "$Env:TMP\$buildFolder"
$oldLocation = Get-Location

New-Item -Path $buildDirectory -ItemType directory
Copy-Item Dockerfile $buildDirectory
Copy-Item requirements.txt $buildDirectory
Copy-Item -Path "$oldLocation\battlestern" -Recurse -Destination $buildDirectory -Container
Copy-Item -Path "$oldLocation\tests" -Recurse -Destination $buildDirectory -Container

Set-Location $buildDirectory
docker build -t battlestern .

Set-Location $oldLocation
Remove-Item -Path $buildDirectory -Recurse -Force