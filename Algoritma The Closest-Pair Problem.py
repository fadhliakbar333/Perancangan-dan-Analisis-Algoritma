import math

def jarak(t1, t2):
    return math.sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2)

def brute_force_terdekat(titik):
    min_jarak = float('inf')
    pasangan_terdekat = None
    n = len(titik)
    for i in range(n):
        for j in range(i + 1, n):
            d = jarak(titik[i], titik[j])
            if d < min_jarak:
                min_jarak = d
                pasangan_terdekat = (titik[i], titik[j])
    return pasangan_terdekat, min_jarak

def strip_terdekat(strip, d):
    min_jarak = d
    pasangan_terdekat = None
    strip.sort(key=lambda titik: titik[1])  # Urutkan berdasarkan koordinat y
    
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = jarak(strip[i], strip[j])
            if d < min_jarak:
                min_jarak = d
                pasangan_terdekat = (strip[i], strip[j])
    return pasangan_terdekat, min_jarak

def pasangan_terdekat_rekursif(titik):
    n = len(titik)
    if n <= 3:
        return brute_force_terdekat(titik)
    
    tengah = n // 2
    titik_tengah = titik[tengah]
    
    kiri_pasangan, kiri_jarak = pasangan_terdekat_rekursif(titik[:tengah])
    kanan_pasangan, kanan_jarak = pasangan_terdekat_rekursif(titik[tengah:])
    
    if kiri_jarak < kanan_jarak:
        pasangan_min, jarak_min = kiri_pasangan, kiri_jarak
    else:
        pasangan_min, jarak_min = kanan_pasangan, kanan_jarak
    
    strip = [t for t in titik if abs(t[0] - titik_tengah[0]) < jarak_min]
    strip_pasangan, strip_jarak = strip_terdekat(strip, jarak_min)
    
    if strip_pasangan and strip_jarak < jarak_min:
        return strip_pasangan, strip_jarak
    else:
        return pasangan_min, jarak_min

def pasangan_terdekat(titik):
    titik.sort()  # Urutkan berdasarkan koordinat x
    return pasangan_terdekat_rekursif(titik)

# Contoh penggunaan
data_titik = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pasangan, jarak_min = pasangan_terdekat(data_titik)
print("Pasangan titik terdekat:", pasangan)
print("Jarak minimum:", jarak_min)