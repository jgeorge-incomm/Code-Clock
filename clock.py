import sys, os, time, datetime

def decimalTime(date):
    decimalSecondsPerHour = 8640
    decimalSecondsPerMinute = 86.4
    decimalSecondsPerSecond = 0.864

    decimalHour = date.hour * decimalSecondsPerHour
    decimalMinute = date.minute * decimalSecondsPerMinute
    decimalSecond = date.second * decimalSecondsPerSecond
    decimal = decimalHour + decimalMinute + decimalSecond

    print decimalHour
    print decimalMinute
    print decimalSecond
    
    return decimal

def sleepTime(time):
    sleep = 0.864

    remainder = (time % 1)
    if(remainder > 0.1):
        sleep = remainder

    return remainder

def renderHours(hours):
    print bin(int(hours))


def renderSeconds(seconds):
    print bin(int(seconds))

def renderBinary(value):
    binaryValue = bin(int(value))
    stringValue = str(binaryValue)[2:]

    stringValue = stringValue.replace('0', ' _')
    stringValue = stringValue.replace('1', ' =')

    print stringValue

def renderTime(time):
    # clear_console = 'clear' if os.name == 'posix' else 'CLS'
    # os.system(clear_console)

    hours = round(time / 10000)
    minutes = round((time - (hours * 10000)) / 100)
    seconds = round(time - (hours * 10000) - (minutes * 100))
    print "hours: " + str(hours)
    print "minutes: " + str(minutes)
    print "seconds: " + str(seconds)

    renderBinary(hours)
    renderBinary(minutes)
    renderBinary(seconds)
    print round(time)

    # sys.stdout.write(outstr)
    sys.stdout.flush()

def runLoop():

    while True:

        # START: debug remove me 
        clear_console = 'clear' if os.name == 'posix' else 'CLS'
        os.system(clear_console)
        # END: debug remove me 

        date = datetime.datetime.now()
        decimal = decimalTime(date)

        renderTime(decimal)

        sleep = sleepTime(decimal)
        time.sleep(sleep)

def animgif_to_ASCII_animation(animated_gif_path):
    chars = ('/', '-', '\\', '|')
    clear_console = 'clear' if os.name == 'posix' else 'CLS'

    # Step through forever, frame by frame
    while True:
        for index in range(0,len(chars)):

            # Built up the string, by translating luminance values to characters
            outstr = ''
            outstr += 'Doing some important work: '
            outstr += chars[index]

            outstr += '\r\n'
            outstr += 'Doing some important work: '
            outstr += chars[(index + 1) % len(chars)]

            outstr += '\r\n'
            outstr += 'Doing some important work: '
            outstr += chars[(index + 2) % len(chars)]

            outstr += '\r\n'
            outstr += 'Doing some important work: '
            outstr += chars[(index + 4) % len(chars)]

            outstr += '\r\n'

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
            time.sleep(0.1)

# run the animation based on some animated gif
runLoop()