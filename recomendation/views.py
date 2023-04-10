from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.core.exceptions import FieldError,ViewDoesNotExist,FieldDoesNotExist


# Create your views here.


def start(request):
    name = 'ederson'
    selected_name = name.replace("_", " ").title()
    mydata = Gk.objects.values_list(
        'player','nation', 'squad','comp', 'age').order_by(name)[1:16]
    mydata = [(x[0], x[1], x[2], x[3],x[4])
              for x in mydata]
    player_info = Gk.objects.get(player=selected_name)
    context = {
        'mydata': mydata,
        'selected_name': selected_name,
        'player_info': player_info,
        'selection': 'Goalkeeper',
        'filtered_nation': 'ALL',
        'filtered_comp': 'ALL',
        'filtered_value': '15',
        'filtered_age': 'ALL',
    }
    return render(request, 'search-page.html', context)


def myview(request):
    if request.method == 'GET':
        name = request.GET.get('search-box')
        selection = request.GET.get('select')
        nation=request.GET.get('nation-filter')
        value=request.GET.get('value-filter')
        age=request.GET.get('age-filter')
        comp=request.GET.get('comp-filter')
        existing_comp = request.GET.get('filtered_comp')
        existing_selection = request.GET.get('selection')
        existing_name=request.GET.get('selected_name')
        existing_nation=request.GET.get('filtered_nation')
        existing_age=request.GET.get('filtered_position')
        existing_value=request.GET.get('filtered_value')

        if name == "":
            name = " "
        name = name.replace(" ", "_").lower()
        selected_name = name.replace("_", " ").title()        
        if selection == '':
            selection = existing_selection
        if age == '':
            age = existing_age
        if value == '':
            value = existing_value
        if nation == '':
            nation = existing_nation
        if comp == '':
            comp = existing_comp
        filtering_age=age
        filtering_value=value
        filtering_nation=nation
        filtering_comp=comp
        if filtering_age=="ALL":
             filtering_age=""
        else:
            filtering_age=int(filtering_age)
        filtering_value=int(filtering_value)
        if filtering_nation=="ALL":
            filtering_nation=""
        if filtering_comp=="ALL":
            filtering_comp=""

        
            
        if selection == 'Goalkeeper':
            try:
                if name:
                    # #print("starting hereeeee....... --------------------------------        --------------------------------\n")
                    # my_object = Gk.objects.values(name).first()
                    mydata=Gk.objects.all()
                    if filtering_age:
                        # #print('entered --------------------------------')
                        mydata=mydata.filter(age__lt=filtering_age)
                    # #print(mydata)
                    # #print('\n now here -------------------------------')
                    if filtering_nation:
                        # #print("entering nationsss---------------")
                        mydata=mydata.filter(nation=filtering_nation)
                    # #print(mydata)
                    # #print('finally hereeeeee')
                    # #print(mydata)
                    if filtering_comp:
                        mydata=mydata.filter(comp=filtering_comp)
                    mydata = mydata.values_list(
                        'player', 'nation', 'squad','comp', 'age').order_by(name)[1:filtering_value+1]
                    player_info = Gk.objects.get(player=selected_name)
                    mydata = [(x[0], x[1], x[2], x[3],x[4]) for x in mydata]
                    
                    context = {
                        "mydata": mydata,
                        "selected_name": selected_name,
                        "player_info": player_info,
                        "selection": selection,                    
                        'filtered_nation': nation,
                        'filtered_comp': comp,
                        'filtered_value': value,
                        'filtered_age': age,

                        # "player_information": player_inf,
                    }
                return render(request, 'search-page.html', context)

        #          Gkeeper._meta.get_field(selected_name)
            except (AttributeError, ValueError, FieldError, IndexError, TypeError, UnboundLocalError,ViewDoesNotExist,FieldDoesNotExist):
                selection = 'Goalkeeper'
            #     # Name is not a valid field name
            #        name = None
                mydata = None
                player_info = None
                player_inf = None
                context = {
                    "mydata": mydata,
                    "selected_name": selected_name,
                    "player_info": player_info,
                    'selection': selection,
                    'filtered_nation': nation,
                    'filtered_comp': comp,
                    'filtered_value': value,
                    'filtered_age': age,


                    # "player_information": player_inf,
                }
                #print(context)
                return render(request, 'search-page.html', context)
        else:
            try:
                selection = 'Others'
                name = selected_name
                if name:
                    identity = Linkers.objects.filter(
                        player=name).values_list('id', flat=True).first()
                    # #print('starting hereeeee....... --------------------------------        --------------------------------\n')

                    #print(identity)

                    # #print('hero is a good person')
                    # #print(identity)
                    search_id = identity
                    # #print('hola       ---------------------------------------------------------------- \n')
                    # #print(search_id)
                    mydata_use=Info.objects.all()
                    #print(mydata_use)

                    if (search_id < 718):
                        # #print('endtered first search --------------------')
                        if filtering_age:
                            # #print('entered age --------------------------------')
                            mydata_use=mydata_use.filter(age__lt=filtering_age)
                        # #print(mydata_use)
                        # #print('\n now here -------------------------------')
                        if filtering_nation:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(nation=filtering_nation)
                        if filtering_comp:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(comp=filtering_comp)
                        
                        # #print(mydata_use)
                        # #print(mydata_use)
                        # #print('out of position -------------------------------')
                        player_info = Info.objects.get(id=search_id)

                        mydata = Output1.objects.values_list('id').order_by(f'-number_{search_id}')
                        # #print(mydata)
                        # #print('saadfdshfsdflkdsjfc--------------------------------------------------------asdflasfd')
                        pi = []
                        for x in mydata:
                            try:
                                data = mydata_use.get(id=x[0])
                                player_i = (x[0], data.nation, data.squad,data.comp, data.age)
                                pi.append(player_i)
                            except mydata_use.model.DoesNotExist:
                                pass
                        # #print(pi)
                        # #print('nowwww npwwww npwwww npwwww npwwww npwwww npwwww')
                        mydata = [str(Linkers.objects.get(id=x[0]).player) for x in pi]
                        # #print('sucess------------------------')
                        # #print(mydata)
                        mydata = [(x, pi[i][1], pi[i][2], pi[i][3], pi[i][4])for i, x in enumerate(mydata)][1:filtering_value+1]
                    
                   

                    elif (search_id >= 718 and search_id < 1437):
                        if filtering_age:
                            # #print('entered age --------------------------------')
                            mydata_use=mydata_use.filter(age__lt=filtering_age)
                        # #print(mydata_use)
                        # #print('\n now here -------------------------------')
                        if filtering_nation:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(nation=filtering_nation)
                        # #print(mydata_use)
                        # #print(mydata_use)
                        # #print('out of position -------------------------------')
                        if filtering_comp:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(comp=filtering_comp)
                        
                        player_info = Info.objects.get(id=search_id)

                        mydata = Output2.objects.values_list('id').order_by(f'-number_{search_id}')
                        # #print(mydata)
                        # #print('saadfdshfsdflkdsjfc--------------------------------------------------------asdflasfd')
                        pi = []
                        for x in mydata:
                            try:
                                data = mydata_use.get(id=x[0])
                                player_i = (x[0], data.nation, data.squad,data.comp ,data.age)
                                pi.append(player_i)
                            except mydata_use.model.DoesNotExist:
                                pass
                        # #print(pi)
                        # #print('nowwww npwwww npwwww npwwww npwwww npwwww npwwww')
                        mydata = [str(Linkers.objects.get(id=x[0]).player) for x in pi]
                        # #print('sucess------------------------')
                        # #print(mydata)
                        # player_info = mydata[0]
                        mydata = [(x, pi[i][1], pi[i][2], pi[i][3], pi[i][4])for i, x in enumerate(mydata)][1:filtering_value+1]

                    else:
                        if filtering_age:
                            # #print('entered age --------------------------------')
                            mydata_use=mydata_use.filter(age__lt=filtering_age)
                        # #print(mydata_use)
                        # #print('\n now here -------------------------------')
                        if filtering_nation:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(nation=filtering_nation)
                        if filtering_comp:
                            # #print("entering nationsss---------------")
                            mydata_use=mydata_use.filter(comp=filtering_comp)
                        
                        # #print(mydata_use)
                        # #print(mydata_use)
                        # #print('out of position -------------------------------')
                        player_info = Info.objects.get(id=search_id)

                        mydata = Output3.objects.values_list('id').order_by(f'-number_{search_id}')
                        # #print(mydata)
                        # #print('saadfdshfsdflkdsjfc--------------------------------------------------------asdflasfd')
                        pi = []
                        for x in mydata:
                            try:
                                data = mydata_use.get(id=x[0])
                                player_i = (x[0], data.nation,data.comp ,data.squad,  data.age)
                                pi.append(player_i)
                            except mydata_use.model.DoesNotExist:
                                pass
                        # #print(pi)
                        # #print('nowwww npwwww npwwww npwwww npwwww npwwww npwwww')
                        mydata = [str(Linkers.objects.get(id=x[0]).player) for x in pi]
                        # #print('sucess------------------------')
                        # #print(mydata)
                        # player_info = mydata[0]
                        mydata = [(x, pi[i][1], pi[i][2], pi[i][3], pi[i][4])for i, x in enumerate(mydata)][1:filtering_value+1]
                    

                    context = {
                        "mydata": mydata,
                        "selected_name": selected_name,
                        "player_info": player_info,
                        "selection": selection,
                        'filtered_nation': nation,
                        'filtered_value': value,
                        'filtered_comp': comp,
                        'filtered_age': age,
                            # "player_information": player_inf,
                    }
                    #print(context)
                    return render(request, 'search-page.html', context)

            except (AttributeError, ValueError, FieldError, IndexError, TypeError,ViewDoesNotExist,FieldDoesNotExist):
                mydata = None
                player_info = None
                player_inf = None
                selection = 'Others'
                context = {
                    "mydata": mydata,
                    "selected_name": selected_name,
                    "player_info": player_info,
                    'selection': selection,
                    'filtered_nation': nation,
                    'filtered_comp': comp,
                    'filtered_value': value,
                    'filtered_age': age,
                    # "player_information": player_inf,
                }
                ##print(context)
                return render(request, 'search-page.html', context)
