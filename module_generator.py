from pathlib import Path
import re


def create_module(name):
    name = name.strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
        raise ValueError("Invalid module name")

    module_dir = Path("app/modules") / name
    module_dir.mkdir(parents=True, exist_ok=True)
    files = [
        "__init__.py",
        f"{name}_model.py",
        f"{name}_service.py",
        f"{name}_controller.py",
        f"{name}_route.py",
        f"{name}_schemas.py",
    ]
    for filename in files:
        file_path = module_dir / filename
        if not file_path.exists():
            file_path.touch()
        else:
            print(f"Already exists: {file_path}")

    print(f"\nModule '{name}' created successfully!")
    print(f"Location: {module_dir}")

if __name__ == "__main__":
    module_name = input("Enter module name: ")
    create_module(module_name)
