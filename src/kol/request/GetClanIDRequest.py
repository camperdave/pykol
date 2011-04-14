from GenericRequest import GenericRequest
from kol.util import ParseResponseUtils
from kol.manager import PatternManager
from kol.Error import RequestError

class GetClanIDRequest(GenericRequest):
    "Get a given Player's ClanID"
    def __init__(self, session, playerID):
        super(GetClanIDRequest, self).__init__(session)
        self.url = session.serverURL + 'showplayer.php?who=' + str(playerID)

    def parseResponse(self):
        clanIDPattern = PatternManager.getOrCompilePattern('clanID')
        match = clanIDPattern.search(self.responseText)
        if match:
            self.responseData["clanID"] = int(match.group(1))
        else:
            raise RequestError("Wasn't able to read a clanID for that player")