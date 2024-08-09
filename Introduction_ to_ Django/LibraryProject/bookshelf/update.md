#the python command
>>>a = Book.objects.get(pk=1)
>>>a.title = "Nineteen Eighty-Four"
>>>a.save()
#expected output
>>>