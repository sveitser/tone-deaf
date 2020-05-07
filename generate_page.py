from yattag import Doc

COLORS = {
    1: "#e30000",
    2: "#02b31c",
    3: "#1510f0",
    4: "#8900bf",
    5: "#777777",
}

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
    """
    )

with tag("table", cellpadding=10):
    for first_tone in range(1, 5):
        with tag("tr"):
            for second_tone in range(1, 6):
                with tag("td"):

                    doc.stag(
                        "input",
                        type="submit",
                        value="    ",
                        onclick=f"play({first_tone}, {second_tone})",
                        style=(
                            f"background-image: linear-gradient(to right, {COLORS[first_tone]} 47%, #ffffff 48%, #ffffff 52%, {COLORS[second_tone]} 53%);"
                            "border-radius: 5px;"
                            "border: none;"
                            "min-width: 150px;"
                            "min-height: 80px;"
                        ),
                    )

print(doc.getvalue())
