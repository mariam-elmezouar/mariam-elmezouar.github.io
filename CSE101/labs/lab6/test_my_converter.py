from my_converter import dec2bin_comp, BinComp2Dec

# Test cases for dec2bin_comp

print(dec2bin_comp(-129))  # Should return an error
print(dec2bin_comp(-128))  # Should print 10000000
print(dec2bin_comp(-1))    # Should print 11111111
print(dec2bin_comp(0))     # Should print 00000000
print(dec2bin_comp(127))   # Should print 01111111
print(dec2bin_comp(128))   # Should return an error

# Test cases for BinComp2Dec
print(BinComp2Dec('00000001'))  # Should return 1
print(BinComp2Dec('11111111'))  # Should return -1
print(BinComp2Dec('01111111'))  # Should return 127
print(BinComp2Dec('10000000'))  # Should return -128
print(BinComp2Dec('10000001'))  # Should return -127
