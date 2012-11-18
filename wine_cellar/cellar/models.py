from django.db import models

#| id          | int(11)      | NO   | PRI | NULL    | auto_increment |
#| name        | varchar(45)  | YES  |     | NULL    |                |
#| year        | varchar(45)  | YES  |     | NULL    |                |
#| grapes      | varchar(45)  | YES  |     | NULL    |                |
#| country     | varchar(45)  | YES  |     | NULL    |                |
#| region      | varchar(45)  | YES  |     | NULL    |                |
#| description | blob         | YES  |     | NULL    |                |
#| picture     | varchar(256) | YES  |     | NULL    |                |



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
    