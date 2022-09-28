# downloadurl

Simply download any URL doing the following:

**Install**
```bash
python3 -m pip install downloadurl
```

**Use as CLI**
```bash
downloadurl https://upload.wikimedia.org/wikipedia/commons/8/8c/Cow_%28Fleckvieh_breed%29_Oeschinensee_Slaunger_2009-07-07.jpg cow
```

**Use as library**
```python
import downloadurl

filename = downloadurl.downloadurl("https://www.britannica.com/animal/cow", "cow")
# filename should be "cow.html"
```
