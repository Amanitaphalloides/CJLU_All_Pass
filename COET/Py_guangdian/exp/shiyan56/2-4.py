def get_student_info(student_id):

    xydm = {
        '01': '经济管理学院',
        '02': '机电学院',
        '03': '生命科学院',
        '04': '外国语学院',
        '05': '理学院',
        '06': '文法学院',
        '08': '计算机学院'
    }


    if len(student_id) != 10:
        return "学号格式错误"

    year = student_id[:4]
    college_code = student_id[4:6]

    college_name = xydm.get(college_code, "未知学院")

    return f"年级{year}，所属学院是{college_name}"

student_id = input("学号")
result = get_student_info(student_id)
print(result)
