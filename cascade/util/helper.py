import io


def getSignedNumber(number, bitLength):
    mask = (2 ** bitLength) - 1
    if number & (1 << (bitLength - 1)):
        return number | ~mask
    else:
        return number & mask


def unsigned_to_signed(arr):
    temp = []
    for i in arr:
        temp.append(getSignedNumber(i, 8))

    return temp


def img_to_cascade(image):
    with open(image, "rb") as f:
        arr = f.read()
    return unsigned_to_signed(arr)