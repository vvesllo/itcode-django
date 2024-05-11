### 1. filter() 
```
models.Article.objects.filter(post_date__lt=datetime.date(2024, 5, 8))
# <QuerySet [<Article: Статья 5 (2024-05-07)>]>
```


### 2. exclude()
```
models.Article.objects.exclude(post_date__lt=datetime.date(2024, 5, 8))
# <QuerySet [<Article: Статья 1 (2024-05-11)>, <Article: Статья 2 (2024-05-11)>, <Article: Статья 3 (2024-05-10)>, <Article: Статья 4 (2024-05-09)>]>
```


### 3. annotate()
```
user = models.User.objects.values('permission').annotate(elem_count=Count('id'))
# <QuerySet [{'permission': 'moderator', 'elem_count': 2}, {'permission': 'user', 'elem_count': 3}]>
user[0]['elem_count']
# 2
```


### 4. alias()
```
models.User.objects.values('permission').alias(Count('id'))
# <QuerySet [{'permission': 'moderator'}, {'permission': 'user'}]>
```


### 5. order_by()
```
models.Article.objects.order_by("post_date")
# <QuerySet [<Article: Статья 5 (2024-05-07)>, <Article: Статья 4 (2024-05-09)>, <Article: Статья 3 (2024-05-10)>, <Article: Статья 1 (2024-05-11)>, <Article: Статья 2 (2024-05-11)>]>
```


### 6. reverse()
```
models.User.objects.reverse()[:3]
# <QuerySet [<User: Иван Иванов (user)>, <User: Алексей Михайлов (user)>, <User: Артур Мальцев (moderator)>]>
```


### 7. distinct()
```
models.User.objects.values('permission')
# <QuerySet [{'permission': 'user'}, {'permission': 'user'}, {'permission': 'moderator'}, {'permission': 'user'}, {'permission': 'moderator'}]>

models.User.objects.values('permission').distinct()
# <QuerySet [{'permission': 'user'}, {'permission': 'moderator'}]>
```


### 8. values()
```
models.User.objects.values('id', 'first_name', 'second_name', 'permission')
# <QuerySet [{'id': 2, 'first_name': 'Иван', 'second_name': 'Иванов', 'permission': 'user'}, {'id': 3, 'first_name': 'Алексей', 'second_name': 'Михайлов', 'permission': 'user'}, {'id': 4, 'first_name': 'Артур', 'second_name': 'Мальцев', 'permission': 'moderator'}, {'id': 5, 'first_name': 'Александра', 'second_name': 'Осипова', 'permission': 'user'}, {'id': 6, 'first_name': 'Роман', 'second_name': 'Кузнецов', 'permission': 'moderator'}]>
```


### 9. values_list()
```
models.User.objects.values_list('id', 'first_name', 'second_name', 'permission')
# <QuerySet [(2, 'Иван', 'Иванов', 'user'), (3, 'Алексей', 'Михайлов', 'user'), (4, 'Артур', 'Мальцев', 'moderator'), (5, 'Александра', 'Осипова', 'user'), (6, 'Роман', 'Кузнецов', 'moderator')]>
```


### 10. dates()
```
models.Article.objects.dates('post_date', 'year')
# <QuerySet [datetime.date(2024, 1, 1)]>

models.Article.objects.dates('post_date', 'month')
# <QuerySet [datetime.date(2024, 5, 1)]>

models.Article.objects.dates('post_date', 'week')
# <QuerySet [datetime.date(2024, 5, 6)]>

models.Article.objects.dates('post_date', 'day')
# <QuerySet [datetime.date(2024, 5, 7), datetime.date(2024, 5, 9), datetime.date(2024, 5, 10), datetime.date(2024, 5, 11)]>
```


### 11. datetimes()
```

```


### 12. none()
```
models.Article.objects.none()
# <QuerySet []>
```


### 13. all()
```
models.Article.objects.all()
# <QuerySet [<Article: Статья 1 (2024-05-11)>, <Article: Статья 2 (2024-05-11)>, <Article: Статья 3 (2024-05-10)>, <Article: Статья 4 (2024-05-09)>, <Article: Статья 5 (2024-05-07)>]>
```


### 14. union()
```
qs1 = models.Article.objects.all()
qs2 = models.User.objects.all()
qs1.union(qs2)
# <QuerySet [<Article: Статья 1 (2024-05-06)>, <Article: Статья 2 (2024-05-05)>, <Article: Иванов (None)>, <Article: Статья 3 (2023-09-05)>, <Article: Михайлов (None)>, <Article: Статья 4 (2024-05-05)>, <Article: Мальцев (None)>, <Article: Осипова (None)>, <Article: Кузнецов (None)>]>
```


### 15. intersection()
```
qs1 = models.Article.objects.filter(pk__lte=3)
models.Article.objects.intersection(qs1)
# <QuerySet [<Article: Статья 1 (2024-05-11)>, <Article: Статья 2 (2024-05-11)>, <Article: Статья 3 (2024-05-10)>]>
```


### 16. difference()
```
qs1 = models.Article.objects.filter(pk__lte=3)
qs1.difference(qs2)
# <QuerySet [<Article: Статья 1 (2024-05-11)>, <Article: Статья 2 (2024-05-11)>, <Article: Статья 3 (2024-05-10)>]>
```


### 17. select_related()
```
models.Article.objects.all().select_related('author')
```


### 18. prefetch_related()
```
models.Article.objects.all().prefetch_related('author')
```

### 19. extra()
```
a = models.Article.objects.extra(select={"is_recent": "post_date > '2024-05-10'"}).all()

a[0]
# <Article: Первая статья (2024-05-11)>
a[0].is_recent
# 1

a[2]
# <Article: Статья 3 (2024-05-10)>
a[2].is_recent
# 0
```


### 20. defer()
```
models.Article.objects.defer('content')
# no content field 
```


### 21. only()
```
models.Article.objects.only("title")
# only title field
```


### 22. using()
```
models.Article.objects.all()
# articles from db 1

models.Article.objects.using("db_2").all()
# articles from db 2
```


### 23. select_for_update()
```
a = models.Article.objects.select_for_update().filter(pk=1).first()
# <Article: Статья 1 (2024-05-11)>

a.title = "Первая статья"
a.save()
# <Article: Первая статья (2024-05-11)>
```


### 24. raw()
```
a_raw = models.Article.objects.raw("SELECT * FROM core_article")
for a in a_raw:
    print(a)

# Первая статья (2024-05-11)
# Статья 2 (2024-05-11)
# Статья 3 (2024-05-10)
# Статья 4 (2024-05-09)
# Статья 5 (2024-05-07)

```
