import datetime
def world_times():
               my_city = datetime.datetime.now()
               berlin = (my_city+datetime.timedelta(hours=0))
               baguio_city = (my_city+datetime.timedelta(hours=8))
               las_vegas = (my_city-datetime.timedelta(hours=9))
               all_times = f"It is {my_city} in my city.That means it's {berlin} in Berlin, {baguio_city} in Baguio City and  {las_vegas} in Las Vegas!"
               print(all_times) 
world_times()
