from os import listdir, system


if "layer.zip" in listdir():
    system("rm layer.zip")
system("pip install --target dependencies -r lambda_dependencies.txt")
system("sudo apt-get install zip")
system("zip -r layer.zip dependencies")
system("rm -r dependencies")
