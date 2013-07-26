mport pymongo

def remove_lowest_homework():
    conn = pymongo.Connection('localhost', 27017)
    r = conn.school.students
    curr = r.find({'scores.type':'homework'})
    for doc in curr:
        other_scores = [score for  score in doc['scores'] if score['type'] != 'homework']
        homework_scores = [score for  score in doc['scores'] if score['type'] == 'homework']
        homework_scores = sorted(homework_scores)[1:]
        new_list = other_scores + homework_scores
        #print new_list
        r.update({'_id': doc['_id']}, {'$set': {'scores': new_list}})

if __name__ == "__main__":
    remove_lowest_homework()
