from yattag import Doc

doc, tag, text, line = Doc().ttl()

line("h1", "Play me.")
with tag("script", language="JavaScript"):
    doc.asis(
        """
    let snippetsByTone
    fetch("snippets.json").then(response => response.json()).then( json => { snippetsByTone = json })

    function play(first, second) {{
        const snippets = snippetsByTone[first.toString() + second]
        const fname = snippets[Math.floor(Math.random() * snippets.length)];
        return new Audio(fname).play()
    }}
    """)

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
