from Tribler.Test.test_as_server import AbstractServer
from Tribler.dispersy.dispersy import Dispersy
from Tribler.dispersy.endpoint import ManualEnpoint
from Tribler.dispersy.member import DummyMember
from Tribler.dispersy.util import blocking_call_on_reactor_thread


class AbstractTestCommunity(AbstractServer):

    # We have to initialize Dispersy and the tunnel community on the reactor thread
    @blocking_call_on_reactor_thread
    def setUp(self):
        super(AbstractTestCommunity, self).setUp()
        self.dispersy = Dispersy(ManualEnpoint(0), self.getStateDir())
        self.dispersy._database.open()
        self.master_member = DummyMember(self.dispersy, 1, "a" * 20)
        self.member = self.dispersy.get_new_member(u"curve25519")
