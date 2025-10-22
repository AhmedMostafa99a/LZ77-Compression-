class Tag:
    def __init__(self, dis: int, length: int, next_char: str):
        self.dis = dis
        self.len = length
        self.next = next_char

    def __repr__(self):
        # mimic C++ printing of char (null char will appear invisible)
        return f"Tag(dis={self.dis}, len={self.len}, next={repr(self.next)})"


class lz77:
    def compress(self, raw_data: str):
        raw_data = raw_data + '\0'
        look_up_window = len(raw_data) // 2
        size = len(raw_data)
        tags = []
        current_string = ""
        tags.append(Tag(0, 0, raw_data[0]))
        last=0
        i = 1
        while i < size:
            pattern = ""
            is_repeated = False

            if len(current_string) == 0:
                pattern_size = 1
                while pattern_size < look_up_window and i + pattern_size - 1 < size + 1:
                    pattern += raw_data[i + pattern_size - 1]
                    if not (i >= pattern_size):
                        break
                    if raw_data[i - pattern_size:i] != pattern:
                        pattern_size += 1
                        continue

                    pattern_counter = 0
                    end_of_pattern = None
                    next_differnt_char = '\0'
                    k = i
                    while k < i + look_up_window and k < size - 1:
                        if raw_data[k] == pattern[pattern_counter % pattern_size]:
                            pattern_counter += 1
                        else:
                            break

                        next_differnt_char = raw_data[k + 1]
                        end_of_pattern = k + 1
                        k += 1

                    if (pattern_counter // pattern_size) > 1:
                        i = end_of_pattern
                        is_repeated = True
                        tags.append(Tag(pattern_size, pattern_counter, next_differnt_char))
                        break

                    pattern_size += 1

            if is_repeated:
                i+=1
                continue
            current_string += raw_data[i]

            ind = -1  
            if i - 2 * len(current_string) + 1 >= 0:
                search_end = i - 2 * len(current_string) + 1
                ind = raw_data.rfind(current_string, 0, search_end)

            if ind == -1:
                if len(current_string) == 1:
                    tags.append(Tag(0, 0, raw_data[i]))
                else:
                    tags.append(Tag(i - last - len(current_string) + 1, len(current_string) - 1, current_string[-1]))
                current_string = ""
            else:
                last = ind
                i += 1
                continue

            i += 1
        if tags and tags[-1].dis == 0 and tags[-1].len == 0 and tags[-1].next == '\0':
            tags.pop()

        return tags

    def decompress(self, tags):
        ans = ""
        for t in tags:
            while t.len > t.dis:
                if t.dis == 0:
                    ans += ""
                else:
                    start = len(ans) - t.dis
                    ans += ans[start:start + t.dis]
                t.len -= t.dis

            if t.dis == 0:
                ans += ""
            else:
                start = len(ans) - t.dis
                ans += ans[start:start + t.len]

            ans += t.next

        return ans


if __name__ == "__main__":
    test = lz77()
    tags = test.compress("AABABABABA")
    for i in tags:
        print(i.dis, i.len, i.next)
    print(test.decompress(tags))
