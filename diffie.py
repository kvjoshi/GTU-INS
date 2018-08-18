P = int(input("Please enter the shared P : "))
G = int(input("Please enter the shared Base G : "))

X = int(input("Please enter Sender's secret key : "))
R1 = (G ** X) % P
print("Sender's Sends Over Public Chanel: ", R1)

Y = int(input("Please enter Receiver's key : "))
R2 = (G ** Y) % P
print("Receiver's Sends Over Public Chanel: ", R2)

print("Privately Calculated Shared Secret:")

K1 = (R2 ** X) % P
print("Sender's Shared Secret: ", K1)

K2 = (R1 ** Y) % P
print("Receiver's Shared Secret: ", K2)

K = (G ** (X * Y)) % P
print("Verify the Shared Secret:", K)
