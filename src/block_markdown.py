def markdown_to_blocks(markdown):
    document = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        document.append(block.strip())
    return document