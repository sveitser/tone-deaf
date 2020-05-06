from yattag import Doc
from collections import defaultdict
from pathlib import Path
import os
import re

snippets = defaultdict(list)
media_dir = Path("audio")
filenames = media_dir.glob("*.mp3")

for path in filenames:

    name = path.name
    identifier = os.path.splitext(name)[0]
    pinyin = identifier.split("_")[0]

    split = re.split(r"[1-4]", pinyin)
    n = len(split)
    if n == 1 or n == 2 and split[-1] == "":
        n_syl = 1
    else:
        n_syl = 2

    tones = re.findall(r"[1-4]", pinyin)
    if len(tones) == 1 and n_syl == 2:
        tones.append("5")

    key = "".join(tones)
    snippets[key].append(str(path))

doc, tag, text, line = Doc().ttl()

pairs = []
for key, values in snippets.items():
    vals = ",".join(f'"{v}"' for v in values)
    pairs.append(f"{key}: [{vals}]")


line("h1", "Play me.")
with tag("script", language="JavaScript"):
    doc.asis(
        """
    const snippetsByTone = {{
        {pairs}
    }}
    function play(first, second) {{
        const snippets = snippetsByTone[first.toString() + second]
        const fname = snippets[Math.floor(Math.random() * snippets.length)];
        return new Audio(fname).play()
    }}
    """.format(
            pairs=",".join(pairs)
        )
    )

with tag("table"):
    for first_tone in range(1, 5):
        with tag("tr"):
            for second_tone in range(1, 6):
                with tag("td"):

                    doc.stag(
                        "input",
                        type="submit",
                        value=f"{first_tone} {second_tone}",
                        onclick=f"play({first_tone}, {second_tone})",
                    )

print(doc.getvalue())
