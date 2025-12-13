def get_snippet(text, positions, window_size=8):
    # extract text around match

    if not positions:
        return ""

    words = text.split()

    # take the first match
    center = positions[0]

    start = max(0, center - window_size)
    end = min(len(words), center + window_size + 1)

    return " ".join(words[start:end])
