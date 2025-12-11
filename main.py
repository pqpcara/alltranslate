import asyncio
from googletrans import LANGUAGES, Translator

async def main():
    translator = Translator()
    translations = {}
    total_languages = len(LANGUAGES)
    print(f"Starting translation to {total_languages} languages. This may take a few minutes...")

    for i, lang_code in enumerate(LANGUAGES):
        try:
            await asyncio.sleep(0.1)
            translated = await translator.translate(text="17s at the top", dest=lang_code)
            translations[lang_code] = translated.text
            print(f"Progress: {i + 1}/{total_languages}", end="\r")
        except Exception as e:
            translations[lang_code] = "[ERROR IN TRANSLATION]"
            print(f"Error translating to code '{lang_code}': {e}")

    print("Translation completed for all languages.")

    output_lines = []
    for code, text in translations.items():
        language_name = LANGUAGES.get(code, f"Unknown code: {code}").capitalize()
        output_lines.append(f"{language_name}: {text}")

    output_text = "\n".join(output_lines)

    try:
        with open("translations.txt", "w", encoding="utf-8") as file:
            file.write(output_text)
        print("Translations saved in 'translations.txt'")
    except IOError as e:
        print(f"Unable to write to file 'translations.txt'.': {e}")

if __name__ == "__main__":
    asyncio.run(main())
