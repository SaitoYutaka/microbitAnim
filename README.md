# microbitAnim


![window](img/image000.jpg)

```python
from microbit import *
anim00 = Image("66066:60606:06660:60606:66066")
anim01 = Image("00000:66066:60606:06660:60606")
anim02 = Image("00000:00000:66066:60606:06660")
anim03 = Image("00000:00000:00000:66066:60606")
anim04 = Image("00000:00000:00000:00000:66066")
anim05 = Image("00000:00000:00000:00000:00000")
anim06 = Image("66066:00000:00000:00000:00000")
anim07 = Image("60606:66066:00000:00000:00000")
anim08 = Image("06660:60606:66066:00000:00000")
anim09 = Image("60606:06660:60606:66066:00000")
anim = [
    anim00, anim01, anim02, anim03, anim04, anim05, anim06,
    anim07, anim08, anim09]
while True:
    display.show(anim, delay=200)

```
