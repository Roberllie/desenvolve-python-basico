import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

print("\nDigite uma frase e ela será emojizada:")
frase = input()  

frase_emojizada = emoji.emojize(frase, use_aliases=True)

print("\nFrase emojizada:")
print(frase_emojizada)
