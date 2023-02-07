from flask import Blueprint,render_template, request
from .models import Users_desires,Calculations
from . import available_cal_types,gate_images_lst

views = Blueprint("views",__name__)



@views.route("/")
def home():
    return render_template("home1.html")


@views.route("/calculations")
def calculations():
    inps = 5
    if request.args.get("field_changes"):
        inps = request.args.get("field_changes")
    user = Users_desires(available_cal_types,int(inps))
    print(user.numbers)
    if request.method == "GET":
        return render_template("home.html",user=user,num = int(inps))


@views.route("/calculate",methods=['POST'])
def calculate():
    cal = Calculations()
    cal_list = [getattr(cal,func) for func in dir(cal) if callable(getattr(cal, func)) and not func.startswith("__")]
    if request.method == "POST":
        numbers = list(map(int,request.form.getlist("num")))    # get the input numbers 2 -> 10
        calculation_types = list(map(int,request.form.getlist("cal_type"))) # get the calculation types from users 0 -> 5
        bin_and_inps = {}
        identical_counts = {}                          # list to store the binary value of inputs
        images = set()                              # a set to store images associated with user's calculations
        ans = numbers[0]                    # store the firt input to calculate with further inputs 
        # temporary variable  to store the binary value of result and  double append the answer of each calcutaions 
        temp = bin(int(ans))[2:]            
        for idx,num in enumerate(numbers[1:],1):    # loop through with the user's inputs starting index 1
            if ans in bin_and_inps:
                if ans in identical_counts:
                    identical_counts[ans] += 1
                else:
                    identical_counts[ans] = 1
                bin_and_inps[str(ans)+" "*identical_counts[ans]] = temp
            else:
                bin_and_inps[ans] = temp
            if num in bin_and_inps:
                if num in identical_counts:
                    identical_counts[num] += 1
                else:
                    identical_counts[num] = 1
                bin_and_inps[str(num)+" "*identical_counts[num]] = bin(num)[2:]
            else:
                bin_and_inps[num] = bin(num)[2:]
            ans = cal_list[calculation_types[idx-1]](ans,num)
            bin_and_inps["s"+str(idx)] = "-------------------"
            if ans in bin_and_inps:
                if ans in identical_counts:
                    identical_counts[ans] += 1
                else:
                    identical_counts[ans] = 1
                bin_and_inps[str(ans)+" "*identical_counts[ans]] = bin(ans)[2:]
            else:
                bin_and_inps[ans] = bin(ans)[2:]
            bin_and_inps["S"+str(idx)] = "Finished one calculation"
            images.add(gate_images_lst[calculation_types[idx-1]])
    return render_template("explanation.html",ans = ans ,images = images,bin_and_inps= bin_and_inps)


    # for i in range(1,len(numbers)):     # loop through 
    #     bin_numbers.append(temp) 
    #     bin_numbers.append(bin(int(numbers[i]))[2:])
    #     ans = cal_list[int(calculation_types[i-1])](int(ans),int(numbers[i]))
    #     bin_numbers.append("---------------------")
    #     bin_numbers.append(bin(ans)[2:])
    #     bin_numbers.append("Finished one calculation")
    #     temp = bin(ans)[2:]
    #     images.append()
