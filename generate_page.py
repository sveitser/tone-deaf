from yattag import Doc, indent

COLORS = {
    1: "#e30000",
    2: "#02b31c",
    3: "#1510f0",
    4: "#8900bf",
    5: "#777777",
}

doc, tag, text, line = Doc().ttl()

doc.asis("<!DOCTYPE html>")

with tag("html"):
    with tag("head"):
        with tag("title"):
            doc.asis("Word tones cheatsheet")

        with tag("script", language="JavaScript", src="code.js"):
            pass

    with tag("body"):
        line("h1", "Play me.")
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
                                    f"background-image: linear-gradient(to right, {COLORS[first_tone]} 48%, #ffffff 49%, #ffffff 51%, {COLORS[second_tone]} 52%);"
                                    "border-radius: 5px;"
                                    "border: none;"
                                    "min-width: 150px;"
                                    "min-height: 80px;"
                                ),
                            )

print(indent(doc.getvalue()))
