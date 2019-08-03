import os
import sys
import shutil
import base64

amb = sys.argv[1]

dirpath = os.getcwd()
print("full work directory is : " + dirpath)

foldername = os.path.basename(dirpath)
print("current directory is : " + foldername)

yamlfolder = dirpath + "/" + amb

for filename in os.listdir(yamlfolder):
    if filename != "Jenkinsfile":
        newfilename = filename.split("_")[0] + "_" +filename.split("_")[1] + ".yml"
        print("creating yaml file : " + newfilename)
        shutil.copy2('secret-default.yaml', newfilename)

        data = open(yamlfolder+"/"+filename, "r").read()
        encoded = base64.b64encode(data)

        namespace = filename.split("_")[0]
        secretname = filename.split("_")[1]
        filename = filename.split("_")[2]

        with open(newfilename) as f:
            newText=f.read().replace("ambiente", namespace)
            newText=newText.replace("secretname", secretname)
            newText=newText.replace("filename", filename)
            newText=newText.replace("filecrypted", encoded)

        with open(newfilename, "w") as f:
            f.write(newText)
        continue
    else:
        continue

print("Finished Creation Process")
