chessboard = {
    "1a": "bking",
    "2a": "bqueen",
    "3a": "brook",
    "4a": "brook",
    "5a": "bknight",
    "6a": "bknight",
    "7a": "bbishop",
    "8a": "bbishop",
    "1b": "bpawn",
    "2b": "bpawn",
    "3b": "bpawn",
    "4b": "bpawn",
    "5b": "bpawn",
    "6b": "bpawn",
    "7b": "bpawn",
    "8b": "bpawn",
    "1c": "wking",
    "2c": "wqueen",
    "3c": "wrook",
    "4c": "wrook",
    "5c": "wbishop",
    "6c": "wbishop",
    "7c": "wknight",
    "8c": "wknight",
    "1e": "wpawn",
    "2e": "wpawn",
    "3e": "wpawn",
    "4e": "wpawn",
    "5e": "wpawn",
    "6e": "wpawn",
    "7e": "wpawn",
    "8e": "wpawn",
    "1f": "",
    "2f": "",
    "3f": "",
    "4f": "",
    "5f": "",
    "6f": "",
    "7f": "",
    "8f": "",
    "1g": "",
    "2g": "",
    "3g": "",
    "4g": "",
    "5g": "",
    "6g": "",
    "7g": "",
    "8g": "",
    "1h": "",
    "2h": "",
    "3h": "",
    "4h": "",
    "5h": "",
    "6h": "",
    "7h": "",
    "8h": "",
}


def hasOnlyOneKing(chessboard):
    if "wking" & "bking" in chessboard.values():
        return True
    return False


def hasOnly32keys(chessboard):
    if len(chessboard) == 32:
        return True
    return False


def isOnValidSpace(chessboard):
    allValidPositions = []
    for j in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        for i in range(1, 9):
            allValidPositions.append(str(i) + j)
    for key in chessboard.keys():
        if key in allValidPositions:
            return True
        return False


def isValidName(chessboard):
    allValidNames = []
    for i in ["w", "b"]:
        for j in ["pawn", "bishop", "rook", "knight", "queen", "king"]:
            allValidNames.append(i + j)
    for values in chessboard.values():
        if values in allValidNames:
            return True
        return False


def isChessBoardValid(chessboard):
    hasOnlyOneKing(chessboard)
    hasOnly32keys(chessboard)


isValidName(chessboard)
