from App.Http.Controllers.Controller import Controller
from App.Http.Models.User import User

class Home(Controller):
    # def __init__(self):
        # self.User = User

        # self.db = Controller.db
        # self.db = db()
    # def __del__(self):
        # self.db.close()


    def index(self):
        # users = self.db.query(User).all()
        users = User().table().filter(User.id == 1).all()
        return users
        # return {'Hello':'world'}
    
    # def store(self):
    #     user = User(
    #         id = '2',
    #         name = 'Anas',
    #         email= 'Anas@hts.pk',
    #         password= '00000000',
    #     )
    #     # user = User(user)
    #     self.db.add(user)
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return 
    


    # shops_list__ = db.query(EmployeeDB.fk_user, EmployeeDB.id.label('fk_employee'), 
    #                        EmployeeDB.designation.label('designation'), OrderbookerDB.distribution.label('distribution'),
    #                        TownDB.id.label('idtown'), TerritoryDB.id.label('idterritory'),
    #                        AreaDB.id.label('idarea'), ZoneDB.id.label('idzone'),
                           
    #                        RegionDB.id.label('idregion'),func.concat(EmployeeDB.first_name, ' ', EmployeeDB.last_name).label('emp_name'),
    #                        ShopDB.id.label('Shop_id'), 
    #                        func.min(func.date(Secondary_orderDB.date)),
    #                        func.min(cast(Secondary_orderDB.date,Time)),
    #                         ShopDB.name.label('Shop_name'), 
    #                        func.min(coalesce(ShopDB.lat, 0)).label('lat'),
    #                        func.min(coalesce(ShopDB.lng, 0)).label('lng')) \
    # .join(Secondary_orderDB, ShopDB.id == Secondary_orderDB.fk_shop,isouter=True) \
    # .join(EmployeeDB, Secondary_orderDB.fk_orderbooker_employee == EmployeeDB.id,isouter=True)   \
    # .join(OrderbookerDB, EmployeeDB.id == OrderbookerDB.fk_employee,isouter=True) \
    # .join(PjpDB, PjpDB.fk_employee == EmployeeDB.id,isouter=True) \
    # .join(Pjp_weekdayDB, PjpDB.id == Pjp_weekdayDB.fk_pjp,isouter=True) \
    # .join(Pjp_ruleDB, Pjp_weekdayDB.id == Pjp_ruleDB.fk_pjp_weekday,isouter=True) \
    # .join(DistributionDB, OrderbookerDB.distribution == DistributionDB.id,isouter=True) \
    #     \
    # .join(TownDB, DistributionDB.fk_town == TownDB.id,isouter=True) \
    # .join(TerritoryDB, TownDB.fk_territory == TerritoryDB.id,isouter=True) \
    # .join(AreaDB, TerritoryDB.fk_area == AreaDB.id,isouter=True) \
    # .join(ZoneDB, AreaDB.fk_zone == ZoneDB.id,isouter=True) \
    # .join(RegionDB, ZoneDB.fk_region == RegionDB.id,isouter=True) \
    # .filter(func.date(Secondary_orderDB.date) >= startdate) \
    # .filter(func.date(Secondary_orderDB.date) <= enddate) \
    # .group_by(OrderbookerDB.fk_employee, EmployeeDB.id, EmployeeDB.designation, 
    #           OrderbookerDB.distribution, TownDB.id, TerritoryDB.id,
    #           AreaDB.id, ZoneDB.id, RegionDB.id,func.date(Secondary_orderDB.date),EmployeeDB.fk_user, ShopDB.id)
   
    # if emp_id is not None:
    #     shops_list__ = shops_list__.filter(EmployeeDB.id == emp_id)
    # if (designation is not None):
    #     shops_list__ = shops_list_.filter(EmployeeDB.designation.in(designation))
    # if dist_id is not None:
    #     shops_list__ = shops_list__.filter(OrderbookerDB.distribution == dist_id)
    # if town_id is not None:
    #     shops_list__ = shops_list__.filter(TownDB.id == town_id)
    # if territory_id is not None:
    #     shops_list__ = shops_list__.filter(TerritoryDB.id == territory_id)
    # if area_id is not None:
    #     shops_list__ = shops_list__.filter(AreaDB.id == area_id)
    # if zone_id is not None:
    #     shops_list__ = shops_list__.filter(ZoneDB.id == zone_id)
    # if region_id is not None:
    #     shops_list__ = shops_list__.filter(RegionDB.id == region_id)
    # shops_list__ = shops_list__.all()

    """
    SELECT 
    e.fk_user, 
    e.id AS fk_employee, 
    e.designation AS designation, 
    o.distribution AS distribution,
    t.id AS idtown, 
    tt.id AS idterritory,
    a.id AS idarea, 
    z.id AS idzone,
    r.id AS idregion,
    CONCAT(e.first_name, ' ', e.last_name) AS emp_name,
    s.id AS Shop_id, 
    MIN(DATE(so.date)) AS min_date,
    MIN(CAST(so.date AS TIME)) AS min_time,
    s.name AS Shop_name, 
    MIN(COALESCE(s.lat, 0)) AS lat,
    MIN(COALESCE(s.lng, 0)) AS lng
    """