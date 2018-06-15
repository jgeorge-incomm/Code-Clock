import sys, os, time, datetime

def decimalTime(date):
    decimalSecondsPerSecond = 1.157407407407407

    secondsSinceMidnight = (date - date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
    decimalSecondsSinceMidnight = secondsSinceMidnight * 1.157407407407407
    print "secondsSinceMidnight: " + str(secondsSinceMidnight)
    print "decimalSecondsSinceMidnight: " + str(decimalSecondsSinceMidnight)

    decimalHour = int(decimalSecondsSinceMidnight / 10000)
    decimalSecondsRemainder = decimalSecondsSinceMidnight - (decimalHour * 10000)

    print "decimalSecondsRemainder(minutes): " + str(decimalSecondsRemainder)
    decimalMinute = int(decimalSecondsRemainder / 100)
    decimalSecond = int(round(decimalSecondsRemainder - (decimalMinute * 100)))

    decimal = {
        'hour': decimalHour,
        'minute': decimalMinute,
        'second': decimalSecond 
    }

    print "date: " + str(date)
    print "decimalHour: " + str(decimalHour)
    print "decimalMinute: " + str(decimalMinute)
    print "decimalSecond: " + str(decimalSecond)
    print "decimal: " + str(decimal)
    
    return decimal

def sleepTime(time):
    sleep = 0.864
    return sleep

def renderHours(hours):
    print bin(int(hours))


def renderSeconds(seconds):
    print bin(int(seconds))

def renderBinary(value):
    value = abs(value)
    binaryValue = bin(int(value))
    stringValue = str(binaryValue)[2:]

    stringValue = stringValue.replace('0', ' _')
    stringValue = stringValue.replace('1', ' =')
    stringValue += '\r\n'

    sys.stdout.write(stringValue)

def renderTime(time):


    # START: debug remove me 
    # clear_console = 'clear' if os.name == 'posix' else 'CLS'
    # os.system(clear_console)
    # END: debug remove me 

    renderBinary(time['hour'])
    renderBinary(time['minute'])
    renderBinary(time['second'])

    sys.stdout.flush()

def runLoop():

    while True:

        clear_console = 'clear' if os.name == 'posix' else 'CLS'
        os.system(clear_console)

        date = datetime.datetime.now()
        decimal = decimalTime(date)

        renderTime(decimal)

        sleep = sleepTime(decimal)
        time.sleep(sleep)

runLoop()