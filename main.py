import frases

if __name__ == "__main__":
    frase_del_dia = frases.obtener_frase()
    print("\n" + *50)
    print(f"FRASE MOTIVADORA".CENTER(50))
    print("=")
    print("\n {frase_del_dia}\n")
    print("="*50)