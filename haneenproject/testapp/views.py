from django.shortcuts import render

# Create your views here.
def news_info(request):
	return render(request, 'testapp/index.html')

def movies_info(request):
    head_msg = 'Movie Information'
    sub_msg1 = 'Jailer is very good movie'
    sub_msg2 = 'Planning for aashiqui-3 with Mahesh sir & Sunny Leone'
    sub_msg3 = 'Dont go for movies....practice Django....'
    type = 'movies'
    my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type' : type}
    return render(request,'testapp/news.html',my_dict)

def sport_info(request):
	head_msg = 'Sport Information'
	sub_msg1 = 'Yesterday India won the match'
	sub_msg2 = 'Basketball is my favourit sport'
	sub_msg3 = 'Dont go for Extrem sports'
	type = 'sports'
	my_dict = {'head_msg':head_msg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3, 'type':type}
	return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_msg = 'Politics Information'
    sub_msg1 = 'India PM was Modi Ji'
    sub_msg2 = 'Telangana CM was KCR'
    sub_msg3 = 'Upcoming CM for AP ?????'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3, 'type':type}
    return render(request,'testapp/news.html',my_dict)