def end_with_ing(input_string):
    if input_string[-3:] == "ing":
    # if "ing" in input_string:   - Be careful as this will compare to "ing" being anywhere in the string.
        return True
    else:
        return False


print(end_with_ing("Running"))
print(end_with_ing("Runner"))
