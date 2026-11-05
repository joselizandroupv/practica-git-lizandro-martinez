"""
Utileria de limpieza y resumen
"""


def to_mxn(valor, tasa: float = 18.58) -> float:
    """
    Convierte "valor" a MXN multiplicando por "tasa".
    """
    return float(valor) * float(tasa)


def clean_string(s_txt: str) -> str:
    """
    Limpiar espacios y capitaliza.
    """
    return " ".join(s_txt.strip().title().split())


# ORIGINAL.- "   CaRLOs    AnTOnIo              ToVAr          GarCIA    "
# STRIP().- "CaRLOs    AnTOnIo              ToVAr          GarCIA"
# TITLE().- "Carlos Antonio Tovar Garcia"
# SPLIT().- ['Carlos', 'Antonio', 'Tovar', 'Garcia']
# JOIN().- "Carlos Antonio Tovar Garcia"
