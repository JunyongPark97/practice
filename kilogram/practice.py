
class User(models.Model):
  pass


class TimeLog(models.Model):
  user = models.ForeignKey(User, related_name='time_logs')
  timestamp = models.DateTimeField()


# 아주 기본적인 사용법
user = User.objects.get(id=10)
timelogs = TimeLog.objects.filter(user=user)  #1


# exploit ORM 1
user = User.objects.get(id=10)
timelogs = user.time_logs  #2
type(timelogs) == QuerySet

# exploit ORM 2  : join and where
User.objects.filter(time_logs__timestamp__range=('2018-11-01', '2018-11-31'))
print(User.objects.filter(time_logs__timestamp__range=('2018-11-01', '2018-11-31')).query)  #
# select * from user left outer join timelogs on ~ where timelogs.timestamp > ...



log = TimeLog.objects.get()

log.user_id  # int
log.user  # User object # join역할
log.user.name  # string


# django
# 1. models.py 작성
# 2. python manage.py makemigrations
# 3. python manage.py migrate  # -> db.sqlite3에 적용


# sqlite3 db.sqlite3
#