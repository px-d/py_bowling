import re


def eval(input) -> float:
    """
    Given an Input String of the Format `--|--|--|--|--|--|--|--|--|--||` evaluate the score of given String and if it
    conforms to our formatting (in which variations such as `35|2/|X|71|--|--|--|--|--|--|` are also allowed)

    >>> eval("--|--|--|--|--|--|--|--|--|--||") #Correct Empty Input
    0.0

    >>> eval("--|--|---|--|--|--|--|--|--|--||") #Incorrect Input (3 hyphons)
    -1.0

    >>> eval("--|--|--|--|--|--|--|--|--|--|") #Only one pipe in the end
    -1.0

    # Two strikes in one frame impossible
    >>> eval("XX|--|--|--|--|--|--|--|--|--||")
    -1.0

    >>> eval("101|--|--|--|--|--|--|--|--|--||") #Three throws in one frame
    -1.0

    >>> eval("--||--|--|--|--|--|--|--|--|--||") #Two Pipes before the end
    -1.0

    >>> eval("--|--|--|--|--|--|--|--|--|--|--||") #too many frames
    -1.0

    >>> eval("/-|--|--|--|--|--|--|--|--|--||") #spare on 0 of frame impossible
    -1.0

    # Sum of 10 is not possible > spare
    >>> eval("--|55|--|--|--|--|--|--|--|--||")
    -1.0

    >>> eval("--|75|--|--|--|--|--|--|--|--||") #Sum greater 10 > impossible
    -1.0

    >>> eval("1-|-5|12|--|9-|2-|--|3-|--|16||") #Normal Game
    30.0

    >>> eval("-/|--|--|--|--|--|--|--|--|--||") #Spare
    10.0

    >>> eval("X|--|--|--|--|--|--|--|--|--||") #Strike
    10.0

    >>> eval("-/|22|--|--|--|--|--|--|--|--||") #Spare +4
    16.0

    >>> eval("X|22|-2|--|--|--|--|--|--|--||") #Strike + score
    20.0

    >>> eval("X|X|-2|--|--|--|--|--|--|--||") #Two Strikes
    34.0

    >>> eval("--|--|--|--|--|--|--|--|--|5/||7") #Bonus Throw
    24.0

    # >>> eval("3/|4/|--|--|--|--|--|--|--|--||")
    # 24.0

    >>> eval("--|--|--|--|--|--|--|--|--|X||72")
    28.0

    >>> eval("--|--|--|--|--|--|--|--|--|X||XX")
    50.0

    >>> eval("--|--|--|--|--|--|--|--|--|X||X7")
    44.0

    >>> eval("--|--|--|--|--|--|--|--|--|X||7/")
    30.0

    >>> eval("--|--|--|--|--|--|--|--|--|--||34")
    -1.0

    >>> eval("--|--|--|--|--|--|--|--|--|3/||34")
    -1.0

    >>> eval("--|--|--|--|--|--|--|--|--|X||3")
    -1.0
    """
    
    if not re.search("^([1-9-]{2}\\||[1-9-]/\\||X\\|){10}\\|([1-9-/X]{1,2})?", input):
        return -1.0

    frames = convertGame(input)

    score = 0.0
    lastHitSpare = False
    lastFrameStrike = False

    broke = False

    for idx, frame in enumerate(frames):
        hits = list(frame)
        frame_score = 0.0
        if isInvalidLastFrame(idx, frame, lastFrameStrike, lastHitSpare):
            return -1.0

        for hit in hits:
            if re.search("[1-9]", hit) or hit == "-":
                points = safe_cast_to_int(hit)
                frame_score += points
                if frame_score >= 10.0:
                    return -1.0
                if lastHitSpare:
                    score += points
                    lastHitSpare = False

            elif hit == "/":
                frame_score = 10.0
                lastHitSpare = True

            elif hit == "X":
                if lastFrameStrike or lastHitSpare:
                    score += 10.0
                score += 10.0
                lastFrameStrike = True
                if not isLastFrame(frames, idx):
                    broke = True

        if broke == False and lastFrameStrike:
            frame_score = frame_score * 2
            lastFrameStrike = False

        score += frame_score
        broke = False
    return score


def safe_cast_to_int(val):
    """cast input safely to either a number or if its `-` to `0.0`"""
    if val.isdigit():
        return float(val)
    else:
        return 0.0


def isInvalidLastFrame(current_index, frame, strike, spare):
    if current_index == 10:
        if frame == "":
            return False
        if not strike and not spare or len(list(frame)) != 2 and strike or len(list(frame)) != 1 and spare:
            return True
    return False


def isLastFrame(frames, index):
    if index == len(frames) - 1:
        return True
    else:
        return False


def convertGame(game):
    x = game.replace('||', '+')
    a = x.split('|')
    b = a[len(a)-1].split('+')
    a[len(a)-1] = b[0]
    if len(b) > 1:
        a.append(b[1])
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()