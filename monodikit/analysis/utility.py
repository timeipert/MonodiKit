def compute_intervals(neume_components, start_asterisk = False, filter_division_change = False):
    note_to_num = {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'A': 6, 'B': 7}
    if start_asterisk:
        intervals = ["*"]
    else:
        intervals = []
    count_div_changes = 0
    for i in range(1, len(neume_components)):
        if filter_division_change and neume_components[i-1].index[0:-4] != neume_components[i].index[0:-4]:
            count_div_changes += 1
            continue
        prev_note_val = (neume_components[i - 1].octave * 7) + note_to_num[neume_components[i - 1].base]
        curr_note_val = (neume_components[i].octave * 7) + note_to_num[neume_components[i].base]
        interval = curr_note_val - prev_note_val
        if interval >= 0:
            intervals.append(interval)
        else:
            intervals.append(interval)
    return intervals

