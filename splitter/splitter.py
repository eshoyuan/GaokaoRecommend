def splitter(curriculum):
    requirement1 = curriculum.split('/')
    requirement2 = curriculum.split('、')
    if curriculum == '不限':
        return [], "none"  # 不限
    if len(requirement1) >= len(requirement2):
        requirement = requirement1
        requirement_type = "or"  # n选1
    else:
        requirement = requirement2
        requirement_type = "and"  # 都要选
    return requirement, requirement_type


# test
print("限制科目为{}，选择类型为{}".format(splitter('物、化、生')[0], splitter('物、化、生')[1]))
print("限制科目为{}，选择类型为{}".format(splitter('物/化/生')[0], splitter('物/化/生')[1]))
print("限制科目为{}，选择类型为{}".format(splitter('不限')[0], splitter('不限')[1]))

