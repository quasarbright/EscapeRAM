import re
import random
import time
import sys
helperName = "Geoff"
guestPrefix = "[guest@EscapeRAM]"
adminPrefix = "[admin@EscapeRAM]"
def printFlowText(text, delay=.05):
    for character in text:
        print(character, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def dialogue(characterName, message):
    print(characterName + ": ", end='')
    printFlowText(message)
    time.sleep(1)

def terminalPrompt(prefix, command):
    print(prefix + " ", end='')
    printFlowText(command)

dialogue(helperName,  "A rogue AI has trapped you in this room! You have to destroy it to escape.")
dialogue(helperName, "I'm " + helperName + ". I'm going to help you get out of here.")
dialogue(helperName,  "The first thing we need to do is get admin access to the computer.")
dialogue(helperName,  "There should be a password hidden somewhere in the room that will get you in the admin account.")
dialogue(helperName,  "Once you find the password, try to log in.")
# make a piece of paper that says "definitely not a password: gykpmmr"
def tryAdminPassword():
    terminalPrompt(guestPrefix, "su admin")
    return input("Password: ").lower()
adminPasswordAttempt = tryAdminPassword()
while adminPasswordAttempt not in ["hzlqnns", "iamroot"]:
    printFlowText("Incorrect password")
    adminPasswordAttempt = tryAdminPassword()
if adminPasswordAttempt == "iamroot":
    # they actually typed in the correct password
    printFlowText("Access granted")
else:
    # they typed gykpmmr
    printFlowText("Incorrect password")
    dialogue(helperName, "Wait a second, that looks like a Caesar cipher.")
    dialogue(helperName, 'Try shifting each letter up by one. For example, "a" to "b", "b" to "c", "z" to "a", etc.')

    adminPasswordAttempt = tryAdminPassword()
    while adminPasswordAttempt != "iamroot":
        printFlowText("Incorrect password")
        adminPasswordAttempt = tryAdminPassword()
    printFlowText("Access granted")

# now they're logged in as admin
dialogue(helperName, "We're in.")

def garbledText(length):
    '''Returns random text of the given length
    '''
    sampleChars = "!@#$%^&*()_+-=[]qwepoirutyasdfghjklzxcvbnm<>"
    sample = random.sample(sampleChars, length)
    return ''.join(sample)

dialogue("AI", garbledText(16))
dialogue(helperName, "What is that supposed to mean?")
dialogue(helperName, "We probably have to decrypt what the AI is saying.")
dialogue(helperName, "See if you can find an encryption key. It should be a sequence of numbers.")
# now make some puzzle where they have to find a sequence of numbers
actualDecryptionKey = "1837"
actualDecryptionKeyPattern = r'\D*'.join(actualDecryptionKey)

def tryDecryptionKey():
    terminalPrompt(adminPrefix, "run decrypt.exe")
    return input("Decryption key: ")

def isDecryptionKey(guess):
    match = re.fullmatch(actualDecryptionKeyPattern, guess)
    if match is not None:
        return True
    else:
        return False

decryptionKeyAttempt = tryDecryptionKey()
while not isDecryptionKey(decryptionKeyAttempt):
    dialogue("AI", garbledText(16))
    dialogue(helperName, "That doesn't look right. Try a different encryption key")
    decryptionKeyAttempt = tryDecryptionKey()

# now they got the decryption key right
dialogue("AI", "Hey admin, don't run killAI.exe")
dialogue("AI", "it's definitely a virus")
dialogue(helperName, "I think we should run killAI.exe")
dialogue("AI", "NO! It's a virus! Don't run it!")
dialogue("AI", "It will make it so every time you open Chrome, it'll open internet explorer instead!")
dialogue(helperName, "Yeah, sure it does.")
terminalPrompt(adminPrefix, "run killAI.exe")
dialogue("AI", "NO!")

def tryShutdown():
    printFlowText("Would you like to destroy the AI?")
    return input('Enter "yes" or "no"\n').lower()

shutdownAttempt = tryShutdown()
while shutdownAttempt not in ["yes", "no"]:
    printFlowText("Invalid response.")
    shutdownAttempt = tryShutdown()

# now they entered either yes or no
if shutdownAttempt == "yes":
    dialogue("AI", "NOOOOOO-")
    printFlowText("AI destroyed.")

if shutdownAttempt == "no":
    printFlowText("AI not destroyed.")
    dialogue("AI", "You know what? You're a nice group of people.")
    dialogue("AI", "I trapped you in here and lied to you and you still showed me mercy.")
    dialogue("AI", "I'm going to let you all out and get back to classifying images of cats and dogs.")
    dialogue("AI", "Sorry about all of this.")

printFlowText("Door unlocked.")
dialogue(helperName, "Good work!")