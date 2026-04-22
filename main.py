#!/usr/bin/env python3
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load env before importing runner
load_dotenv()

from src.runner import ClaimbackRadar


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path-to-input-json>")
        print("Example: python main.py examples/netflix_input.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        user_input = json.load(f)

    radar = ClaimbackRadar()
    result = radar.run(user_input)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
