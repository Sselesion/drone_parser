def format_text(text):
    return " " + text.lower().replace("\n", " ").strip()


if __name__ == "__main__":
    print(
        format_text(
            text="""
        !!СЮДА ВСТАВИТЬ СВОЙ ТЕКСТ!!
        """
        )
    )
