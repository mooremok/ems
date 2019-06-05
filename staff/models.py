from django.db import models

# Create your models here.



class Department(models.Model):
    name = models.CharField('部门', max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '部门列表'

class Position(models.Model):
    name = models.CharField('职位', max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = verbose_name_plural = '职位列表'

class Area(models.Model):
    city = models.CharField('地区', max_length=20)
    #自关联的字段外键指向自己，用self
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='上一级行政区', related_name='subs')

    def __str__(self):
        return self.city
    
    class Meta:
        verbose_name = verbose_name_plural ='行政区域'

class Employee(models.Model):

    SEX_ITEMS = [
        (0, '男'),
        (1, '女'),
    ]

    STATUS_ITEMS = [
        (0, '申请'),
        (1, '通过'),
        (2, '拒绝'),
    ]

    ENTRY_ITEMS = [
        (0, '试用期'),
        (1, '转正'),
        (2, '离职'),
    ]

    name = models.CharField('姓名', max_length=20)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='部门', related_name='department')
    sex = models.IntegerField('性别', choices=SEX_ITEMS)
    birthday = models.DateField('生日')
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING, verbose_name='职位', related_name='position')
    hometown = models.ForeignKey(Area, on_delete=models.DO_NOTHING, verbose_name='籍贯', related_name='hometown')
    phone = models.IntegerField('手机', max_length=11)
    status = models.IntegerField('申请状态', choices=STATUS_ITEMS)
    entry = models.IntegerField('在职状态', choices=ENTRY_ITEMS)

    class Meta:
        verbose_name = verbose_name_plural = '员工信息'
    
    def __str__(self):
        return self.name
    
