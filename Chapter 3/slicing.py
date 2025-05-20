name = "Siddharth"

shortName = name[0:3] # Character at index 0, 1, 2
print(shortName)

print(name[-7:-4])  # Character at index -7, -6, -5  <- Negative Slicing
print(name[2:5])    # Same as name[-7: -4]
print(name[7:4])    # Empty string, because 7 > 4
print(name[2:])     # Character at index 2 to end
print(name[:5])     # Character at index 0 to 4
print(name[1:8:2])  # From 1 to 7 with 2 steps skipping