import subprocess
class Synopsis:
    @staticmethod
    def run_mafft(input_data):
        """
        Runs the MAFFT multiple sequence alignment tool on the given input data.

        Args:
            input_data (dict): Dictionary with sequence names as keys and sequences as values.

        Returns:
            list: List of dictionaries containing sequence names and aligned sequences.
        """
        input_content = Synopsis.parse_mafft_input(input_data)
        with open("temp.fasta", "w") as f:
            f.write(input_content)
        command = f"mafft --auto --anysymbol temp.fasta"
        out = subprocess.run(command, shell=True, capture_output=True)

        return Synopsis.parse_mafft_output(str(out.stdout))

    @staticmethod
    def parse_mafft_input(input_data):
        """
        Parses the input data into the format expected by MAFFT.

        Args:
            input_data (dict): Dictionary with sequence names as keys and sequences as values.

        Returns:
            str: MAFFT-compatible formatted input.
        """
        output = ""
        for key in input_data:
            output += f"> {key}\n"
            output += f"{input_data[key]}\n"
        return output

    @staticmethod
    def parse_mafft_output(mafft_output):
        """
        Parses the MAFFT output into a list of aligned sequences with their names.

        Args:
            mafft_output (str): MAFFT output as a string.

        Returns:
            list: List of dictionaries containing sequence names and aligned sequences.
        """
        sequences = []
        blocks = mafft_output.strip().split('>')[1:]
        print("BLOCKS", blocks)

        for block in blocks:
            lines = block.strip().split('\\n')

            name = lines[0].strip().split()[0]
            sequence = ''.join(line.strip() for line in lines[1:])

            sequences.append({'name': name, 'sequence': sequence})
        return sequences

    @staticmethod
    def visualize_alignments(alignments, highlight=None, offset=0):
        """
        Generates an HTML table to visualize sequence alignments.

        Args:
            alignments (list): List of dictionaries containing sequence names and aligned sequences.
            highlight (list): List of lists specifying positions to highlight for each sequence. The result object of a search can be used.
            offset (int): Offset for highlighted positions.

        Returns:
            str: HTML formatted table for visualization.
        """
        html_output = "<table border='0'>"
        html_output += "<tr><th>Name</th><th>Sequence</th></tr>"
        for i, alignment in enumerate(alignments):
            name = alignment['name']
            sequence = ""
            if highlight:
                highlight_offset = [n + offset for n in highlight[i]]
                char_count = 0
                for char in alignment['sequence']:
                    if char == "-":
                        sequence += "-"
                    else:
                        if char_count in highlight_offset:
                            sequence += f"<span style='color: red'>{char}</span>"
                        else:
                            sequence += char
                        char_count += 1
            else:
                sequence = ",".join(list(alignment['sequence']))
            html_output += f'<tr><td>{name}</td><td style="text-align: left; font-family: Volpiano; font-size:3em; white-space: nowrap;">{sequence}</td></tr>'
        html_output += "</table>"
        return html_output
