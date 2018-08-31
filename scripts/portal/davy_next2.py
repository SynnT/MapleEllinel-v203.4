# 925100200 - Third Map of the Lord Pirate PQ
def init():
    if sm.getReactorQuantity() > 8 or sm.hasMobsInField(): # due to invisible reactor hidden on the map
        sm.chat("The portal is not opened.")
    else:
        sm.warpPartyIn(sm.getFieldID() + 100)
    sm.dispose()
