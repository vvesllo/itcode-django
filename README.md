### 1. filter() 
```
models.Article.objects.filter(post_date=datetime.date(2024, 5, 5))
# <QuerySet [<Article: Статья 2 (2024-05-05)>, <Article: Статья 4 (2024-05-05)>]>
```


### 2. exclude()
```
models.Article.objects.exclude(post_date=datetime.date(2024, 5, 5))
# <QuerySet [<Article: Статья 1 (2024-05-06)>, <Article: Статья 3 (2023-09-05)>]>
```


### 3. annotate()
```
models.User.objects.values('permission').annotate(Count('id'))
# <QuerySet [{'permission': 'moderator', 'id__count': 2}, {'permission': 'user', 'id__count': 3}]>
```


### 4. alias()
```
models.User.objects.values('permission').alias(Count('id'))
<QuerySet [{'permission': 'moderator'}, {'permission': 'user'}]>
```


### 5. order_by()
```
models.Article.objects.order_by("post_date")
# <QuerySet [<Article: Статья 3 (2023-09-05)>, <Article: Статья 2 (2024-05-05)>, <Article: Статья 4 (2024-05-05)>, <Article: Статья 1 (2024-05-06)>]>
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
# <QuerySet [datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)]>

models.Article.objects.dates('post_date', 'month')
# <QuerySet [datetime.date(2023, 9, 1), datetime.date(2024, 5, 1)]>

models.Article.objects.dates('post_date', 'week')
# <QuerySet [datetime.date(2023, 9, 4), datetime.date(2024, 4, 29), datetime.date(2024, 5, 6)]>

models.Article.objects.dates('post_date', 'day')
# <QuerySet [datetime.date(2023, 9, 5), datetime.date(2024, 5, 5), datetime.date(2024, 5, 6)]>
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
# <QuerySet [<Article: Статья 1 (2024-05-06)>, <Article: Статья 2 (2024-05-05)>, <Article: Статья 3 (2023-09-05)>, <Article: Статья 4 (2024-05-05)>]>
```


### 14. union()
```

```


### 15. intersection()
```

```


### 16. difference()
```

```


### 17. select_related()
```

```


### 18. prefetch_related()
```

```


### 19. extra()
```

```


### 20. defer()
```

```


### 21. only()
```

```


### 22. using()
```

```


### 23. select_for_update()
```

```


### 24. raw()
```

```
