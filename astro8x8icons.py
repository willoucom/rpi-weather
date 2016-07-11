#===============================================================================
# atro8x8icons.py
#
# Dictionary of LED 8x8 matrix icons.
#
#
# 2016-07-10
# Wilfried JEANNIARD
#==============================================================================

X = [255, 255, 255]  # White
R = [255, 0, 0]  # RED
O = [0, 0, 0]  # NOT LIGHTED

LED8x8ICONS = {
#---------------------------------------------------------
# misc
#---------------------------------------------------------
'UNKNOWN' : [
O, O, O, R, R, O, O, O,
O, O, R, O, O, R, O, O,
O, O, O, O, O, R, O, O,
O, O, O, O, R, O, O, O,
O, O, O, R, O, O, O, O,
O, O, O, R, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, R, O, O, O, O
],
#---------------------------------------------------------
# weather
#---------------------------------------------------------
'SUNNY' : [
X, O, O, X, O, O, O, X,
O, X, O, O, O, O, X, O,
O, O, O, X, X, O, O, O,
O, O, X, X, X, X, O, X,
X, O, X, X, X, X, O, O,
O, O, O, X, X, O, O, O,
O, X, O, O, O, O, X, O,
X, O, O, O, X, O, O, X
] ,
'RAIN' : [
O, X, O, X, O, X, O, X,
X, O, X, O, X, O, X, O,
O, X, O, X, O, X, O, X,
X, O, X, O, X, O, X, O,
O, X, O, X, O, X, O, X,
X, O, X, O, X, O, X, O,
O, X, O, X, O, X, O, X,
X, O, X, O, X, O, X, O
] ,
'CLOUD' : [
O, X, X, X, O, O, O, O,
X, O, O, O, X, X, X, O,
X, O, O, O, X, O, O, X,
X, O, O, O, O, O, O, X,
X, O, O, O, O, O, O, X,
O, X, X, X, X, X, X, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
] ,
'SHOWERS' : [
O, X, X, X, O, O, O, O,
X, O, O, O, X, X, X, O,
X, O, O, O, X, O, O, X,
X, O, O, O, O, O, O, X,
X, O, O, O, O, O, O, X,
O, X, X, X, X, X, X, O,
O, X, O, X, O, X, O, O,
X, O, X, O, X, O, O, O
] ,
'SNOW' : [
X, O, X, O, O, X, O, X,
O, X, O, O, O, O, X, O,
X, O, X, O, O, X, O, X,
O, O, O, X, X, O, O, O,
O, O, O, X, X, O, O, O,
X, O, X, O, O, X, O, X,
O, X, O, O, O, O, X, O,
X, O, X, O, O, X, O, X
] ,
'STORM' : [
O, X, X, X, O, O, O, O,
X, O, O, O, X, X, X, O,
X, O, O, O, X, O, O, X,
X, O, O, O, O, O, O, X,
O, X, X, X, X, X, X, O,
O, O, O, X, O, O, O, O,
O, O, X, O, O, O, O, O,
O, X, O, X, O, O, O, O
] ,
}
