class Udacian:
    def __init__(self,Udacian_name,Udacian_city,Udacian_enrollment,Udacian_nanodegree,Udacian_status):
        self.name=Udacian_name
        self.city=Udacian_city
        self.enrollment=Udacian_enrollment
        self.nanodegree=Udacian_nanodegree
        self.status=Udacian_status
		
    def Print(self):
        return "name:"+self.name+"  city:"+self.city+"  enrollment:"+self.enrollment+"  nanodegree:" +self.nanodegree+ "  status:"+self.status
