$(function () {

    $("#show").hide();
    $("#submit").click(function () {
        var content = $('#input').val();
        send(content)
    })


    function send(content) {
        $.ajax({
            cache: false,
            type: "post",
            dataType:'json',
            url:"/receive-prescription",
            data:{'content':content},
            async: true,
            success: function(data) {
                parse(data)
            },
        });
    }

    function parse(data) {
        console.log(data)
        $('#show').empty()
        for(var x = 0;x<data.length;x++) {
            $('#show').append("<hr style='height:3px;background-color:black;border:none;margin: 0px auto'>")
            if(x%2!=0) { //原因
                $('#show').append("<h4 style='margin: 1px; padding: 1px;text-indent: 2em; background-color: #c0c0c0; font-weight: bold'>"
                    +"开方原因："+data[x]+"</h4>")
            }else{
                $('#show').append("<h4 style='margin: 1px; padding: 1px;'>"+data[x]+"</h4>")
            }

            $("#show").show()
        }

    }
    
})

