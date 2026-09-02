class RdsConcatenator:
    def __init__(self):
        self.message_buffer = []
        self.pattern = None
        self.pattern_index = 0

    def input_rds_text(self, text):
        # If we have a pattern, check if this text continues it
        if self.pattern is not None:
            if text == self.pattern[self.pattern_index]:
                # Pattern continues
                self.pattern_index = (self.pattern_index + 1) % len(self.pattern)
                return
            else:
                # Pattern is broken! Reset and start new message with this text
                self.message_buffer = [text]
                self.pattern = None
                self.pattern_index = 0
                return
        
        # No active pattern, check if this text is already in buffer
        if text in self.message_buffer:
            # Found repetition! Pattern starts from first occurrence
            idx = self.message_buffer.index(text)
            self.pattern = self.message_buffer[idx:]
            self.message_buffer = self.pattern[:]  # Keep only one cycle
            self.pattern_index = 1 % len(self.pattern)
        else:
            # New unique text
            self.message_buffer.append(text)

    def get_text(self):
        return "".join(self.message_buffer)
###############################################################################
rds = RdsConcatenator()
rds.input_rds_text("Hello ")      # Remembers "Hello "
rds.input_rds_text("darkness, ")  # Remembers "darkness, "
rds.input_rds_text("my old ")     # Remembers "my old"
rds.input_rds_text("friend.")     # Remembers "friend."

print(rds.get_text())             # Returns the elements concatenated together

# Returns
# >>> Hello darkness, my old friend.

rds.input_rds_text("Hello ")
rds.input_rds_text("world!")
rds.input_rds_text("Hello ")    # Creating "Hello world!" text
rds.input_rds_text("world!")    # part of repeating text

print(rds.get_text())