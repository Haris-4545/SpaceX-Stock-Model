from pathlib import Path
import yaml

_CONFIG_DIR = Path(__file__).resolve().parents[3] / "configs"

def load_config(name: str = "base") -> dict:
    path = _CONFIG_DIR / f"{name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with open(path) as f:
        return yaml.safe_load(f)
    
def get_nested(cfg: dict, *keys, default=None):
    for key in keys:
        if not isinstance(cfg, dict):
            return default
        cfg = cfg.get(key, default)
    return cfg