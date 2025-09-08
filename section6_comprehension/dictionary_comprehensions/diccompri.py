tea_price_pkr = {
    "Masala chai":40,
    "Green tea":30,
    "Lemon tea":200
}

tea_price_usd = {tea:pricee * 264 for tea,pricee in tea_price_pkr.items()}
print(tea_price_pkr)