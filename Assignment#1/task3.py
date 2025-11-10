class Package:
    def __init__(self,packageId,weightInKg):
        self.packageId=packageId
        self.weightInKg=weightInKg


class Drone:
    def __init__(self,droneId,maxLoadInKg):
        self.droneId=droneId
        self.maxLoadInKg=maxLoadInKg
        self._status='idle'
        self.currentPackage=None
        self.deliveryTimer=0

    def getStatus(self):
        return self._status

    def setStatus(self,newStatus):
        if newStatus in ['idle','delivering','charging']:
            self._status=newStatus

    def assignPackage(self,packageObj):
        if self._status=='idle' and packageObj.weightInKg<=self.maxLoadInKg:
            self.currentPackage=packageObj
            self.setStatus('delivering')
            self.deliveryTimer=2
            return True
        return False


class FleetManager:
    def __init__(self):
        self.drones={}
        self.pendingPackages=[]

    def dispatchJobs(self):
        for p in self.pendingPackages[:]:
            for d in self.drones.values():
                if d.getStatus()=='idle':
                    if d.assignPackage(p):
                        self.pendingPackages.remove(p)
                        break

    def simulationTick(self):
        for d in self.drones.values():
            if d.getStatus()=='delivering':
                d.deliveryTimer-=1
                if d.deliveryTimer<=0:
                    d.setStatus('charging')
                    d.currentPackage=None
            elif d.getStatus()=='charging':
                d.setStatus('idle')

fm=FleetManager()
d1=Drone("D1",10)
d2=Drone("D2",5)
fm.drones[d1.droneId]=d1
fm.drones[d2.droneId]=d2
p1=Package("P1",4)
p2=Package("P2",8)
p3=Package("P3",6)
fm.pendingPackages=[p1,p2,p3]
for i in range(5):
    fm.dispatchJobs()
    fm.simulationTick()
    for d in fm.drones.values():
        print(d.droneId,d.getStatus())
    print()
