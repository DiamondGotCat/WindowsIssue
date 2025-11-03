#!/usr/bin/env python3
import os
import json

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    issues_dir = os.path.join(script_dir, "issues")
    index_file = os.path.join(script_dir, "index.json")

    if not os.path.exists(issues_dir):
        print(f"Not found: {issues_dir}")
        return

    filenames = [
        os.path.splitext(f)[0]
        for f in os.listdir(issues_dir)
        if os.path.isfile(os.path.join(issues_dir, f))
    ]

    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(filenames, f, ensure_ascii=False)

    print(f"Indexed: {index_file}")

if __name__ == "__main__":
    main()
