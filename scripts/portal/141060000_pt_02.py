# 141060000
from net.swordie.ms.client.character.skills.temp import CharacterTemporaryStat

def init():
    # Ride Vehicle Check
    if sm.getnOptionByCTS(CharacterTemporaryStat.RideVehicle) == 1930000: # Riena Skiff used in Riena Strait
        sm.removeCTS(CharacterTemporaryStat.RideVehicle)

    sm.warp(141020000, 0) # Middle of Strait : Ice Station 2
    sm.dispose()