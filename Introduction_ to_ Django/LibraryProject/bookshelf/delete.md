#the python command
>>> c = Book.objects.get(pk=1)
>>> c.delete()
#expected output
(1, {'byyee.Book': 1})
#confirmation of deletion
>>>Book.objects.all()
#expected output
<QuerySet []>