$(document).ready(function() {
    $('#example').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5'
        ]
    });
});

$(document).ready(function(){
    $("input").focus(function(){
        $(this).css("background-color", "lavender");
    });
    $("input").blur(function(){
        $(this).css("background-color", "white");
    });
});