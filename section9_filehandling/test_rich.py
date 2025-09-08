from rich import traceback
traceback.install()

def brew_chai(flavor):
    if flavor != "masala":
        raise ValueError("Unspotted chai flavour...")  # Intentional error
    return "Your chai is ready!"

brew_chai("mint")
