class BattlesternError(Exception):
    pass

class OrientationError(BattlesternError):
    pass

class CoordinateError(BattlesternError):
    pass

class PlayerSetupError(BattlesternError):
    pass

class BoardError(BattlesternError):
    pass