# convert inches and pounds to centimeters and kilos
height = 72 # inches
weight = 187 # lbs
h_cm = height * 2.54
w_kilo = weight / 2.2046 
print "My height is %d inches." % height
print "That's %d in centimeters." % h_cm
print "My weight is %d pounds." % weight
print "That's %.2f in kilograms." % (weight / 2.2046)