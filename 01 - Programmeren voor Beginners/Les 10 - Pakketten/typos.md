### 10.6.1.2 datetime

Het voorbeeld is heel onduidelijk.
Input:
```python
from datetime import date
d = date(2002, 12, 31)
d.replace(day=26)
print(d)
```
Output:
```
2002-12-31
```
Je ziet hier `d.replace(day=26)` en verwacht dus dat `d` verandert, maar dat gebeurt niet. De `replace`-methode maakt een nieuwe datum aan, maar wij slaan die niet op.
```python
d = d.replace(day=26)
```
De output is dan:
```
2002-12-26
```