def searchW(documents, pattern, window):
    data = [(document.meta.id, document.flat_neume_components) for document in documents]
    search_result = []
    for document in data:
        data_str = [f"{note.base}{note.octave}" for note in document[1]]
        if search_pattern_in_window(data_str, pattern, window):
            search_result.append(document)
    return search_result


def search_pattern_in_window(text, pattern, window_length):
    text_length = len(text)
    pattern_length = len(pattern)

    for i in range(text_length - window_length + 1):
        window = text[i:i+window_length]
        if is_pattern_in_window(window, pattern):
            return True

    return False

def is_pattern_in_window(window, pattern):
    window_index = 0
    pattern_index = 0

    while window_index < len(window) and pattern_index < len(pattern):
        if window[window_index] == pattern[pattern_index]:
            pattern_index += 1

        window_index += 1

    return pattern_index == len(pattern)
