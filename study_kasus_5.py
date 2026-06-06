#kasus 1: sistem penilaian

nilai = float(input("Masukkan nilai (0 - 100): "))

if nilai >= 80:
    Grade = "A"
elif nilai >= 70:
    Grade = "B"
elif nilai >= 60:
    Grade = "C"
elif nilai >= 50:
    Grade = "D"
else:
    Grade = "E"

print(f"Nilai Anda: {nilai}")
print(f"Grade Anda: {Grade}")

nilai = float(input("Masukkan nilai (0-100): "))

match nilai :
    case n if n >= 80:
        print('Grade: A')
    case n if n >= 70:
        print('Grade: B')
    case n if n >= 60:
        print()