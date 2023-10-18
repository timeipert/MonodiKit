from .utility import Utility
class Segment:
    """  Represents a segment found in a Search.  """
    def __init__(self, indices, window, window_offset):
        self.indices = indices
        self.window = window
        self.window_offset = window_offset

class SearchResult:
    """ Represents a search result with information of chant and one or multiple found segments. """
    def __init__(self, chant, segments):
        self.chant = chant
        self.segments = segments

class Search:
    def __init__(self):
        pass

    @staticmethod
    def search_in_window(corpus, pattern, window, preprocess=None):
        """
        Searches for a pattern within a window in a given corpus.

        Args:
            corpus (Corpus): The corpus containing the documents to search.
            pattern (str): The pattern to search for.
            window (int): The window length for the search.
            preprocess (str): The window length for the search.

        Returns:
            list: List of search results containing segments and corresponding chant information.
        """
        search_result = []
        if preprocess == "intervals":
            data = [(document, Utility.compute_intervals(document.flat_neume_components)) for document in corpus.documents]
            for document in data:

                data_str = [f"{intv}" for intv in document[1]]

                segments = Search.search_pattern_in_window(data_str, pattern, window)
                if len(segments):
                    result_object = SearchResult(document[0], segments)
                    search_result.append(result_object)
        else:
            data = [(document, document.flat_neume_components) for document in corpus.documents]
            for document in data:

                data_str = [f"{note.base}{note.octave}" for note in document[1]]
                segments = Search.search_pattern_in_window(data_str, pattern, window)
                if len(segments):
                    result_object = SearchResult(document[0], segments)
                    search_result.append(result_object)
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
                segment = Segment(window_indices, window, i)
                segments.append(segment)
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
        # Define the style for the Volpiano notation
        notation_style = ' style="font-family: Volpiano; font-size: 2em; white-space: nowrap;" '

        # Initialize the HTML string
        html = (
            "<h2>Results</h2>"
            "<table>"
        )

        # Iterate through each search result and generate HTML representation
        for result in results:
            notation = ""
            notation += f'<td {notation_style}>'  # Start a table cell with Volpiano style

            close_span = False  # Flag to close the span tag for highlighting
            broken = False  # Flag to indicate if highlighting is broken

            # Iterate through the volpiano representation of the chant
            for index, pitch in enumerate(result.chant.volpiano):
                for segment in result.segments:
                    for id in segment.indices:
                        if (id + segment.window_offset) == index:
                            notation += '<span style="color: red">'  # Start highlighting
                            close_span = True
                            broken = True
                            break
                    if broken:
                        broken = False
                        break

                # Add the pitch to the notation
                notation += pitch
                notation += "-"

                if close_span:
                    notation += "</span>"  # Close the highlighting span
                    close_span = False

            notation += "</td>"

            # Construct the row with chant information and notation
            html += (
                f'<tr><td style="white-space: nowrap">{result.chant.meta.initial_text} - '
                f'{result.chant.meta.document_id} - {result.chant.meta.genre} </td>'
                f'<td>{len(result.segments)}</td>'
                f'{notation}</tr>'
            )

        # Close the table
        html += "</table>"
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
            for segment in result.segments:
                i += 1
                name = f'{result.chant.meta.document_id.replace(" ", "")}-{i}'
                volp = result.chant.volpiano
                sl = slice(segment.window_offset - context, segment.window_offset + len(segment.window) + context)
                mafft_input[name] = "".join(volp[sl])
        return mafft_input
