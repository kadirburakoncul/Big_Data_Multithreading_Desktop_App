import re

def sembol_remove_bulma(satir):
	return re.sub(r"[^a-zA-Z0-9 çğıöşüÇĞİÖŞÜ]", "", satir)