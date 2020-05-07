let cache
let snippetsByTone

const numCached = 3

fetch("snippets.json").then(response => response.json()).then( json => {
    snippetsByTone = json
    cache = new Object()
    for (const key in snippetsByTone) {
        cache[key] = new Array()
        for (const _ of Array(numCached).keys()) {
            cacheSnippet(key)
        }
    }
})

function cacheSnippet(key){
    const snippets = snippetsByTone[key]
    const fname = snippets[Math.floor(Math.random() * snippets.length)];
    cache[key].push(new Audio(fname))
}

function play(first, second) {
    key = first.toString() + second
    const audio = cache[key].pop()
    if (audio != undefined) {
        audio.play()
    }
    cacheSnippet(key)
}
