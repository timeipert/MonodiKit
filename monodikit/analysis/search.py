def search_in_window(corpus, pattern, window):
    data = [(document, document.flat_neume_components) for document in corpus.documents]
    search_result = []
    for document in data:
        data_str = [f"{note.base}{note.octave}" for note in document[1]]
        segments = search_pattern_in_window(data_str, pattern, window)
        if len(segments):
            search_result.append({"segments":segments, "chant": document[0]})
    return search_result

def search_pattern_in_window(text, pattern, window_length):
    text_length = len(text)
    segments = []
    for i in range(text_length - window_length + 1):
        window = text[i:i+window_length]
        window_indices = is_pattern_in_window(window, pattern)
        if window_indices:
            segments.append({"window_offset": i, "ids": window_indices, "window": window})
    return segments

def is_pattern_in_window(window, pattern):
    indices = []
    window_index = 0
    pattern_index = 0
    while window_index < len(window) and pattern_index < len(pattern):
        if window[window_index] == pattern[pattern_index]:
            indices.append(window_index)
            pattern_index += 1
        window_index += 1
    if pattern_index == len(pattern):
        return indices
    else:
        return None

