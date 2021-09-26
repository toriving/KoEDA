SPACE_TOKEN = "\u241F"


def replace_space(text: str) -> str:
    return text.replace(" ", SPACE_TOKEN)


def revert_space(text: list) -> str:
    clean = (
        " ".join("".join(text).replace(SPACE_TOKEN, " ").split())
        .strip()
    )
    return clean
