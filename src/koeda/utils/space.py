SPACE_TOKEN = "___"

def replace_space(text: str) -> str:
    return text.replace(" ", SPACE_TOKEN)

def revert_space(text: list) -> str:
    return ' '.join(''.join(text).replace(SPACE_TOKEN, ' ').split())

