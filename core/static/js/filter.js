$(document).ready(function() {
    $('#btnPending').click(function() {
        $("#myTable tr td").each(function() {
            var cell = $(this).text();
            if ($.trim(cell) == 'Pending') {
                $(this).parent().hide();
            }
        });
    });
    $('#btnAccepted').click(function() {
        $("#myTable tr td").each(function() {
            var cell = $(this).text();
            if ($.trim(cell) == 'Accepted') {
                $(this).parent().hide();
            }
        });
    });
     $('#btnReset').click(function() {
        $("#myTable tr").each(function() {
            $(this).show();
        });
    });
});