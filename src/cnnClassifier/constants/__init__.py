from pathlib import Path

# Path(__file__) is .../src/cnnClassifier/constants/__init__.py
# We need to go up 4 levels to get to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# Now build the correct paths from the real root
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
