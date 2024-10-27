# OK this script will reset the state of the development environment
# to do this we need to: 
# step1 delete the folder in the root of this repo called "my_images"
# step2 delete the test folder incase while running app code the state of the test folder was changed
# step3 copy the folder test-backup to root of this repo and rename it to test

# Define the root directory of the repository
$rootDir = (Get-Location).Path

# Step 1: Delete the "my_images" folder if it exists
$myImagesDir = Join-Path -Path $rootDir -ChildPath "my_images"
if (Test-Path -Path $myImagesDir) {
    Remove-Item -Path $myImagesDir -Recurse -Force
    Write-Output "Deleted folder: my_images"
} else {
    Write-Output "Folder 'my_images' does not exist"
}

# Step 2: Delete the "test" folder if it exists
$testDir = Join-Path -Path $rootDir -ChildPath "test"
if (Test-Path -Path $testDir) {
    Remove-Item -Path $testDir -Recurse -Force
    Write-Output "Deleted folder: test"
} else {
    Write-Output "Folder 'test' does not exist"
}

# Step 3: Copy the "test-backup" folder to the root and rename it to "test"
$testBackupDir = Join-Path -Path $rootDir -ChildPath "test-backup"
if (Test-Path -Path $testBackupDir) {
    Copy-Item -Path $testBackupDir -Destination $testDir -Recurse
    Write-Output "Copied folder 'test-backup' to 'test'"
} else {
    Write-Output "Folder 'test-backup' does not exist"
}