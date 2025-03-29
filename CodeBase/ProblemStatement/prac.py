movies = [(1, 'spi'), (2, 'ave'), (3, 'bat')]
ratings = [(1, 101, 3.4), (1, 102, 3.2), (1, 103, 3.1), (2, 101, 3.4), (2, 102, 3.2), (2, 103, 3.1),
           (3, 101, 3.4), (3, 102, 3.2)]

# list of dict - output
for i in range(movies):
    movie_id = movies[i][0]
    rating_li = []
    for j in range(ratings):
        if movie_id == ratings[j][0]:
            rating_li.append(ratings[j])


select s.id, s.name m.marks, avg(marks)
from students s  inner join marks m
on s.id = m.id
where m.marks >= avg(marks)
group by s.id, s.name m.marks