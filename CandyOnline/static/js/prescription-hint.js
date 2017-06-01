$(function () {

    $('#finish').click(function () {

        var free_text = $('#free').val()
        if (free_text == ''){
            alert('输入的内容不能为空')
        }else {
            send(free_text)
        }
    })

    function send(content) {
        $.ajax({
                    cache: false,
                    type: "post",
                    dataType:'json',
                    url:"/prescription-match",
                    data:{'free_text':content},
                    async: false,
                    success: function(data) {
                        parse(data)
                    },
            });
    }

    function parse(content) {
        if(content['lis'].length>0){
            $('#dynamic').empty()
            for(var v = 0; v<content['lis'].length;v++){
                $('#dynamic').append('<input class="custom_cb" id="check'+v+'" type="checkbox" value="'+content['lis'][v]+'"/> <label for="check'+v+'" class="label label-primary">'
                    +content['lis'][v]+
                '</label>')
                if (v>1 && (v+1)%8==0){
                    $('#dynamic').append('<br><br>')
                }
            }
            $('#hidden').show()
        }
    }


    $('#submit').click(function () {
        jqchk()
    })

    function jqchk(){ //jquery获取复选框值
        var chk_value =[];
        $('input[type="checkbox"]:checked').each(function(){
            chk_value.push($(this).val());
        });
        alert(chk_value.length==0 ?'你还没有选择任何内容！':chk_value);
    }

})