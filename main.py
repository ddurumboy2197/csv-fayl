import os
import shutil

def birlashtir_fayl(fayl_nomi, kelgan_fayl_nomi):
    try:
        with open(fayl_nomi, 'w') as yangi_fayl:
            for fayl in os.listdir('.'):
                if fayl.endswith('.txt'):
                    with open(fayl, 'r') as f:
                        yangi_fayl.write(f.read() + '\n')
        shutil.move(fayl_nomi, kelgan_fayl_nomi)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

birlashtir_fayl('yangi_fayl.txt', 'birlashtirilgan_fayl.txt')
```

```python
import os
import shutil

def birlashtir_fayl(fayl_nomi, kelgan_fayl_nomi):
    try:
        with open(fayl_nomi, 'w') as yangi_fayl:
            for fayl in os.listdir('.'):
                if fayl.endswith('.txt'):
                    with open(fayl, 'r') as f:
                        yangi_fayl.write(f.read() + '\n')
        shutil.move(fayl_nomi, kelgan_fayl_nomi)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

birlashtir_fayl('yangi_fayl.txt', 'birlashtirilgan_fayl.txt')
