import json
import os
import re
from collections import defaultdict
from pathlib import Path

snippets = defaultdict(list)
media_dir = Path("audio")
filenames = media_dir.glob("*.mp3")

for path in filenames:

    name = path.name
    identifier = os.path.splitext(name)[0]
    pinyin = identifier.split("_")[0]

    tones = re.findall(r"[1-4]", pinyin)
    if len(tones) == 1:
        tones.append("5")

    key = "".join(tones)
    snippets[key].append(str(path))

with open("snippets.json", "w") as f:
    json.dump(snippets, f, indent=2)
