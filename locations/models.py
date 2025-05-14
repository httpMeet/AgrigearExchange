from django.db import models

# Create your models here.
class state_master(models.Model):
    status_id_choices = (
        ('active', 'active'),
        ('inactive', 'inactive'),
    )
    state_id = models.AutoField(primary_key=True,unique=True)
    state_name = models.CharField(max_length=150,null=False,blank=False,unique=True)

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name_plural = "States and Union Territories"


class district_master(models.Model):
    district_id = models.AutoField(primary_key=True,unique=True)
    district_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    state_name = models.ForeignKey(state_master,to_field='state_name',null=False,blank=False,on_delete=models.PROTECT)
    state_id = models.IntegerField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.state_name:
            state = state_master.objects.filter(state_name=self.state_name).first()
            if state:
                self.state_id = state.state_id
        super(district_master, self).save(*args, **kwargs)

    def __str__(self):
        return self.district_name