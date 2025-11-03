#!/usr/bin/env python3
import subprocess
from pathlib import Path
from uuid import uuid4
from datetime import datetime, timezone

def main() -> None:
    base_dir = Path(__file__).resolve().parent
    issues_dir = base_dir / "issues"
    issues_dir.mkdir(parents=True, exist_ok=True)

    issue_id = str(uuid4())
    file_path = issues_dir / f"{issue_id}.jsonc"

    whoami_result = str(subprocess.run("whoami", stdout=subprocess.PIPE, shell=True, encoding="utf-8").stdout).strip()

    with open(file_path, "x", encoding="utf-8") as f:
        f.write("""
{
    "id": \"""" + issue_id + """\",
    "desc": "SSD corruption during large data copy in Windows 11",
    "status": "announced", // discovered|announced|identified|fixing|fixed
    "recurrence": false, // If the same issue has occurred before and was once fixed, and this problem is a recurrence of that issue, list the previous issue ID(s) here. If not, use `false`.
    "windows": {
        "editions": ["11:any"], // <7|8|8.1|10|11>:<any|starter|home-basic|home-premium|ultimate|professional|enterprise|noname|pro|rt|home|pro-s|pro-workstation|enterprise-ltsb|pro-education|education|mobile|mobile-enterprise|iot-core|other>
        "updates": ["KB5063878", "KB5062660"] // Windows Update ID
    },
    "conditions": {}, // Specify the software ID, version, and whether the condition is essential to reproducing the problem. Example: {"com.obsproject.Studio": {"versions": ["32.0.1", "32.0.2"], "require": true}} (The issue only occurs if you have the 32.0.1 or 32.0.2 version of OBS Studio installed.)
    "effects": {}, // Specify which software and versions this issue affects. It doesn't have to be all software. The syntax is almost the same as `conditions`, except that `require` is not needed.
    "timestamps": { // The change history of the problem file using an ISO 8601 formatted timestamp, the editor, and a description.
        \"""" + datetime.now(timezone.utc).isoformat() + """\": {"by": \"""" + whoami_result + """\", "desc": "Added this problem file"}
    }
}
""".strip())

    print(str(file_path))

if __name__ == "__main__":
    main()
