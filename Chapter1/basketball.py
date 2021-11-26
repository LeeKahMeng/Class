points_str = input ("Enter the lead in points")
point_remaining_int = int (points_str)

leadpoints_float = float (point_remaining_int -3 )

hastheball_str = input ("Does the leading team has the ball (Yes/No) :")

if hastheball_str == 'Yes':
	leadpoints_float = leadpoints_float + 0.5
else :
	leadpoints_float = leadpoints_float - 0.5
	
if leadpoints_float < 0 :
	leadpoints_float = 0
	
leadpoints_float = leadpoints_float **2

secondsremain_int = int (input ("Enter the number of seconds remaining :"))

if leadpoints_float > secondsremain_int :
	print ("The lead is safe")
else :
	print ("The lead is not safe")
#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
