import os
print(os.environ['EnvUser'])
print(os.environ['EnvPas'])
EnvUser = os.environ["EnvUser"]
EnvPas = os.environ["EnvPas"]
print(f"USERNAME: {EnvUser}, PASSWORD: {EnvPas}")