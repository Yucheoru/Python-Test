def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
        
gender = "남자"
height = 179
weight = round(std_weight(height / 100, gender), 2) #소수점으로 변환

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))
