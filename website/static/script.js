inps = document.getElementById("add_inps")


$(document).on("input",'#add_inps',function(){
    fields = $("#add_inps").val()
    $.ajax({
        type:"get",
        url:"/calculations",
        data : {field_changes:fields},
    })
})