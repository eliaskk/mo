/**
 * Created by admin on 2017/5/29.
 */
$(function () {
    $('#submit').click(function () {
        var diseaseName = $("input[name='diseaseName']").val()
        var patientContent = $("textarea[name='patientContent']").val()
        var contentVec = $("textarea[name='contentVec']").val()
        var prescriptionName = $("input[name='prescriptionName']").val()
        var prescriptions = $("textarea[name='prescriptions']").val()
        var prescriptionsReason = $("textarea[name='prescriptionsReason']").val()
        var sourceFrom = $("input[name='sourceFrom']").val()
        var data = {
                'diseaseName': diseaseName,
                'patientContent': patientContent,
                'contentVec': contentVec,
                'prescriptionName': prescriptionName,
                'prescriptions': prescriptions,
                'prescriptionsReason': prescriptionsReason,
                'sourceFrom': sourceFrom
            }
            $.ajax({
                    cache: false,
                    type: "post",
                    dataType:'json',
                    url:"/prescription-receive",
                    data:data,
                    async: true,
                    success: function(data) {
                        parse(data)
                    },
            });
    })

    function parse(data) {
        alert(data['result'])
    }

})
