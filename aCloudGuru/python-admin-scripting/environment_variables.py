import os

stage = os.getenv("stage",default="dev").upper()
if stage.startswith("STAGE"):
    print(f' You are running the script in {stage}')
elif stage.startswith("PROD"):
    print(f' Danger !!! You are running the script in {stage}')