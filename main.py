class Champion: 
    def __init__(self,name,pdv,mres,armor,ap,ad,ats,atsRatio,items=None):
        self.name = name
        self.pdv = pdv
        self.armor = armor
        self.mres = mres
        self.ap = ap
        self.ad = ad
        self.ats = ats
        self.atsRatio = atsRatio 
        self.items = items

    def computestats(self):
        if self.items is not None :
            for item in self.items: 
                self.pdv += item.pdv
                self.armor += item.armor
                self.mres += item.mres
                self.ad += item.ad
                self.ap += item.ap
                self.ats += item.ats*self.atsRatio
                
        
class Items: 
    def __init__(self,name,pdv,mres,armor,ap,ad,ats):
        self.name = name
        self.pdv = pdv
        self.armor = armor
        self.mres = mres
        self.ap = ap
        self.ad = ad
        self.ats = ats

y = Items("Boris",3000,80,80,500,400,0.5)
x = Champion("Bassem",3000,80,80,500,400,0.765,0.659,[y])
x.computestats()

print(f"""
name:{x.name}
pdv:{x.pdv}
armor:{x.armor}
mres:{x.mres}
ap:{x.ap}
ad:{x.ad}
ats:{x.ats}
atsRatio:{x.atsRatio}
""")

print(f"""
name:{y.name}
pdv:{y.pdv}
armor:{y.armor}
mres:{y.mres}
ap:{y.ap}
ad:{y.ad}
ats:{y.ats}
""")