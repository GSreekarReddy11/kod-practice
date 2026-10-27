class LowPercentageError(Exception):
    pass
try:
    percentage=45
    if percentage<40:
        raise LowPercentageError("You need to gain good skills to get more than 40 percentage")
    print("Eligible")
