import re
# def extract_text_between_substrings(s, start_sub, end_sub):
#     start_index = s.find(start_sub)
#     if start_index == -1:
#         return None

#     start_index += len(start_sub)
#     end_index = s.find(end_sub, start_index)

#     if end_index == -1:
#         return None

#     return s[start_index:end_index].strip()

# def extract_text_between_substrings(s):
#     start_sub = 'Distribué par</h3>\r\n '
#     end_sub = '<br>'
#     s=s[0]
#     print(s)
#     start_index = s.find(start_sub)
#     if start_index == -1:
#         return None

#     start_index += len(start_sub)
#     end_index = s.find(end_sub, start_index)

#     if end_index == -1:
#         return None

#     return s[start_index:end_index].strip()


# def extract_text_between_substrings(self, s, pattern):
#         result = re.search(pattern, s, re.DOTALL)
        
#         return result.group(1).strip()
def extract_text_between_substrings(s):
    start_sub = 'Distribué par</h3>\r\n '
    end_sub = '<br>'
    
    start_index = s.find(start_sub)
    if start_index == -1:
        return None

    start_index += len(start_sub)
    end_index = s.find(end_sub, start_index)

    if end_index == -1:
        return None

    return s[start_index:end_index].strip()