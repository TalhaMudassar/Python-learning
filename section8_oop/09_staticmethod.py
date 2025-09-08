class chaiutils:
    @staticmethod
    def clean_ingridients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "water,  milk,  ginger,  honey"

cleaned = chaiutils.clean_ingridients(raw)
print(cleaned)
