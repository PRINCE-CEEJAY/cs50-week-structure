from emoji import emojize

emoji_request = input("Input: ").strip()
emojized = emojize(emoji_request, language="alias")

print(emojized)
