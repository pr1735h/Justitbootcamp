from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
from statistics import mean

def main():
    client = MongoClient("mongodb+srv://pr1735h:vPvcoOjrKHF6r7Em@cluster0.zu2wfsw.mongodb.net/")
    db_name = "c9w4"
    mongo_db = client[db_name]
    course = "course"
    lesson = "lesson"
    members = "members"
    table_course = mongo_db[course]
    table_lesson = mongo_db[lesson]
    table_members = mongo_db[members]

    # Use the SQL AND, OR, and NOT Operators in your query
    query = {
        "$and": [
            {"courseID": {"$lt": 5}},
            {"Instructor": {"$in": ["Amelia"]}}
        ]
    }
    result = table_course.find(query)
    pprint(list(result))

    # Where courseID is equals to a number above 5 and the lesson time is in the morning or afternoon.
    query2 = {
        "$and": [
            {"courseID": {"$gt": 5}},
            {"lessonTime": {"$in": ["Morning", "Afternoon"]}}
        ]
    }
    result2 = table_course.find(query2)
    pprint(list(result2))

    # Order by the above results by startDate in “course” table
    result3 = table_course.find().sort("startDate")
    pprint(list(result3))

    # Order by MemberID in “members” table
    result4 = table_members.find().sort("MemberID")
    pprint(list(result4))

    # UPDATE the following:
    # Members table, change the addresses of any three members.
    document_id1 = ObjectId('65a9098ef775bbb6d3dfca82')
    m1 = {"_id": document_id1}
    document_id2 = ObjectId('65a9098ef775bbb6d3dfca83')
    m2 = {"_id": document_id2}
    document_id3 = ObjectId('65a9098ef775bbb6d3dfca84')
    m3 = {"_id": document_id3}

    query3 = {"_id": {"$in": [m1, m2, m3]}}
    update = {"$set": {"Address": "123 New Address"}}
    table_members.update_many(query3, update)

    # Course table, change the startDate and lesson time for three of the sessions.
    document_id4 = ObjectId('65a90974f775bbb6d3dfca1c')
    m4 = {"_id": document_id4}
    document_id5 = ObjectId('65a90974f775bbb6d3dfca1e')  # Replace with a valid ObjectId
    m5 = {"_id": document_id5}
    document_id6 = ObjectId('65a90974f775bbb6d3dfca1e')
    m6 = {"_id": document_id6}

    query4 = {"_id": {"$in": [m4, m5, m6]}}
    update2 = {"$set": {"startDate": "2024-02-15", "LessonTime": "15:00"}}
    table_lesson.update_many(query4, update2)

    # Smallest and Largest LessonID
    min_lesson_id = table_lesson.find_one({}, sort=[("_id", 1)])["_id"]
    max_lesson_id = table_lesson.find_one({}, sort=[("_id", -1)])["_id"]
    print(f"Smallest _id (LessonID): {min_lesson_id}, Largest _id (LessonID): {max_lesson_id}")

    # Smallest and Largest membersID
    min_members_id = table_members.find_one({}, sort=[("_id", 1)])["_id"]
    max_members_id = table_members.find_one({}, sort=[("_id", -1)])["_id"]
    print(f"Smallest _id (membersID): {min_members_id}, Largest _id (membersID): {max_members_id}")

    # Total number of members
    total_members = table_members.count_documents({})
    print(f"Total members: {total_members}")

    # Average CourseID from all lessons
    cursor = table_lesson.find({}, {"CourseID": 1, "_id": 0})
    course_ids = [doc["CourseID"] for doc in cursor]
    average_course_id = mean(course_ids)
    print(f"Average CourseID: {average_course_id}")

    # WILDCARD queries (like operator)
    # Find all the people from the “members” table whose last name starts with A.
    query_a_start = {"lastName": {"$regex": '^A'}}
    result_a_start = table_members.find(query_a_start)
    # Find all the people from the “members” table whose last name ends with A.
    query_a_end = {"lastName": {"$regex": 'A$'}}
    result_a_end = table_members.find(query_a_end)
    # Find all the people from the “members” table that have "ab" in any position in the last name.
    query_ab = {"lastName": {"$regex": 'ab'}}
    result_ab = table_members.find(query_ab)
    # Find all the people from the “members” table that that have "b" in the second position in their first name.
    query_b_second = {"firstName": {"$regex": '^.[bB].'}}
    result_b_second = table_members.find(query_b_second)
    # Find all the people from the “members” table whose last name starts with "a" and are at least 3 characters in length:
    query_a_long = {"lastName": {"$regex": '^a.{2,}'}}
    result_a_long = table_members.find(query_a_long)
    # Find all the people from the “members” table whose last name starts with "a" and ends with "y"
    query_a_y = {"lastName": {"$regex": '^a.*y$'}}
    result_a_y = table_members.find(query_a_y)
    # Find all the people from the “members” table whose last name does not starts with "a" and ends with "y"
    query_not_a_y = {"lastName": {"$regex": '^[^a].*y$'}}
    result_not_a_y = table_members.find(query_not_a_y)

    # What do you understand by LEFT and RIGHT join? Explain with an example.
    # Joins are used two combine rows from multiple tables with a related column from all tables used.
    # This is useful when multiple tables have data for one entity like a customer and you want to compare, analyse or export specific fields.
    # LEFT and RIGHT JOIN take specified columns from one table and combine them with the specified columns from other tables.
    # If there are no matches the result will be displayed as "NULL".
    course1 = table_course
    members2 = table_members

    # Perform a left join
    pipeline = [
        {
            "$lookup": {
                "from": "course",
                "localField": "_id",
                "foreignField": "Firstname",
                "as": "customerInfo"
            }
        }
    ]

    result7 = list(members2.aggregate(pipeline))
    pprint(result7)

    # Perform a right join
    pipeline = [
        {
            "$lookup": {
                "from": "members",
                "localField": "_id",
                "foreignField": "Instructor",
                "as": "orderInfo"
            }
        }
    ]

    result8 = list(course1.aggregate(pipeline))
    pprint(result8)


if __name__ == "__main__":
    main()

# all_docs_cursor = table_course.find()
# all_docs_list = list(all_docs_cursor)
# pprint(all_docs_list)