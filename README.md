# cardprint

### To install
- have python 3; on OSx see [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)
- pip install pyqrcode
- pip install pypng
- pip install pyyaml
- pip install Pillow


### To launch
C:\github\cardprint>cardprint.py "VPMF2018 Kaelakaardi info Piletilevile - Meeskond.csv"


### CSV example without person picture:
```
eesnimi,perenimi,lisainfo,kaardigrupp,pildifail,kood
John,Doe,Most epic band ever,Esineja,,26071402
```
Configuration folder yaml contains all the card group settings.
### FONT names do not work in Windows 10 with installed fonts. Tested and got it to work only with arial

Experimental:
Company2 parameter does not work by default, but it logic is same as company1
