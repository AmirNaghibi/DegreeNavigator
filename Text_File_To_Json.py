file_reader = open('Courses_File.txt', 'r')
lines = file_reader.readlines()
a = 0
courseTypes = []
while a < len(lines):
    courseType = {}
    currentType = eval(lines[a])[0]
    courseLevels = []
    while a < len(lines) and eval(lines[a])[0] == currentType:
        courseLevel = {}
        currentLevel = eval(lines[a])[1][0]
        courses = []
        while a < len(lines) and eval(lines[a])[1][0] == currentLevel:
            course = {}
            course["name"] = currentType + ' ' + eval(lines[a])[1]
            courses.append(course)
            a += 1
        courseLevel["name"] = currentLevel + "XX"
        courseLevel["children"] = courses
        courseLevels.append(courseLevel)
    courseType["name"] = currentType
    courseType["children"] = courseLevels
    courseTypes.append(courseType)
allCourses = {}
allCourses["name"] = "Courses"
allCourses["children"] = courseTypes

#This code puts the dictionary in the json file
import json
with open('Courses_File_New.json', 'w') as fp:
    json.dump(allCourses, fp)