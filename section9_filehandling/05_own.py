def brew_chai(flavour):
    if flavour not in ["masala","ginger","elaichai"]:
        raise ValueError("Unsupportted chai flavour...")
    print(f"bewing {flavour} chai...")
brew_chai("mint")