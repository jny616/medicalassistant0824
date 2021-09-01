#models.py
class records(models.Model):
    uid = models.CharField(max_length=50,null=False,default='')                 #user_id
    name = models.CharField(max_length=255,blank=True,null=False)               #LINE名字
    description = models.CharField(max_length=100,blank=True,null=False)        #內容描述
    mdt = models.DateTimeField(auto_now=True)                                   #物件儲存的日期時間

    def __str__(self):
        return self.uid
