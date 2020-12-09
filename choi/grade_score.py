user_input = raw_input()

total = 0
avg_score =0 

score_list = [int(i) for i in user_input.split(" ")]
for i in score_list:
	total += float(i)
	
avg_score = round(total/len(score_list),2)
	
if avg_score >= 90:
	grade = 'A'
elif avg_score >= 80:
	grade = 'B'
elif avg_score >= 70:
	grade = 'C'
elif avg_score >= 60: 
	grade = 'D'
else:
	grade = 'F'
	
print ("%0.2f %s" % (avg_score, grade))