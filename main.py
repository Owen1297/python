import os

def cls() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    return None

cls()
print("HI")