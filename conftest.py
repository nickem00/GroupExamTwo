import sys
from pathlib import Path

# Lägg till src-katalogen till sys.path för att tillåta import av moduler
sys.path.append(str(Path(__file__).parent.resolve() / "src"))
