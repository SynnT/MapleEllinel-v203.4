# 105200310 (+ other RA bosses)
def init():
    sm.sendAskYesNo("Would you like to leave?")

def action(response, answer):
    if response == 1:
        if sm.getParty() is None:
            sm.warpInstanceOut(350060000) # Entrance Core
        else:
            sm.warpPartyOut(350060000) # Entrace Core
    sm.dispose()