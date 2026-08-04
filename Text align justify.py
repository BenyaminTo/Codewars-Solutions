def justify(text, width):
    if not text:
        return ""
    
    words = text.split()
    if not words:
        return ""

    # 1.Group words into lines (Greedy approach - fit as many words as possible per line)
    lines = []
    current_line = []
    current_length = 0  # Total length of words in current line (excluding spaces)
    
    for word in words:
        word_len = len(word)
        # Calculate required length if this word is added (including spaces between words)
        needed_length = current_length + word_len + (len(current_line) if len(current_line) > 0 else 0)
        
        if needed_length <= width:
            # Word fits in the current line
            current_line.append(word)
            current_length += word_len
        else:
            # Word doesn't fit, start a new line
            lines.append(current_line)
            current_line = [word]
            current_length = word_len
            
    # Don't forget the last line
    if current_line:
        lines.append(current_line)
        
    # 2.Justify the lines
    justified_lines = []
    for i, line_words in enumerate(lines):
        is_last_line = (i == len(lines) - 1)
        
        # Last line is left-aligned with single spaces between words (no justification)
        if is_last_line:
            justified_lines.append(" ".join(line_words))
        else:
            n = len(line_words)
            # Single-word lines don't need extra spaces at the end
            if n == 1:
                justified_lines.append(line_words[0])
            else:
                # Calculate total spaces needed
                total_chars = sum(len(w) for w in line_words)
                total_spaces = width - total_chars
                gaps = n - 1  # Number of gaps between words
                
                # Base spaces per gap + extra spaces distributed from left to right
                base_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                # Build the justified line
                parts = []
                for j in range(n - 1):
                    # Larger gaps go first (left side), then smaller gaps
                    space_count = base_spaces + (1 if j < extra_spaces else 0)
                    parts.append(line_words[j])
                    parts.append(" " * space_count)
                
                # Add the last word
                parts.append(line_words[-1])
                justified_lines.append("".join(parts))
                
    # 3.Join all lines with newlines
    return '\n'.join(justified_lines)