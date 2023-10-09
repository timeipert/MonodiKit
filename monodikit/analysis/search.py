class Search:
    def __init__(self):
        pass

    @staticmethod
    def search_in_window(corpus, pattern, window):
        """
        Searches for a pattern within a window in a given corpus.

        Args:
            corpus (Corpus): The corpus containing the documents to search.
            pattern (str): The pattern to search for.
            window (int): The window length for the search.

        Returns:
            list: List of search results containing segments and corresponding chant information.
        """
        data = [(document, document.flat_neume_components) for document in corpus.documents]
        search_result = []
        for document in data:
            data_str = [f"{note.base}{note.octave}" for note in document[1]]
            segments = Search.search_pattern_in_window(data_str, pattern, window)
            if len(segments):
                search_result.append({"segments": segments, "chant": document[0]})
        return search_result

    @staticmethod
    def search_pattern_in_window(text, pattern, window_length):
        """
        Searches for a pattern within a window of text.

        Args:
            text (str): The text to search within.
            pattern (str): The pattern to search for.
            window_length (int): The window length for the search.

        Returns:
            list: List of segments containing window offset, indices, and the window.
        """
        text_length = len(text)
        segments = []
        for i in range(text_length - window_length + 1):
            window = text[i:i + window_length]
            window_indices = Search.is_pattern_in_window(window, pattern)
            if window_indices:
                segments.append({"window_offset": i, "ids": window_indices, "window": window})
        return segments

    @staticmethod
    def is_pattern_in_window(window, pattern):
        """
        Checks if a pattern is present in the given window.

        Args:
            window (str): The window to search within.
            pattern (str): The pattern to search for.

        Returns:
            list: List of indices where the pattern is found in the window.
        """
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

    @staticmethod
    def visualize_html(results):
        """
        Generates an HTML representation of search results.

        Args:
            results (list): List of search results.

        Returns:
            str: HTML formatted representation of the search results.
        """
        html = "<html><head><style>.notation {font-family: Volpiano; font-size:2em;white-space:nowrap}</style></head><body>"
        html += (f"<h2>Results</h2>"
                f"<table>")

        for result in results:
            notation = ""
            notation += '<td class="notation">'
            close_span = False
            for index, pitch in enumerate(result["chant"].volpiano):
                for segment in result["segments"]:
                    if close_span:
                        notation += "</span>"
                        close_span = False
                    if segment["window_offset"] + len(segment["window"])-1 == index:
                        notation += '</td><td class="notation">'
                    if segment["window_offset"] == index:
                        notation += '</td><td class="notation">'

                    for id in segment["ids"]:
                        if (id + segment["window_offset"]) == index:
                            notation += '<span style="color: red">'
                            close_span = True
                notation += pitch
                notation += "-"
            notation += "</td>"
            html += (
                f'<tr><td>{result["chant"].meta.initial_text} – {result["chant"].meta.document_id} - {result["chant"].meta.genre} </td>'
                f'{notation}</tr>')
        html += "</table></body></html>"
        return html

    @staticmethod
    def to_mafft_input(results, context=0):
        """
        Converts search results to input format for MAFFT.

        Args:
            results (list): List of search results.
            context (int): Additional context to include in the input.

        Returns:
            dict: Dictionary with formatted input for MAFFT.
        """
        mafft_input = {}
        for result in results:
            i = 1
            for segment in result['segments']:
                i += 1
                name = f'{result["chant"].meta.document_id.replace(" ", "")}-{i}'
                volp = result["chant"].volpiano
                sl = slice(segment["window_offset"] - context, segment["window_offset"] + len(segment["window"]) + context)
                mafft_input[name] = "".join(volp[sl])
        return mafft_input
