def reverse(st):
    # Your Code Here
    return ' '.join(st.split(" ")[::-1]).strip(" ")

print(reverse("The quick brown fox jumps over the lazy dog"))