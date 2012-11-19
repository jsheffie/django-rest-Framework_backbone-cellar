from django.db import models

class Wine( models.Model ):
    name        = models.CharField( max_length=45 )
    year        = models.CharField( max_length=45, blank=True, null=True  )
    grapes      = models.CharField( max_length=45, blank=True, null=True  )
    country     = models.CharField( max_length=45, blank=True, null=True  )
    region      = models.CharField( max_length=45, blank=True, null=True  )
    description = models.TextField( blank=True, null=True )
    picture     = models.CharField( max_length=256, blank=True, null=True  )

    class Meta:
        db_table='wine'
        
    def __unicode__( self ):
        return self.name
    