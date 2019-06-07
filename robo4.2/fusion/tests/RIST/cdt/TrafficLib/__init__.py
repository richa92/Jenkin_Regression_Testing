from keywords import TrafficLibraryKeywords
from robot.version import get_version
__version__ = get_version()


class TrafficLib(
        TrafficLibraryKeywords,
        TrafficLibraryKeywords.VspLibraryKeywords,
        TrafficLibraryKeywords.PingTrafficLibraryKeywords,
        TrafficLibraryKeywords.FpingTrafficLibraryKeywords,
        TrafficLibraryKeywords.IPerfTrafficLibraryKeywords,
        TrafficLibraryKeywords.IOMeterLibraryKeywords,):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        for base in TrafficLib.__bases__:
            base.__init__(self)
