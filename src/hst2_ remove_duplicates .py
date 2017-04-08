def remove_duplicates(string):
    new_string = set(string)
    duplicates_count = len(string) - len(set(string))
    return new_string, duplicates_count

print(remove_duplicates('aaabbbac'))