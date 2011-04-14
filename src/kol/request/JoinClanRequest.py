from GenericRequest import GenericRequest
from kol.util import ParseResponseUtils
from kol.manager import PatternManager
from kol.Error import RequestError

class JoinClanRequest(GenericRequest):
    "Join a specific clan by ID#"
    def __init__(self, session, clanID):
        super(JoinClanRequest, self).__init__(session)
        self.url = session.serverURL + 'showclan.php?recruiter=1&whichclan='+ str(clanID) +'&pwd=' + session.pwd + '&whichclan=' + str(clanID) + '&action=joinclan&apply=Apply+to+this+Clan&confirm=on'

    def parseResponse(self):
        joindedClanPattern = PatternManager.getOrCompilePattern('joinedClan')
        match = joindedClanPattern.search(self.responseText)
        self.responseData['success'] = match != None